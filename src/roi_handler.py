import threading
import time

from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QImage

from src.stream_receiver import StreamSize

import cv2
import numpy as np
from enum import Enum
from typing import Tuple

SELECTING_ROI_COLOR = (0, 255, 0)
TRACKING_ROI_COLOR = (0, 0, 255)
FAILED_ROI_COLOR = (255, 0, 0)

ROI_THICKNESS_DEFAULT = 1

INIT_START_POINT = [0, 0]
INIT_END_POINT = [0, 0]
INIT_ROI = [0, 0, 0, 0]


class ROIState(Enum):
    NONE = 0
    SELECTING = 1
    TRACKING = 2
    FAILED = 3
    CANCELED = 4


class ROIHandler(QObject):

    roi_selected_signal = Signal(np.ndarray)

    def __init__(self, parent=None, view_label=None, roi_label=None, stream_size=None):
        super().__init__(parent)
        self.parent = parent
        self.roi = INIT_ROI
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT
        self.enabled = False
        self.is_mouse_dragging = False
        self.stream_size = stream_size
        self.tracking_frame_size = stream_size
        self.current_state = ROIState.NONE
        self.view_label = view_label
        self.roi_label = roi_label
        self._stop_smooth_event  = threading.Event()
        self._smooth_update_thread = None
        #self._roi_lock = threading.Lock()


    def enable_roi_selecting(self) -> None:
        self.enabled = True


    def disable_roi_selecting(self) -> None:
        self.enabled = False


    def add_roi_to_frame(self, frame: np.ndarray, p1, p2, color) -> np.ndarray:
        cv_frame = frame.copy()
        cv2.rectangle(cv_frame, p1, p2, color, self.get_roi_thickness())
        return cv_frame


    def qimage_to_cv2_matlike(self, image, width, height) -> np.ndarray:
        rgb_img = image.convertToFormat(QImage.Format.Format_RGBA8888)
        ptr = rgb_img.bits()
        array = np.array(ptr, dtype=np.uint8).reshape((height, width, 4))
        array = cv2.cvtColor(array, cv2.COLOR_RGBA2BGR)
        return array


    def get_roi_thickness(self) -> int:
        if self.stream_size == StreamSize.SIZE_720[1]:
            return 4
        elif self.stream_size == StreamSize.SIZE_480[1]:
            return 2
        elif self.stream_size == StreamSize.SIZE_360[1]:
            return 2
        elif self.stream_size == StreamSize.SIZE_240[1]:
            return 1
        elif self.stream_size == StreamSize.SIZE_144[1]:
            return 1
        else:
            return ROI_THICKNESS_DEFAULT


    def calculate_roi(self) -> np.ndarray:
        pixmap = self.view_label.pixmap()
        if pixmap is None:
            print("Pixmap is empty, can't calculate roi!")
            return None

        x1, y1 = self.start_point
        x2, y2 = self.end_point

        roi_width = abs(x2 - x1)
        roi_height = abs(y2 - y1)

        self.roi = [
            int(min(x1, x2)),
            int(min(y1, y2)),
            int(roi_width),
            int(roi_height),
        ]
        return self.roi


    def update_roi(self, roi) -> None:
        if self.current_state == ROIState.SELECTING:
            return

        if all(v == 0 for v in roi):
            self.change_state(ROIState.FAILED)
        else:
            width_offset = self.stream_size[0] / self.tracking_frame_size[0]
            height_offset = self.stream_size[1] / self.tracking_frame_size[1]
            scaled_roi = (int(roi[0] * width_offset), int(roi[1] * height_offset),
                          int(roi[2] * width_offset), int(roi[3] * height_offset))
            if scaled_roi == self.roi:
                return
            if self._smooth_update_thread is None or not self._smooth_update_thread.is_alive():
                self._stop_smooth_event.clear()
                self._smooth_update_thread = threading.Thread(target=self.smooth_update_roi, args=(scaled_roi,), daemon=True)
                self._smooth_update_thread.start()
            else:
                self._stop_smooth_event.set()
            self.change_state(ROIState.TRACKING)


    def smooth_update_roi(self, new_roi):

        old_roi = self.roi
        t = 0
        tend = 1
        dt = 0.05
        time_sleep = 0.015
        while t != tend and not self._stop_smooth_event.is_set() and self.current_state == ROIState.TRACKING:
            x = (1 - t) * old_roi[0] + t * new_roi[0]
            y = (1 - t) * old_roi[1] + t * new_roi[1]
            w = (1 - t) * old_roi[2] + t * new_roi[2]
            h = (1 - t) * old_roi[3] + t * new_roi[3]
            self.roi = (int(x), int(y), int(w), int(h))
            t = min(t + dt, tend)
            time.sleep(time_sleep)
        #print(t)
        self.roi = new_roi


    def reset_points(self) -> None:
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT


    def reset_roi(self) -> None:
        self.change_state(ROIState.NONE)
        self.roi = INIT_ROI


    def on_left_click_handle_roi(self, pos) -> None:
        if self.current_state == ROIState.CANCELED:
            self.change_state(ROIState.NONE)
            return

        if self.enabled:
            self.is_mouse_dragging = not self.is_mouse_dragging
            if self.is_mouse_dragging:
                self.change_state(ROIState.SELECTING)

                pixmap = self.view_label.pixmap()
                if pixmap is None:
                    return
                x = int(pos.x())
                y = int(pos.y())

                width_ratio = self.stream_size[0] / pixmap.width()
                height_ratio = self.stream_size[1] / pixmap.height()

                offset_x = max(0, (self.view_label.width() - pixmap.width()) // 2)
                offset_y = max(0, (self.view_label.height() - pixmap.height()) // 2)

                self.start_point = [max(0, min(int((x - offset_x) * width_ratio), int(pixmap.width() * width_ratio) - 1)),
                                  max(0, min(int((y - offset_y) * height_ratio), int(pixmap.height() * height_ratio) - 1))]
                self.end_point = self.start_point
            else:
                self.calculate_roi()
                self.reset_points()
                self.change_state(ROIState.NONE)
                if self.roi[2] != 0 and self.roi[3] != 0:
                    self.roi_selected_signal.emit(self.roi)


    def on_right_click_cancel_roi(self, pos) -> None:
        if self.enabled:
            self.reset_points()
            self.reset_roi()
            self.is_mouse_dragging = False
            self.change_state(ROIState.CANCELED)


    def on_mouse_move_draw_roi(self, pos) -> None:
        if self.is_mouse_dragging:

            pixmap = self.view_label.pixmap()
            if pixmap is None:
                return

            x = int(pos.x())
            y = int(pos.y())

            width_ratio = self.stream_size[0] / pixmap.width()
            height_ratio = self.stream_size[1] / pixmap.height()

            offset_x = max(0, (self.view_label.width() - pixmap.width()) // 2)
            offset_y = max(0, (self.view_label.height() - pixmap.height()) // 2)

            self.end_point = [max(0, min(int((x - offset_x) * width_ratio), int(pixmap.width() * width_ratio) - 1)),
                              max(0, min(int((y - offset_y) * height_ratio), int(pixmap.height() * height_ratio) - 1))]


    def set_stream_size(self, stream_size) -> None:
        self.stream_size = stream_size


    def set_tracking_frame_size(self, size) -> None:
        self.tracking_frame_size = size


    def change_state(self, state) -> None:
        self.current_state = state


    def get_roi_points(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        p1 = (self.roi[0], self.roi[1])
        p2 = (self.roi[0] + self.roi[2], self.roi[1] + self.roi[3])
        return p1, p2


    def draw_roi(self, frame) -> np.ndarray:
        if self.current_state == ROIState.SELECTING:
            return self.add_roi_to_frame(frame, self.start_point, self.end_point, TRACKING_ROI_COLOR)
        elif self.current_state == ROIState.TRACKING:
            p1, p2 = self.get_roi_points()
            return self.add_roi_to_frame(frame, p1, p2, SELECTING_ROI_COLOR)
        elif self.current_state == ROIState.FAILED:
            p1, p2 = self.get_roi_points()
            return self.add_roi_to_frame(frame, p1, p2, FAILED_ROI_COLOR)
        return frame


    def draw_roi_on_frame(self, func) -> None:
        def wrapper(*args, **kwargs):
            args = list(args)
            args[0] = self.draw_roi(args[0])
            return func(*args, **kwargs)
        return wrapper
