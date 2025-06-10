# This Python file uses the following encoding: utf-8
import sys
from json import JSONDecodeError

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt, QObject, QEvent, QRegularExpression, Signal
from PySide6.QtGui import QPixmap, QMouseEvent, QRegularExpressionValidator

import datetime
import numpy as np

from src.roi_handler import ROIHandler, ROIState
from src.socket_handler import SocketHandler
from src.stream_receiver import StreamReceiver
from src.viewer import Viewer
from src.tools import numpy_to_pixmap, scale_pixmap, DebugEmitter, increase_grayscale_contrast
from src.command import Command
from src.zeroconf_handler import ZeroconfHandler
from src.widgets_text import *
from src.data import Data

import cv2

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py

from ui_form import Ui_Widget


PARAMS_FILE_NAME = "params"


class Widget(QWidget):

    load_start_state_signal = Signal()
    toggle_view_signal = Signal()
    stream_size_changed_signal = Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        validator = QRegularExpressionValidator(QRegularExpression(r"[0-9]+"))
        self.ui.skip_frame_line_edit.setValidator(validator)
        self.ui.line_edit_c1.setValidator(validator)
        self.ui.line_edit_c2.setValidator(validator)
        self.ui.line_edit_c3.setValidator(validator)
        self.ui.bitrate_line_edit.setValidator(validator)

        self.stream_receiver = StreamReceiver(self)

        self.viewer = Viewer(self, self.stream_receiver)
        self.viewer.frame_ready_signal.connect(self.update_view_label)
        self.viewer.frame_ready_signal.connect(self.update_roi_label)
        self.viewer.play_pressed_signal.connect(self.update_gui_on_play)
        self.viewer.play_pressed_signal.connect(self.start_stream)
        self.viewer.stop_pressed_signal.connect(self.update_gui_on_stop)
        self.viewer.stop_pressed_signal.connect(self.stop_stream)
        self.load_start_state_signal.connect(self.viewer.load_no_connection_view)
        self.toggle_view_signal.connect(self.viewer.toggle_view)

        self.roi_handler = ROIHandler(self, self.ui.view_label, self.ui.roi_label)
        self.roi_handler.roi_selected_signal.connect(self.enable_tracking)
        self.viewer.play_pressed_signal.connect(self.roi_handler.enable_roi_selecting)
        self.viewer.stop_pressed_signal.connect(self.roi_handler.disable_roi_selecting)
        self.stream_size_changed_signal.connect(self.roi_handler.set_stream_size)

        self.update_view_label = self.roi_handler.draw_roi_on_frame(self.update_view_label)  # wrapper
        self.viewer.stop_pressed_signal.connect(self.roi_handler.reset_roi)

        self.view_label_event_filter = MouseEventFilter(
            self.roi_handler.on_left_click_handle_roi,
            self.roi_handler.on_right_click_cancel_roi,
            self.roi_handler.on_mouse_move_draw_roi,
        )
        self.ui.view_label.installEventFilter(self.view_label_event_filter)

        self.socket_handler = SocketHandler(self)
        self.socket_handler.update_roi_signal.connect(self.roi_handler.update_roi)
        self.socket_handler.stop_tracking_signal.connect(self.roi_handler.reset_roi)


        self.debug = DebugEmitter(self)
        self.debug.debug_signal.connect(self.show_debug_message)

        self.zeroconf_handler = ZeroconfHandler()
        self.zeroconf_handler.listener.service_added_signal.connect(self.viewer.change_stream_url)
        self.zeroconf_handler.listener.service_added_signal.connect(self.on_service_added)
        self.zeroconf_handler.listener.service_added_signal.connect(lambda params: self.viewer.load_connection_established_view())
        self.socket_handler.disconnect_from_server_signal.connect(self.on_disconnect_from_server)

        self.start_state = self.capture_start_state()

        self.load_start_state_signal.connect(self.load_start_state)

        self.ui.stream_size_combo_box.addItem("720p")
        self.ui.stream_size_combo_box.addItem("480p")
        self.ui.stream_size_combo_box.addItem("360p")
        self.ui.stream_size_combo_box.addItem("240p")
        self.ui.stream_size_combo_box.addItem("144p")
        self.ui.stream_size_combo_box.currentIndexChanged.connect(self.stream_receiver.change_stream_size_with_index)
        self.stream_receiver.change_stream_size_with_index_signal.connect(self.ui.stream_size_combo_box.setCurrentIndex)

        self.data = Data(self, __file__)
        self.load_saved_parameters()


    def on_service_added(self, params) -> None:
        self.ui.connection_label.setText(f"{CONNECTED_TO} {params['server_ip']}:{params['server_port']}")
        self.ui.toggle_button.setEnabled(True)
        self.ui.tracking_group_box.setEnabled(True)
        self.ui.reboot_server_button.setEnabled(True)
        self.socket_handler.connect(params["server_ip"], params["server_port"])
        self.roi_handler.set_tracking_frame_size(params["tracking_frame_size"])
        self.toggle_view_signal.emit()


    def enable_tracking(self, roi) -> None:
        if not self.viewer.is_playing:
            return
        data = {
            "roi": roi,
            "kalman": self.ui.kalman_radio_button.isChecked(),
            "skip_frames": int(self.ui.skip_frame_line_edit.text()),
            "stream_size": self.stream_receiver.get_stream_size()
        }
        self.socket_handler.send(Command.UPDATE_TRACKING, data)
        self.ui.tracker_stop_button.setEnabled(True)
        self.ui.kalman_group_box.setEnabled(False)


    def start_stream(self) -> None:
        stream_size = self.stream_receiver.get_stream_size()
        data = {
            "stream_size": stream_size,
            "bitrate": int(self.ui.bitrate_line_edit.text())
        }
        self.socket_handler.send(Command.START_STREAM, data)
        self.stream_size_changed_signal.emit(stream_size)


    def stop_stream(self) -> None:
        self.socket_handler.send(Command.STOP_STREAM)


    def update_view_label(self, frame: np.ndarray) -> None:
        pixmap = numpy_to_pixmap(frame)
        size = self.ui.view_label.size()
        scaled_pixmap = scale_pixmap(pixmap, size)
        self.ui.view_label.setPixmap(scaled_pixmap)


    def update_roi_label(self, frame: np.ndarray) -> None:
        if self.roi_handler.current_state != ROIState.TRACKING:
            return
        x, y = self.roi_handler.roi[0], self.roi_handler.roi[1]
        w, h = self.roi_handler.roi[2], self.roi_handler.roi[3]
        contrast = 2
        template = np.array(frame[y:y+h, x:x+w, :], order='C').astype(np.float32) * contrast
        template = np.clip(template, 0, 255).astype(np.uint8)
        pixmap = numpy_to_pixmap(template)
        self.ui.roi_label.setPixmap(scale_pixmap(pixmap, self.ui.roi_label.size()))


    def update_gui_on_play(self) -> None:
        self.ui.toggle_button.setText(STOP_TEXT)
        self.ui.params_group_box.setEnabled(False)


    def update_gui_on_stop(self) -> None:
        self.ui.toggle_button.setText(PLAY_TEXT)
        self.ui.params_group_box.setEnabled(True)


    def capture_start_state(self) -> dict:
        return {
            "connect_button": {
                "text": self.ui.connect_button.text(),
                "enabled": self.ui.connect_button.isEnabled()
            },
            "toggle_button": {
                "text": self.ui.toggle_button.text(),
                "enabled": self.ui.toggle_button.isEnabled()
            },
            "reboot_server_button": {
                "text": self.ui.reboot_server_button.text(),
                "enabled": self.ui.reboot_server_button.isEnabled()
            },
            "kalman_group_box": {
                "enabled": self.ui.kalman_group_box.isEnabled()
            },
            "params_group_box": {
                "enabled": self.ui.params_group_box.isEnabled()
            },
            "cfs_group_box": {
                "enabled": self.ui.cfs_group_box.isEnabled()
            },
            "connection_label": {
                "text": self.ui.connection_label.text()
            }
        }

    def load_saved_parameters(self):
        saved_data = self.data.from_json(PARAMS_FILE_NAME)
        if saved_data is None:
            self.stream_receiver.set_default_stream_size()
            return
        self.ui.kalman_radio_button.setChecked(saved_data["kalman"])
        self.ui.skip_frame_line_edit.setText(str(saved_data["skip_frames"]))
        self.stream_receiver.change_stream_size_with_index(saved_data["stream_size_index"])
        self.ui.bitrate_line_edit.setText(str(saved_data["bitrate"]))

    def save_parameters(self):
        self.data.to_json(PARAMS_FILE_NAME, {
            "kalman": self.ui.kalman_radio_button.isChecked(),
            "skip_frames": int(self.ui.skip_frame_line_edit.text()),
            "stream_size_index": self.stream_receiver.get_stream_size_index(),
            "bitrate": int(self.ui.bitrate_line_edit.text())
        })


    def show_debug_message(self, msg: str) -> None:
        current_datetime = datetime.datetime.now().strftime("%X")
        new_line = f"({current_datetime}) {msg}"
        if self.debug.last_message == msg:
            cursor = self.ui.debug_plain_text_edit.textCursor()
            cursor.movePosition(cursor.MoveOperation.StartOfBlock, cursor.MoveMode.KeepAnchor)
            cursor.removeSelectedText()
            cursor.insertText(new_line + f" ( x{self.debug.last_message_count} )")
            self.ui.debug_plain_text_edit.setTextCursor(cursor)
        else:
            self.ui.debug_plain_text_edit.appendPlainText(new_line)


    def load_start_state(self):
        self.ui.connect_button.setText(self.start_state["connect_button"]["text"])
        self.ui.connect_button.setEnabled(self.start_state["connect_button"]["enabled"])
        self.ui.toggle_button.setText(self.start_state["toggle_button"]["text"])
        self.ui.toggle_button.setEnabled(self.start_state["toggle_button"]["enabled"])
        self.ui.reboot_server_button.setText(self.start_state["reboot_server_button"]["text"])
        self.ui.reboot_server_button.setEnabled(self.start_state["reboot_server_button"]["enabled"])
        self.ui.kalman_group_box.setEnabled(self.start_state["kalman_group_box"]["enabled"])
        self.ui.params_group_box.setEnabled(self.start_state["params_group_box"]["enabled"])
        self.ui.cfs_group_box.setEnabled(self.start_state["cfs_group_box"]["enabled"])
        self.ui.connection_label.setText(self.start_state["connection_label"]["text"])


    def on_disconnect_from_server(self):
        self.viewer.stop()
        self.zeroconf_handler.clear()
        self.load_start_state_signal.emit()


    def closeEvent(self, e) -> None:
        self.save_parameters()
        self.viewer.stop()
        self.zeroconf_handler.clear()
        e.accept()


    @QtCore.Slot()
    def on_connect_button_clicked(self) -> None:
        self.zeroconf_handler.browse()
        self.ui.connection_label.setText(CONNECTION_AWATING)
        self.ui.connect_button.setEnabled(False)
        self.ui.cfs_group_box.setEnabled(True)


    @QtCore.Slot()
    def on_toggle_button_clicked(self) -> None:
        self.toggle_view_signal.emit()


    @QtCore.Slot()
    def on_tracker_stop_button_clicked(self) -> None:
        self.socket_handler.send(Command.STOP_TRACKING)
        self.ui.tracker_stop_button.setEnabled(False)
        self.ui.kalman_group_box.setEnabled(True)


    @QtCore.Slot()
    def on_reboot_server_button_clicked(self) -> None:
        reply = QMessageBox.question(self, "Stream Receiver", RESTART_SERVER, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.load_start_state_signal.emit()
            self.socket_handler.send(Command.REBOOT_SERVER)
            self.socket_handler.disconnect()



class MouseEventFilter(QObject):
    def __init__(self, callback_left_button=None, callback_right_button=None, callback_move=None):
        super().__init__()
        self.callback_left_button = callback_left_button
        self.callback_right_button = callback_right_button
        self.callback_move = callback_move


    def eventFilter(self, obj, event) -> bool:
        if type(event) is QMouseEvent:
            if event.button() == Qt.LeftButton:
                if self.callback_left_button is not None:
                    self.callback_left_button(event.position())
            elif event.button() == Qt.RightButton and event.type() == QEvent.MouseButtonPress:
                if self.callback_right_button is not None:
                    self.callback_right_button(event.position())
            else:
                if self.callback_move is not None:
                    self.callback_move(event.position())
            return True
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
