import numpy as np
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, Signal, QObject


def numpy_to_pixmap(array: np.ndarray) -> QPixmap:
    """
    Returns a QPixmap from a numpy array.
    :param array:
    :return QPixmap:
    """
    h, w, ch = array.shape
    bytes_per_line = ch * w
    image = QImage(array, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(image)


def scale_pixmap(size, pixmap) -> QPixmap:
    """
    Scales a QPixmap to a given size.
    :param size:
    :param pixmap:
    :return QPixmap:
    """
    return pixmap.scaled(size, Qt.KeepAspectRatio, Qt.FastTransformation)


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


    def send(self, msg: str) -> None:
        self.debug_signal.emit(msg)
        print(f"<debug> {msg}")