from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap

from src.tools import numpy_to_pixmap, DebugEmitter
from src.stream_receiver import StreamReceiver

import threading
import numpy as np
import time
from pathlib import Path

TARGET_FPS = 30
TARGET_FRAME_TIME = 1 / TARGET_FPS

NO_CONNECTION_IMAGE = Path(__file__).parent / "img/no_connection.png"
CONNECTION_ESTABLISHED_IMAGE = Path(__file__).parent  / "img/connection_established.png"


class Viewer(QWidget):

    frame_ready_signal = Signal(np.ndarray)
    play_pressed_signal = Signal()
    stop_pressed_signal = Signal()


    def __init__(self, parent=None, stream_receiver: StreamReceiver = None):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.current_frame = None
        self.view_thread = None
        self.stream_receiver = stream_receiver
        self.is_playing = False
        self.stream_url = None

        self.debug = DebugEmitter()

        self.load_no_connection_view()


    def load_connection_established_view(self):
        self.load_image_view(CONNECTION_ESTABLISHED_IMAGE)


    def load_no_connection_view(self):
        self.load_image_view(NO_CONNECTION_IMAGE)


    def load_image_view(self, view_image) -> None:
        """
        Loads the image view
        :return None:
        """
        try:
            no_connection = QPixmap(view_image)
            if no_connection.isNull():
                raise Exception(f"Specified image path is incorrect {view_image}")
            self.ui.view_label.setPixmap(no_connection)
        except Exception as e:
            self.debug.send(f"Error loading image view: {e}")


    def update(self) -> None:
        """
        Updates the view by sending signal with current frame
        :return None:
        """
        while self.is_playing:
            start_time = time.time()
            try:
                frame = self.stream_receiver.get_current_frame()
                if frame is None:
                    continue
                self.current_frame = frame
                self.frame_ready_signal.emit(frame)
            except Exception as e:
                self.debug.send(f"Error updating view: {e}")

            end_time = time.time() - start_time
            if end_time < TARGET_FRAME_TIME:
                time.sleep(TARGET_FRAME_TIME - end_time)


    def change_stream_url(self, stream_params) -> None:
        """
        Changes the stream url using stream parameters
        :param stream_params:
        :return None:
        """
        if "stream_ip" in stream_params and "stream_port" in stream_params:
            self.stream_url = f"{stream_params['stream_protocol']}://{stream_params['stream_ip']}:{stream_params['stream_port']}"
        else:
            self.debug.send("Invalid stream parameters")


    def play(self) -> None:
        """
        Play the stream
        :return None:
        """
        self.is_playing = True
        self.stream_receiver.start(self.stream_url)
        self.view_thread = threading.Thread(target=self.update, daemon=True)
        self.view_thread.start()
        self.play_pressed_signal.emit()


    def stop(self) -> None:
        """
        Stop the stream
        :return None:
        """
        self.is_playing = False
        self.stream_receiver.stop()
        self.load_connection_established_view()
        self.stop_pressed_signal.emit()



    def toggle_view(self) -> None:
        try:
            if not self.is_playing:
                self.play()
            else:
                self.stop()
        except Exception as e:
            self.debug.send(f"Error occurred when toggle button was pressed: {e}")
