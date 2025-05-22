from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QPixmap, QImage

from src.tools import numpy_to_pixmap
import cv2
import numpy as np

ROI_COLOR = (0, 0, 255)
ROI_THICKNESS = 2

INIT_START_POINT = [0, 0]
INIT_END_POINT = [0, 0]
INIT_ROI = [0, 0, 0, 0]

class ROIHandler(QObject):

    roi_selected_signal = Signal(np.ndarray)

    def __init__(self, parent=None, view_label=None, stream_size=(640, 480)):
        super().__init__(parent)
        self.parent = parent
        self.roi = INIT_ROI
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT
        self.enabled = True
        self.is_mouse_dragging = False
        self.stream_size = stream_size

        self.view_label = view_label


    def enable_roi_selecting(self) -> None:
        self.enabled = True


    def disable_roi_selecting(self) -> None:
        self.enabled = False


    def add_roi_to_frame(self, frame: np.ndarray, p1, p2) -> np.ndarray:
        cv_frame = frame.copy()
        cv2.rectangle(cv_frame, p1, p2, ROI_COLOR, ROI_THICKNESS)
        return cv_frame


    def qimage_to_cv2_matlike(self, image, width, height) -> np.ndarray:
        rgb_img = image.convertToFormat(QImage.Format.Format_RGBA8888)
        ptr = rgb_img.bits()
        array = np.array(ptr, dtype=np.uint8).reshape((height, width, 4))
        array = cv2.cvtColor(array, cv2.COLOR_RGBA2BGR)
        return array


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


    def reset_points(self):
        self.start_point = INIT_START_POINT
        self.end_point = INIT_END_POINT


    def reset_roi(self):
        self.roi = INIT_ROI


    def handle_roi(self, pos) -> None:
        if self.enabled:
            self.is_mouse_dragging = not self.is_mouse_dragging
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

                self.start_point = [max(0, min(int((x - offset_x) * width_ratio), int(pixmap.width() * width_ratio) - 1)),
                                  max(0, min(int((y - offset_y) * height_ratio), int(pixmap.height() * height_ratio) - 1))]

                self.end_point = self.start_point
            else:
                self.calculate_roi()
                self.reset_points()
                self.roi_selected_signal.emit(self.roi)


    def cancel_roi(self, pos) -> None:
        if self.enabled:
            self.reset_points()
            self.reset_roi()


    def draw_roi(self, pos) -> None:
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


    def draw_roi_on_pixmap(self, func) -> None:
        def wrapper(*args, **kwargs):
            args = list(args)
            frame = args[0]
            if self.enabled and (self.start_point != INIT_START_POINT or self.end_point != INIT_END_POINT):
                args[0] = self.add_roi_to_frame(frame, self.start_point, self.end_point)
            return func(*args, **kwargs)
        return wrapper
