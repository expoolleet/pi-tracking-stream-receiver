from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap

from src.tools import numpy_to_pixmap, DebugEmitter
from src.streamer import Streamer

import threading
import numpy as np
import time

NO_CONNECTION_IMAGE = "src/img/no_connection.png"

TARGET_FPS = 30
TARGET_FRAME_TIME = 1 / TARGET_FPS


class Viewer(QWidget):

    frame_ready_signal = Signal(np.ndarray)
    play_pressed_signal = Signal()
    stop_pressed_signal = Signal()


    def __init__(self, parent=None, streamer: Streamer = None):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.ui.toggle_button.clicked.connect(self.on_toggle_button_clicked)
        self.load_default_view()
        self.current_frame = self.ui.viewLabel.pixmap()
        self.view_thread = None
        self.streamer = streamer
        self.is_playing = False
        self.debug = DebugEmitter()
        self.stream_url = None


    def load_default_view(self) -> None:
        """
        Load the default view
        :return None:
        """
        try:
            no_connection = QPixmap(NO_CONNECTION_IMAGE)
            self.ui.viewLabel.setPixmap(no_connection)
        except Exception as e:
            self.debug.send(f"Error loading default view: {e}")
            black_frame = np.zeros((480, 640, 3), dtype=np.uint8)
            self.ui.viewLabel.setPixmap(numpy_to_pixmap(black_frame))


    def update(self) -> None:
        """
        Update the view
        :return None:
        """
        while self.is_playing:
            start_time = time.time()
            try:
                frame = self.streamer.get_current_frame()
                qpixmap = numpy_to_pixmap(frame)
                self.current_frame = qpixmap
                self.frame_ready_signal.emit(frame)
            except Exception as e:
                self.debug.send(f"Error updating view: {e}")

            end_time = time.time() - start_time
            if end_time < TARGET_FRAME_TIME:
                time.sleep(TARGET_FRAME_TIME - end_time)


    def change_stream_url(self, stream_params) -> None:
        if "stream_ip" in stream_params and "stream_port" in stream_params:
            self.stream_url = f"{stream_params['stream_protocol']}://{stream_params['stream_ip']}:{stream_params['stream_port']}"
        else:
            self.debug.send("Invalid stream parameters")

    def play(self) -> None:
        """
        Play the stream
        :return:
        """
        self.is_playing = True
        self.streamer.start(self.stream_url)
        self.view_thread = threading.Thread(target=self.update, daemon=True)
        self.view_thread.start()
        self.play_pressed_signal.emit()


    def stop(self) -> None:
        """
        Stop the stream
        :return:
        """
        self.is_playing = False
        self.streamer.stop()
        self.stop_pressed_signal.emit()


    @QtCore.Slot()
    def on_toggle_button_clicked(self) -> None:
        try:
            if not self.is_playing:
                self.play()
            else:
                self.stop()
        except Exception as e:
            self.debug.send(f"Error occurred when toggle button was pressed: {e}")
