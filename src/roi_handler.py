import threading
import time

from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QImage

from src.stream_receiver import StreamSize

import cv2
import numpy as np
from enum import Enum
from typing import Tuple

from src.tools import DebugEmitter

SELECTING_ROI_COLOR = (0, 0, 255)
TRACKING_ROI_COLOR = (0, 255, 0)
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
    FAST_SELECTING = 5


class ROIHandler(QObject):

    roi_selected_signal = Signal(np.ndarray)

    def __init__(self, parent=None, view_label=None, roi_label=None, stream_size=None):
        super().__init__(parent)
        self.parent = parent
        self.roi = INIT_ROI
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT
        self.enabled = False
        self.stream_size = stream_size
        self.tracking_frame_size = stream_size
        self.current_state = ROIState.NONE
        self.last_state = None
        self.view_label = view_label
        self.roi_label = roi_label

        self._stop_smooth_event  = threading.Event()
        self._smooth_update_thread = None
        self._is_mouse_pressed = False
        self._roi_lock = threading.Lock()

        self.debug = DebugEmitter()


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
            self.debug.send("Pixmap is empty, can't calculate roi!")
            return None

        x1, y1 = self.start_point
        x2, y2 = self.end_point

        roi_width = abs(x2 - x1)
        roi_height = abs(y2 - y1)

        roi = [
            int(min(x1, x2)),
            int(min(y1, y2)),
            int(roi_width),
            int(roi_height),
        ]
        return roi


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
        dt = 0.1
        time_sleep = 0.01
        while t != tend and not self._stop_smooth_event.is_set() and self.current_state == ROIState.TRACKING:
            x = (tend - t) * old_roi[0] + t * new_roi[0]
            y = (tend - t) * old_roi[1] + t * new_roi[1]
            w = (tend - t) * old_roi[2] + t * new_roi[2]
            h = (tend - t) * old_roi[3] + t * new_roi[3]
            with self._roi_lock:
                self.roi = [int(x), int(y), int(w), int(h)]
            t = min(t + dt, tend)
            time.sleep(time_sleep)
        with self._roi_lock:
            self.roi = new_roi


    def reset_points(self) -> None:
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT


    def reset_roi(self) -> None:
        self.change_state(ROIState.NONE)
        with self._roi_lock:
            self.roi = INIT_ROI

    def try_reset_roi(self) -> bool:
        if self.current_state == ROIState.FAST_SELECTING:
            return False
        self.change_state(ROIState.NONE)
        with self._roi_lock:
            self.roi = INIT_ROI
        return True


    def on_key_pressed_try_send_roi(self) -> None:
        if not self.enabled or self.current_state != ROIState.FAST_SELECTING:
            return
        self.debug.send("Sending ROI to the server...")
        self.try_send_roi()


    def on_left_click_handle_roi(self, pos) -> None:
        if not self.enabled or self.current_state == ROIState.TRACKING:
            return

        if self.current_state == ROIState.CANCELED:
            self.change_state(ROIState.NONE)
            return

        if self.current_state == ROIState.FAST_SELECTING:
            self._is_mouse_pressed = True
            if self.try_send_roi():
                self.change_state(ROIState.NONE)
            return

        self._is_mouse_pressed = not self._is_mouse_pressed
        if self._is_mouse_pressed:
            pixmap = self.view_label.pixmap()
            if pixmap is None:
                return
            x = int(pos.x())
            y = int(pos.y())

            width_ratio = self.stream_size[0] / pixmap.width()
            height_ratio = self.stream_size[1] / pixmap.height()

            offset_x = max(0, (self.view_label.width() - pixmap.width()) // 2)
            offset_y = max(0, (self.view_label.height() - pixmap.height()) // 2)

            self.start_point = [
                max(0, min(int((x - offset_x) * width_ratio), int(pixmap.width() * width_ratio) - 1)),
                max(0, min(int((y - offset_y) * height_ratio), int(pixmap.height() * height_ratio) - 1))]
            self.end_point = self.start_point
            self.change_state(ROIState.SELECTING)
        elif self.last_state != ROIState.FAST_SELECTING:
            if self.try_send_roi():
                self.change_state(ROIState.NONE)


    def on_right_click_cancel_roi(self, pos) -> None:
        if not self.enabled or self.current_state == ROIState.TRACKING:
            return
        self.reset_points()
        self.reset_roi()
        self._is_mouse_pressed = False
        self.change_state(ROIState.CANCELED)


    def on_mouse_move_draw_roi(self, pos) -> None:
        if self.view_label.pixmap() is None:
            return

        if self.view_label.pixmap() is None or not self.enabled:
            return

        x = int(pos.x())
        y = int(pos.y())
        if self.current_state == ROIState.FAST_SELECTING:
            pixmap = self.view_label.pixmap()
            offset_x, offset_y, width_ratio, height_ratio = self.calculate_offsets_and_size_ratios(pixmap)

            x1 = int((x - offset_x) * width_ratio - self.roi[2] // 2)
            y1 = int((y - offset_y) * height_ratio - self.roi[3] // 2)
            x2 = x1 + self.roi[2]
            y2 = y1 + self.roi[3]
            with self._roi_lock:
                self.roi = [x1, y1, self.roi[2], self.roi[3]]
            self.start_point = [x1, y1]
            self.end_point = [x2, y2]

        elif self._is_mouse_pressed:
            pixmap = self.view_label.pixmap()
            offset_x, offset_y, width_ratio, height_ratio = self.calculate_offsets_and_size_ratios(pixmap)

            self.end_point = [max(0, min(int((x - offset_x) * width_ratio), int(pixmap.width() * width_ratio) - 1)),
                              max(0, min(int((y - offset_y) * height_ratio), int(pixmap.height() * height_ratio) - 1))]


    def calculate_offsets_and_size_ratios(self, pixmap) -> tuple[int, int, float, float]:
        width_ratio = self.stream_size[0] / pixmap.width()
        height_ratio = self.stream_size[1] / pixmap.height()
        offset_x = max(0, (self.view_label.width() - pixmap.width()) // 2)
        offset_y = max(0, (self.view_label.height() - pixmap.height()) // 2)
        return offset_x, offset_y, width_ratio, height_ratio


    def try_send_roi(self) -> bool:
        with self._roi_lock:
            self.roi = self.calculate_roi()
        self.reset_points()
        if self.roi[2] != 0 and self.roi[3] != 0:
            self.roi_selected_signal.emit(self.roi)
            return True
        self.debug.send("Cannot send roi: width and length are zeros")
        return False


    def get_roi(self) -> list[int, int, int, int]:
        with self._roi_lock:
            return self.roi


    def handle_fast_roi(self, enabled, width, height) -> None:
        if enabled:
            center_point = (self.stream_size[0] // 2, self.stream_size[1] // 2)
            x = center_point[0] - width // 2
            y = center_point[1] - height // 2

            roi = [x, y, width, height]

            with self._roi_lock:
                self.roi = roi
            self.start_point = [roi[0], roi[1]]
            self.end_point = [roi[0] + roi[2], roi[1] + roi[3]]
            self.change_state(ROIState.FAST_SELECTING)
        else:
            self.change_state(ROIState.NONE)


    def reset_fast_roi(self) -> None:
        center_point = (self.stream_size[0] // 2, self.stream_size[1] // 2)
        with self._roi_lock:
            x = center_point[0] - self.roi[2] // 2
            y = center_point[1] - self.roi[3] // 2
            roi = [x, y, self.roi[2], self.roi[3]]
            self.roi = roi
        self.start_point = [roi[0], roi[1]]
        self.end_point = [roi[0] + roi[2], roi[1] + roi[3]]


    def set_stream_size(self, stream_size) -> None:
        self.stream_size = stream_size


    def set_tracking_frame_size(self, size) -> None:
        self.tracking_frame_size = size


    def change_state(self, state) -> None:
        if self.current_state == state:
            return
        self.last_state = self.current_state
        self.current_state = state


    def get_roi_points(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        with self._roi_lock:
            p1 = (self.roi[0], self.roi[1])
            p2 = (self.roi[0] + self.roi[2], self.roi[1] + self.roi[3])
        return p1, p2


    def draw_roi(self, frame) -> np.ndarray:
        if self.current_state == ROIState.SELECTING or self.current_state == ROIState.FAST_SELECTING:
            return self.add_roi_to_frame(frame, self.start_point, self.end_point, SELECTING_ROI_COLOR)
        elif self.current_state == ROIState.TRACKING:
            p1, p2 = self.get_roi_points()
            return self.add_roi_to_frame(frame, p1, p2, TRACKING_ROI_COLOR)
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
