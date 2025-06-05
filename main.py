# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt, QObject, QEvent, QRegularExpression, Signal
from PySide6.QtGui import QPixmap, QMouseEvent, QRegularExpressionValidator

import datetime
import numpy as np

from src.roi_handler import ROIHandler
from src.socket_handler import SocketHandler
from src.streamer import Streamer
from src.viewer import Viewer
from src.tools import numpy_to_pixmap, scale_pixmap, DebugEmitter
from src.command import Command
from src.zeroconf_handler import ZeroconfHandler
from src.widgets_text import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py

from ui_form import Ui_Widget


class Widget(QWidget):

    load_start_state_signal = Signal()
    toggle_view_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        validator = QRegularExpressionValidator(QRegularExpression(r"[0-9]+"))
        self.ui.skip_frame_line_edit.setValidator(validator)
        self.ui.line_edit_c1.setValidator(validator)
        self.ui.line_edit_c2.setValidator(validator)
        self.ui.line_edit_c3.setValidator(validator)

        self.streamer = Streamer(self, stream_size=(640, 480))

        self.viewer = Viewer(self, self.streamer)
        self.viewer.frame_ready_signal.connect(self.update_view_label)
        self.viewer.play_pressed_signal.connect(self.update_gui_on_play)
        self.viewer.stop_pressed_signal.connect(self.update_gui_on_stop)
        self.roi_handler = ROIHandler(self, self.ui.viewLabel)
        self.roi_handler.enable_roi_selecting()
        self.roi_handler.roi_selected_signal.connect(self.enable_tracking)
        self.update_view_label = self.roi_handler.draw_roi_on_frame(self.update_view_label)  # wrapper
        self.viewer.stop_pressed_signal.connect(self.roi_handler.reset_roi)

        self.viewLabel_event_filter = MouseEventFilter(
            self.roi_handler.on_left_click_handle_roi,
            self.roi_handler.on_right_click_cancel_roi,
            self.roi_handler.on_mouse_move_draw_roi,
        )
        self.ui.viewLabel.installEventFilter(self.viewLabel_event_filter)

        self.socket_handler = SocketHandler(self)
        self.socket_handler.update_roi_signal.connect(self.roi_handler.update_roi)
        self.socket_handler.stop_tracking_signal.connect(self.roi_handler.reset_roi)

        self.debug = DebugEmitter(self)
        self.debug.debug_signal.connect(self.show_debug_message)

        self.zeroconf_handler = ZeroconfHandler()
        self.zeroconf_handler.listener.service_added_signal.connect(self.viewer.change_stream_url)
        self.zeroconf_handler.listener.service_added_signal.connect(self.on_service_added)
        self.zeroconf_handler.listener.service_added_signal.connect(lambda params: self.viewer.load_connection_established_view())

        self.start_state = self.capture_start_state()

        self.load_start_state_signal.connect(self.load_start_state)


    def on_service_added(self, params) -> None:
        self.ui.connection_label.setText(f"{CONNECTED_TO} {params['server_ip']}:{params['server_port']}")
        self.ui.toggle_button.setEnabled(True)
        self.ui.tracking_group_box.setEnabled(True)
        self.socket_handler.connect(params["server_ip"], params["server_port"])
        self.socket_handler.send(Command.CONNECT_TO_SERVER)


    def enable_tracking(self, roi) -> None:
        if not self.viewer.is_playing:
            return
        data = {
            "roi": roi,
            "kalman": self.ui.kalman_radio_button.isChecked(),
            "skip_frames": int(self.ui.skip_frame_line_edit.text())
        }
        self.socket_handler.send(Command.UPDATE_TRACKING, data)
        self.ui.tracker_stop_button.setEnabled(True)
        self.ui.kalman_group_box.setEnabled(False)


    def update_view_label(self, frame: np.ndarray) -> None:
        pixmap = numpy_to_pixmap(frame)
        self.ui.viewLabel.setPixmap(self.resize_pixmap(pixmap))


    def update_gui_on_play(self) -> None:
        self.ui.toggle_button.setText(STOP_TEXT)
        self.ui.params_group_box.setEnabled(False)


    def update_gui_on_stop(self) -> None:
        self.ui.toggle_button.setText(PLAY_TEXT)
        self.ui.params_group_box.setEnabled(True)


    def resize_pixmap(self, pixmap) -> QPixmap:
        scaled_pixmap = scale_pixmap(self.ui.viewLabel.size(), pixmap)  # fix later
        return scaled_pixmap


    def show_debug_message(self, msg: str) -> None:
        current_datetime = datetime.datetime.now()
        self.ui.debug_plain_text_edit.appendPlainText(f"({current_datetime}) {msg}")


    def closeEvent(self, e) -> None:
        if self.streamer:
            self.streamer.stop()
        e.accept()


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


    @QtCore.Slot()
    def on_connect_button_clicked(self) -> None:
        self.zeroconf_handler.browse()
        self.ui.connection_label.setText(CONNECTION_AWATING)
        self.ui.connect_button.setEnabled(False)
        self.ui.reboot_server_button.setEnabled(True)
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
        reply = QMessageBox.question(self, "Streamer", RESTART_SERVER, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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
