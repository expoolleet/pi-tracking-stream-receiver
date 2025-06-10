import os
import numpy as np
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, Signal, QObject
import logging
import inspect

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def numpy_to_pixmap(array: np.ndarray, color="rgb24") -> QPixmap:
    """
    Returns a QPixmap from a numpy array.
    :param array: Numpy image
    :param color: String color
    :return QPixmap: QPixmap image
    """

    bytes_per_line = 0
    format = QImage.Format_Invalid

    if color == "rgb24":
        h, w, ch = array.shape
        format = QImage.Format_RGB888
        bytes_per_line = ch * w
    elif color == "gray":
        h, w = array.shape
        format = QImage.Format_Grayscale8
        bytes_per_line = w

    if format == QImage.Format_Invalid or bytes_per_line == 0:
        raise ValueError(f"Unsupported color format: {color}")

    image = QImage(array, w, h, bytes_per_line, format)
    return QPixmap.fromImage(image)


def scale_pixmap(pixmap, size) -> QPixmap:
    """
    Scales a QPixmap to a given size.
    :param pixmap: QPixmap image
    :param size: tuple with width and height
    :return QPixmap: scaled QPixmap image
    """
    return pixmap.scaled(size, Qt.KeepAspectRatio, Qt.FastTransformation)


def increase_grayscale_contrast(image, c = 1.0):
    transformed_image = c * np.log(image + 1)
    max_value = np.max(transformed_image)
    if max_value > 0:
        transformed_image = (transformed_image / max_value) * 255
    else:
        transformed_image = transformed_image * 0
    #print(transformed_image)
    return transformed_image.astype(np.uint8)


class DebugEmitter(QObject):

    debug_signal = Signal(str)

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DebugEmitter, cls).__new__(cls)
        return cls._instance


    def __init__(self, parent=None):
        if getattr(self, "_initialized", False):
            return
        super().__init__(parent)
        self._initialized = True
        self.last_message = None
        self.last_message_count = 1


    def send(self, msg: str) -> None:
        try:
            self.debug_signal.emit(msg)
            frame = inspect.stack()[1]
            logging.debug(f"{os.path.basename(frame.filename)}:{frame.lineno} - {msg}")
        except RuntimeError:
            self.debug.send("Warning: signal 'debug_signal' has been deleted because application is closed")
        finally:
            if self.last_message == msg:
                self.last_message_count += 1
            else:
                self.last_message_count = 1
                self.last_message = msg
