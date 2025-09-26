from collections.abc import Callable

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap

from src.tools import numpy_to_pixmap, DebugEmitter, get_base_path
from src.stream_receiver import StreamReceiver

import threading
import numpy as np
import time
import sys
import cv2
from pathlib import Path

base_path = get_base_path(__file__)

NO_CONNECTION_IMAGE = base_path / "img" / "no_connection.png"
CONNECTION_ESTABLISHED_IMAGE = base_path / "img" / "connection_established.png"

class Viewer(QWidget):

    frame_ready_signal = Signal(np.ndarray)
    play_pressed_signal = Signal()
    stop_pressed_signal = Signal()


    def __init__(self, parent=None, stream_receiver: StreamReceiver=None, frame_rate=60):
        super().__init__(parent)
        self.parent = parent
        self.ui = parent.ui
        self.current_frame = None
        self.view_thread = None
        self.stream_receiver = stream_receiver
        self.is_playing = False
        self.stream_url = None
        self.tracking_frame_size = (0, 0)
        self.black_frame = None

        self.debug = DebugEmitter()

        self.load_no_connection_view()

        self.frame_rate = frame_rate
        self.frame_time = 1.0 / frame_rate

        try:
            self.system_camera = cv2.VideoCapture(0)
            if self.system_camera.isOpened() and self.system_camera.get(cv2.CAP_PROP_FPS) < 1:
                raise Exception("System camera is not working")
        except Exception as e:
            self.debug.send(f"Error initializing system camera: {e}")
            self.system_camera = None

        self._is_playing_lock = threading.Lock()


    def load_connection_established_view(self) -> None:
        self.load_image_view(CONNECTION_ESTABLISHED_IMAGE)


    def load_no_connection_view(self) -> None:
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


    def set_frame_rate(self, frame_rate) -> None:
        self.frame_rate = frame_rate
        self.frame_time = 1 / frame_rate


    def update_frame(self, update_callback: Callable) -> None:
        """
        Updates the view from the callback by sending signal with current frame
        :return None:
        """
        while True:
            with self._is_playing_lock:
                is_playing = self.is_playing
            if not is_playing:
                break
            start_time = time.time()
            try:
                frame = update_callback()
                if frame is None:
                    continue
                self.current_frame = frame
                self.frame_ready_signal.emit(frame)
            except Exception as e:
                self.debug.send(f"Error updating view: {e}")

            elapsed_time = time.time() - start_time
            if elapsed_time < self.frame_time:
                time.sleep(self.frame_time - elapsed_time)


    def update_from_stream(self) -> None:
        """
        Updates the view from the stream
        :return None:
        """
        self.update_frame(self.stream_receiver.get_current_frame)


    def update_from_system_camera(self) -> None:
        """
        Updates the view from the system camera
        :return None:
        """
        self.update_frame(
            lambda: cv2.resize(
                cv2.cvtColor(self.system_camera.read()[1], cv2.COLOR_BGR2RGB),
                self.tracking_frame_size,
                cv2.INTER_LINEAR)
            if self.system_camera and self.system_camera.read()[0]
            else self.black_frame)


    def set_tracking_frame_size(self, size):
        self.tracking_frame_size = size
        self.black_frame = np.zeros((size[1], size[0], 3), dtype=np.uint8)


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
        with self._is_playing_lock:
            self.is_playing = True

        if self.ui.stream_check_box.isChecked():
            self.stream_receiver.start(self.stream_url)
            self.view_thread = threading.Thread(target=self.update_from_stream, daemon=True)
        if self.ui.transmitter_check_box.isChecked():
            self.view_thread = threading.Thread(target=self.update_from_system_camera, daemon=True)

        if self.view_thread is None:
            self.debug.send("Warning: View thread is None!")
            return
        self.view_thread.start()
        self.play_pressed_signal.emit()


    def stop(self) -> None:
        """
        Stop the stream
        :return None:
        """
        with self._is_playing_lock:
            self.is_playing = False

        if self.ui.stream_check_box.isChecked():
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
