# This Python file uses the following encoding: utf-8
import sys
import datetime
import threading

import numpy as np

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt, QObject, QEvent, QRegularExpression, Signal
from PySide6.QtGui import QMouseEvent, QRegularExpressionValidator, QIcon, QWheelEvent

from src.roi_handler import ROIHandler, ROIState
from src.socket_handler import SocketHandler
from src.stream_receiver import StreamReceiver, StreamSize
from src.viewer import Viewer
from src.tools import numpy_to_pixmap, scale_pixmap, DebugEmitter
from src.command import Command
from src.zeroconf_handler import ZeroconfHandler
from src.widgets_text import *
from src.pipeline import WrapperPipeline
from src.data import Data

import cv2

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py

from ui_form import Ui_Widget

PARAMS_FILE_NAME = "params"
SAVE_TIMEOUT = 5


class Widget(QWidget):

    load_start_state_signal = Signal()
    toggle_view_signal = Signal()
    stream_size_changed_signal = Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.send_cfs_push_button.setEnabled(True) # fix

        validator = QRegularExpressionValidator(QRegularExpression(r"[0-9]+"))
        self.ui.skip_frame_line_edit.setValidator(validator)
        self.ui.line_edit_c1.setValidator(validator)
        self.ui.line_edit_c2.setValidator(validator)
        self.ui.line_edit_c3.setValidator(validator)
        self.ui.bitrate_line_edit.setValidator(validator)
        self.ui.roi_width_line_edit.setValidator(validator)
        self.ui.roi_height_line_edit.setValidator(validator)
        self.ui.training_count_line_edit.setValidator(validator)
        self.ui.stream_fps_line_edit.setValidator(validator)
        self.ui.frame_upper_border_line_edit.setValidator(validator)
        self.ui.frame_lower_border_line_edit.setValidator(validator)
        self.ui.frame_left_border_line_edit.setValidator(validator)
        self.ui.frame_right_border_line_edit.setValidator(validator)

        validator = QRegularExpressionValidator(QRegularExpression(r"[+-]?([0-9]*[.])?[0-9]+"))
        self.ui.alpha_smoothing_line_edit.setValidator(validator)
        self.ui.max_corr_line_edit.setValidator(validator)
        self.ui.sigma_factor_line_edit.setValidator(validator)

        self.stream_receiver = StreamReceiver(self)

        self.viewer = Viewer(self, self.stream_receiver)
        self.viewer.frame_ready_signal.connect(self.update_view_label)
        self.viewer.frame_ready_signal.connect(self.update_roi_label)
        self.viewer.play_pressed_signal.connect(self.update_gui_on_play)
        self.viewer.play_pressed_signal.connect(self.start_stream)
        self.viewer.stop_pressed_signal.connect(self.update_gui_on_stop)
        self.viewer.stop_pressed_signal.connect(self.stop_stream)
        self.viewer.stop_pressed_signal.connect(self.ui.roi_label.clear)
        self.load_start_state_signal.connect(self.viewer.load_no_connection_view)
        self.toggle_view_signal.connect(self.viewer.toggle_view)

        self.roi_handler = ROIHandler(self, self.ui.view_label, self.ui.roi_label, 1/int(self.ui.stream_fps_line_edit.text()))
        self.roi_handler.roi_selected_signal.connect(self.enable_tracking)
        self.viewer.play_pressed_signal.connect(self.roi_handler.enable_roi_selecting)
        self.viewer.stop_pressed_signal.connect(self.roi_handler.disable_roi_selecting)
        self.stream_size_changed_signal.connect(self.roi_handler.set_stream_size)
        self.toggle_view_signal.connect(lambda: self.roi_handler.set_interpolation_step(1/int(self.ui.stream_fps_line_edit.text())))

        self.view_label_pipeline = WrapperPipeline()
        self.view_label_pipeline.register_operation(self.draw_crosshair, self.draw_crosshair.__name__)
        self.view_label_pipeline.register_operation(self.roi_handler.draw_roi, self.roi_handler.draw_roi.__name__)
        self.view_label_pipeline.register_operation(self.update_view_label, self.update_view_label.__name__)

        self.update_view_label = self.view_label_pipeline.process

        self.ui.toggle_crosshair_radio_button.toggled.connect(
            lambda enabled: self.view_label_pipeline.enable_operation(self.draw_crosshair.__name__) if enabled
            else self.view_label_pipeline.disable_operation(self.draw_crosshair.__name__))
        self.ui.toggle_roi_radio_button.toggled.connect(
            lambda enabled: self.view_label_pipeline.enable_operation(self.roi_handler.draw_roi.__name__) if enabled
            else self.view_label_pipeline.disable_operation(self.roi_handler.draw_roi.__name__))

        self.ui.toggle_server_roi_radio_button.toggled.connect(
            lambda enabled: self.socket_handler.send(Command.TOGGLE_ROI, True) if enabled
            else self.socket_handler.send(Command.TOGGLE_ROI, False))
        self.ui.toggle_server_crosshair_radio_button.toggled.connect(
            lambda enabled: self.socket_handler.send(Command.TOGGLE_CROSSHAIR, True) if enabled
            else self.socket_handler.send(Command.TOGGLE_CROSSHAIR, False))

        self.view_label_event_filter = MouseEventFilter(
            self.roi_handler.on_left_click_handle_roi,
            [self.roi_handler.on_right_click_cancel_roi, lambda pos: self.on_tracker_stop_button_clicked()],
            self.roi_handler.on_mouse_move_draw_roi)
        self.ui.view_label.installEventFilter(self.view_label_event_filter)
        self.key_press_event_filter = KeyPressFilter(
            self.roi_handler.on_key_pressed_try_send_roi,
            self.on_tracker_stop_button_clicked)
        self.installEventFilter(self.key_press_event_filter)

        self.socket_handler = SocketHandler(self)
        self.socket_handler.update_roi_signal.connect(self.on_roi_update)
        self.socket_handler.stop_tracking_signal.connect(self.roi_handler.try_reset_roi)
        self.socket_handler.stop_tracking_signal.connect(self.handle_ui_when_tracker_is_stopped)
        self.socket_handler.update_tracker_data_signal.connect(self.update_tracker_data)
        self.socket_handler.start_tracking_signal.connect(self.roi_handler.try_send_roi_to_server)

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
        self.stream_receiver.change_stream_size_with_index_signal.connect(lambda index: self.stream_size_changed_signal.emit(self.stream_receiver.get_stream_size()))

        self.ui.roi_width_slider.valueChanged.connect(self.handle_roi_width)
        self.ui.roi_height_slider.valueChanged.connect(self.handle_roi_height)
        self.ui.roi_width_line_edit.textChanged.connect(self.handle_roi_width)
        self.ui.roi_height_line_edit.textChanged.connect(self.handle_roi_height)

        self.ui.roi_frame_brightness_slider.valueChanged.connect(self.handle_roi_label_brightness)
        self.ui.roi_frame_contrast_slider.valueChanged.connect(self.handle_roi_label_contrast)

        self.ui.fast_roi_radio_button.toggled.connect(
            lambda enabled: self.roi_handler.handle_fast_roi(enabled, self.ui.roi_width_slider.value(), self.ui.roi_height_slider.value()))

        self.image_checkboxes = [self.ui.stream_check_box, self.ui.transmitter_check_box]
        self.ui.stream_check_box.stateChanged.connect(lambda state: self.handle_image_checkbox(self.ui.stream_check_box, state))
        self.ui.transmitter_check_box.stateChanged.connect(lambda state: self.handle_image_checkbox(self.ui.transmitter_check_box, state))

        self.ui.optimal_fast_roi_step_radio_button.toggled.connect(self.enable_fast_roi_parameters)

        self.is_tracking_stopped = False

        self.save_thread = None

        self.is_app_closing = False

        self.data = Data(self, __file__, is_parent=True)
        self.load_saved_parameters()


    def handle_image_checkbox(self, check_box, state):
        if check_box == self.ui.stream_check_box:
            if state == Qt.CheckState.Checked.value:
                self.ui.stream_quality_group_box.setEnabled(True)
        if check_box == self.ui.transmitter_check_box:
            if state == Qt.CheckState.Checked.value:
                self.ui.stream_quality_group_box.setEnabled(False)
                self.stream_receiver.change_stream_size_with_index(StreamSize.SIZE_480[0])


    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.roi_handler.current_state != ROIState.FAST_SELECTING:
            return
        direction = np.sign(event.angleDelta().y())
        new_size = (self.roi_handler.roi[2] + self.roi_handler.roi[3]) // 2 + direction

        if self.ui.optimal_fast_roi_step_radio_button.isChecked():
            new_size = self.roi_handler.get_optimal_roi_size(new_size, direction)
        self.handle_roi_width(new_size)
        self.handle_roi_height(new_size)


    def update_tracker_data(self, data) -> None:
        plain_text = ''
        for key in data:
            plain_text += f"{key.capitalize().replace('_', ' ')}: {data[key]}\n\n"
        self.ui.tracker_data_plain_text.setPlainText(plain_text)


    def on_service_added(self, params) -> None:
        self.ui.connection_label.setText(f"{CONNECTED_TO} {params['server_ip']}:{params['server_port']}")
        self.ui.toggle_button.setEnabled(True)
        self.ui.tracking_group_box.setEnabled(True)
        self.ui.reboot_server_button.setEnabled(True)
        self.ui.cancel_connection_button.setEnabled(False)
        self.socket_handler.connect(params["server_ip"], params["server_port"])
        self.roi_handler.set_tracking_frame_size(params["tracking_frame_size"])
        self.viewer.set_tracking_frame_size(params["tracking_frame_size"])
        if self.ui.fast_roi_radio_button.isChecked():
            self.roi_handler.change_state(ROIState.FAST_SELECTING)
        self.socket_handler.send(Command.TOGGLE_ROI, self.ui.toggle_server_roi_radio_button.isChecked())
        self.socket_handler.send(Command.TOGGLE_CROSSHAIR, self.ui.toggle_server_crosshair_radio_button.isChecked())
        self.socket_handler.send(Command.CHANGE_FRAME_BORDERS, self.get_frame_borders_data())
        self.toggle_view_signal.emit()


    def on_roi_update(self, roi) -> None:
        if self.is_tracking_stopped:
            return
        self.roi_handler.update_roi(roi)
        if not self.ui.tracker_stop_button.isEnabled():
            self.ui.tracker_stop_button.setEnabled(True)


    def handle_roi_width(self, width: str | int) -> None:
        if width is None or width == '':
            return
        if isinstance(width, str):
            width = int(width)
        if width < self.ui.roi_width_slider.minimum():
            return
        width = min(width, self.ui.roi_height_slider.maximum())
        self.ui.roi_width_line_edit.setText(str(width))
        self.ui.roi_width_slider.setValue(width)
        if self.ui.fast_roi_radio_button.isChecked():
            self.roi_handler.handle_fast_roi(True, width, self.ui.roi_height_slider.value())


    def handle_roi_height(self, height) -> None:
        if height is None or height == '':
            return
        if isinstance(height, str):
            height = int(height)
        if height < self.ui.roi_height_slider.minimum():
            return
        height = min(height, self.ui.roi_height_slider.maximum())
        self.ui.roi_height_line_edit.setText(str(height))
        self.ui.roi_height_slider.setValue(height)
        if self.ui.fast_roi_radio_button.isChecked():
            self.roi_handler.handle_fast_roi(True, self.ui.roi_width_slider.value(), height)


    def enable_fast_roi_parameters(self, enabled):
        self.ui.roi_width_line_edit.setEnabled(not enabled)
        self.ui.roi_width_slider.setEnabled(not enabled)
        self.ui.roi_height_line_edit.setEnabled(not enabled)
        self.ui.roi_height_slider.setEnabled(not enabled)



    def handle_roi_label_brightness(self, value):
        maximum_brightness = self.ui.roi_frame_brightness_slider.maximum()
        brightness = int((1 + value / maximum_brightness) * 100)
        self.ui.roi_brightness_label.setText(f"{ROI_BRIGHTNESS_LABEL} {str(brightness)}%")


    def handle_roi_label_contrast(self, value):
        maximum_contrast = self.ui.roi_frame_contrast_slider.maximum()
        contrast = int((1 + value / maximum_contrast  - 0.5) * 100)
        self.ui.roi_contrast_label.setText(f"{ROI_CONTRAST_LABEL} {str(contrast)}%")


    def enable_tracking(self, roi) -> None:
        if not self.viewer.is_playing:
            return
        self.is_tracking_stopped = False
        data = {
            "roi": roi,
            "kalman": self.ui.kalman_radio_button.isChecked(),
            "skip_frames": int(self.ui.skip_frame_line_edit.text()),
            "stream_size": self.stream_receiver.get_stream_size(),
            "training_images_count": int(self.ui.training_count_line_edit.text()),
            "alpha_smoothing": float(self.ui.alpha_smoothing_line_edit.text()),
            "max_corr": float(self.ui.max_corr_line_edit.text()),
            "sigma_factor": float(self.ui.sigma_factor_line_edit.text())
        }
        self.socket_handler.send(Command.UPDATE_TRACKING, data)
        self.ui.tracker_params_group_box.setEnabled(False)
        self.ui.tracker_stop_button.setEnabled(True)
        self.ui.kalman_group_box.setEnabled(False)
        self.ui.fast_roi_group_box.setEnabled(False)


    def start_stream(self) -> None:
        if self.ui.stream_check_box.isChecked():
            stream_size = self.stream_receiver.get_stream_size()
            data = {
                "stream_size": stream_size,
                "bitrate": int(self.ui.bitrate_line_edit.text()),
                "frame_rate": int(self.ui.stream_fps_line_edit.text())
            }
            self.socket_handler.send(Command.START_STREAM, data)
        if self.ui.transmitter_check_box.isChecked():
            data = {
                "frame_rate": int(self.ui.stream_fps_line_edit.text())
            }
            self.socket_handler.send(Command.START_TRANSMISSION, data)
        if self.ui.fast_roi_radio_button.isChecked():
            self.roi_handler.handle_fast_roi(True, self.ui.roi_width_slider.value(), self.ui.roi_height_slider.value(), True)


    def stop_stream(self) -> None:
        if self.ui.stream_check_box.isChecked():
            self.socket_handler.send(Command.STOP_STREAM)
        if self.ui.transmitter_check_box.isChecked() and not self.is_app_closing:
            self.socket_handler.send(Command.STOP_TRANSMISSION)


    def update_view_label(self, frame: np.ndarray) -> None:
        pixmap = numpy_to_pixmap(frame)
        size = self.ui.view_label.size()
        scaled_pixmap = scale_pixmap(pixmap, size)
        self.ui.view_label.setPixmap(scaled_pixmap)


    def draw_crosshair(self, frame: np.ndarray)-> np.ndarray:
        stream_size = self.stream_receiver.get_stream_size()
        center_x = stream_size[0] // 2
        center_y = stream_size[1] // 2
        length = 8
        thickness = 2
        frame = frame.copy()
        cv2.line(frame, (center_x, center_y - length), (center_x, center_y + length), (0, 0, 255), thickness)
        cv2.line(frame, (center_x - length, center_y), (center_x + length, center_y), (0, 0, 255), thickness)
        return frame


    def draw_crosshair_wrapper(self, func):
        def wrapper(*args, **kwargs):
            args = list(args)
            if isinstance(args[0], np.ndarray):
                args[0] = self.draw_crosshair(args[0])
            return func(*args, **kwargs)
        return wrapper


    def update_roi_label(self, frame: np.ndarray) -> None:
        state = self.roi_handler.current_state
        if state != ROIState.FAST_SELECTING and state != ROIState.TRACKING:
            self.ui.roi_label.clear()
            return
        x, y = self.roi_handler.roi[0], self.roi_handler.roi[1]
        w, h = self.roi_handler.roi[2], self.roi_handler.roi[3]
        current_brightness_value = self.ui.roi_frame_brightness_slider.value()
        maximum_brightness = self.ui.roi_frame_brightness_slider.maximum()
        brightness = current_brightness_value / maximum_brightness

        current_contrast_value = self.ui.roi_frame_contrast_slider.value()
        maximum_contrast = self.ui.roi_frame_contrast_slider.maximum()
        contrast = 1 + current_contrast_value / maximum_contrast  - 0.5

        template = np.array(frame[y:y+h, x:x+w, :], order='C')
        if template.shape != (h, w, 3) and state != ROIState.TRACKING :
            self.roi_handler.reset_fast_roi()
            return
        template = contrast * (template.astype(np.float32) / 255.0) + brightness
        template = np.clip(template * 255.0, 0, 255).astype(np.uint8)
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
            },
            "fast_roi_group_box": {
                "enabled": self.ui.fast_roi_group_box.isEnabled()
            },
            "cancel_connection_button": {
                "enabled": self.ui.cancel_connection_button.isEnabled()
            },
            "tracker_stop_button": {
                "enabled": self.ui.tracker_stop_button.isEnabled()
            },
            "tracker_params_group_box": {
                "enabled": self.ui.tracker_params_group_box.isEnabled()
            }
        }


    def load_saved_parameters(self) -> None:
        saved_data = self.data.load_from_json(PARAMS_FILE_NAME)
        if saved_data is None:
            self.stream_receiver.set_default_stream_size()
            return

        try:
            self.ui.kalman_radio_button.setChecked(saved_data["kalman"])
            self.stream_receiver.change_stream_size_with_index(saved_data["stream_size_index"])
            self.ui.fast_roi_radio_button.setChecked(saved_data["fast_roi"])
            self.ui.roi_width_slider.setValue(saved_data["fast_roi_width"])
            self.ui.roi_height_slider.setValue(saved_data["fast_roi_height"])
            self.ui.roi_width_line_edit.setText(str(saved_data["fast_roi_width"]))
            self.ui.roi_height_line_edit.setText(str(saved_data["fast_roi_height"]))
            self.ui.toggle_roi_radio_button.setChecked(saved_data["toggle_roi"])
            self.ui.toggle_crosshair_radio_button.setChecked(saved_data["toggle_crosshair"])
            self.ui.toggle_server_roi_radio_button.setChecked(saved_data["server_toggle_roi"])
            self.ui.toggle_server_crosshair_radio_button.setChecked(saved_data["server_toggle_crosshair"])
            self.ui.optimal_fast_roi_step_radio_button.setChecked(saved_data["optimal_fast_roi_step"])
            self.ui.keep_frame_aspect_ratio_radio_button.setChecked(saved_data["keep_frame_aspect_ratio"])
        except KeyError:
            pass

        if "skip_frames" in saved_data:
            self.ui.skip_frame_line_edit.setText(str(saved_data["skip_frames"]))
        if "bitrate" in saved_data:
            self.ui.bitrate_line_edit.setText(str(saved_data["bitrate"]))
        if "training_count_line_edit" in saved_data:
            self.ui.training_count_line_edit.setText(str(saved_data["training_count_line_edit"]))
        if "alpha_smoothing_line_edit" in saved_data:
            self.ui.alpha_smoothing_line_edit.setText(str(saved_data["alpha_smoothing_line_edit"]))
        if "max_corr_line_edit" in saved_data:
            self.ui.max_corr_line_edit.setText(str(saved_data["max_corr_line_edit"]))
        if "sigma_factor_line_edit" in saved_data:
            self.ui.sigma_factor_line_edit.setText(str(saved_data["sigma_factor_line_edit"]))
        if "stream_fps_line_edit" in saved_data:
            self.ui.stream_fps_line_edit.setText(str(saved_data["stream_fps_line_edit"]))
        if "line_edit_c1" in saved_data:
            self.ui.line_edit_c1.setText(str(saved_data["line_edit_c1"]))
        if "line_edit_c2" in saved_data:
            self.ui.line_edit_c2.setText(str(saved_data["line_edit_c2"]))
        if "line_edit_c3" in saved_data:
            self.ui.line_edit_c3.setText(str(saved_data["line_edit_c3"]))
        if "roi_frame_brightness" in saved_data:
            self.ui.roi_frame_brightness_slider.setValue(int(saved_data["roi_frame_brightness"]))
        if "roi_frame_contrast" in saved_data:
            self.ui.roi_frame_contrast_slider.setValue(int(saved_data["roi_frame_contrast"]))
        if "image_check_box" in saved_data:
            for image_cb in self.image_checkboxes:
                if image_cb.objectName() == saved_data["image_check_box"]:
                    image_cb.setChecked(True)
                    break
        if "frame_upper_border" in saved_data:
            self.ui.frame_upper_border_line_edit.setText(str(saved_data["frame_upper_border"]))
        if "frame_lower_border" in saved_data:
            self.ui.frame_lower_border_line_edit.setText(str(saved_data["frame_lower_border"]))
        if "frame_left_border" in saved_data:
            self.ui.frame_left_border_line_edit.setText(str(saved_data["frame_left_border"]))
        if "frame_right_border" in saved_data:
            self.ui.frame_right_border_line_edit.setText(str(saved_data["frame_right_border"]))


    def save_parameters(self) -> None:
        params = {
            "kalman": self.ui.kalman_radio_button.isChecked(),
            "stream_size_index": self.stream_receiver.get_stream_size_index(),
            "fast_roi": self.ui.fast_roi_radio_button.isChecked(),
            "fast_roi_height": self.ui.roi_height_slider.value(),
            "fast_roi_width": self.ui.roi_width_slider.value(),
            "roi_frame_brightness": self.ui.roi_frame_brightness_slider.value(),
            "roi_frame_contrast": self.ui.roi_frame_contrast_slider.value(),
            "toggle_roi": self.ui.toggle_roi_radio_button.isChecked(),
            "toggle_crosshair": self.ui.toggle_crosshair_radio_button.isChecked(),
            "server_toggle_roi": self.ui.toggle_server_roi_radio_button.isChecked(),
            "server_toggle_crosshair": self.ui.toggle_server_crosshair_radio_button.isChecked(),
            "optimal_fast_roi_step": self.ui.optimal_fast_roi_step_radio_button.isChecked(),
            "keep_frame_aspect_ratio": self.ui.keep_frame_aspect_ratio_radio_button.isChecked(),
        }

        for image_cb in self.image_checkboxes:
            if image_cb.isChecked():
                params["image_check_box"] = image_cb.objectName()
                break

        if self.ui.skip_frame_line_edit.text() != '':
            params["skip_frames"] = int(self.ui.skip_frame_line_edit.text())
        if self.ui.bitrate_line_edit.text() != '':
            params["bitrate"] = int(self.ui.bitrate_line_edit.text())
        if self.ui.training_count_line_edit.text() != '':
            params["training_count_line_edit"] = int(self.ui.training_count_line_edit.text())
        if self.ui.alpha_smoothing_line_edit.text() != '':
            params["alpha_smoothing_line_edit"] = float(self.ui.alpha_smoothing_line_edit.text())
        if self.ui.max_corr_line_edit.text() != '':
            params["max_corr_line_edit"] = float(self.ui.max_corr_line_edit.text())
        if self.ui.sigma_factor_line_edit.text() != '':
            params["sigma_factor_line_edit"] = float(self.ui.sigma_factor_line_edit.text())
        if self.ui.stream_fps_line_edit.text() != '':
            params["stream_fps_line_edit"] = int(self.ui.stream_fps_line_edit.text())
        if self.ui.line_edit_c1.text() != '':
            params["line_edit_c1"] = int(self.ui.line_edit_c1.text())
        if self.ui.line_edit_c2.text() != '':
            params["line_edit_c2"] = int(self.ui.line_edit_c2.text())
        if self.ui.line_edit_c3.text() != '':
            params["line_edit_c3"] = int(self.ui.line_edit_c3.text())
        if self.ui.frame_upper_border_line_edit.text() != '':
            params["frame_upper_border"] = int(self.ui.frame_upper_border_line_edit.text())
        if self.ui.frame_lower_border_line_edit.text() != '':
            params["frame_lower_border"] = int(self.ui.frame_lower_border_line_edit.text())
        if self.ui.frame_left_border_line_edit.text() != '':
            params["frame_left_border"] = int(self.ui.frame_left_border_line_edit.text())
        if self.ui.frame_right_border_line_edit.text() != '':
            params["frame_right_border"] = int(self.ui.frame_right_border_line_edit.text())

        self.save_thread = threading.Thread(target=self._save_parameters, args=(params,))
        self.save_thread.start()


    def _save_parameters(self, params):
        self.data.save_to_json(PARAMS_FILE_NAME, params)


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


    def load_start_state(self) -> None:
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
        self.ui.fast_roi_group_box.setEnabled(self.start_state["fast_roi_group_box"]["enabled"])
        self.ui.cancel_connection_button.setEnabled(self.start_state["cancel_connection_button"]["enabled"])
        self.ui.tracker_stop_button.setEnabled(self.start_state["tracker_stop_button"]["enabled"])
        self.ui.tracker_params_group_box.setEnabled(self.start_state["tracker_params_group_box"]["enabled"])

    def get_frame_borders_data(self) -> dict:
        borders = {
            "top": int(self.ui.frame_upper_border_line_edit.text()),
            "bottom": int(self.ui.frame_lower_border_line_edit.text()),
            "left": int(self.ui.frame_left_border_line_edit.text()),
            "right": int(self.ui.frame_right_border_line_edit.text()),
            "keep_aspect_ratio" : self.ui.keep_frame_aspect_ratio_radio_button.isChecked()
        }
        return borders


    def on_disconnect_from_server(self) -> None:
        self.viewer.stop()
        self.zeroconf_handler.clear()
        self.roi_handler.try_reset_roi()
        self.socket_handler.disconnect()
        self.load_start_state_signal.emit()


    def closeEvent(self, e) -> None:
        self.is_app_closing = True
        self.save_parameters()
        self.viewer.stop()
        self.zeroconf_handler.clear()
        self.save_thread.join(timeout=SAVE_TIMEOUT)
        if self.save_thread and self.save_thread.is_alive():
            self.debug.send("Save thread did not finish in time. Data might be incomplete.")
            e.ignore()
        else:
            e.accept()


    def handle_ui_when_tracker_is_stopped(self) -> None:
        self.is_tracking_stopped = True
        self.ui.tracker_stop_button.setEnabled(False)
        self.ui.kalman_group_box.setEnabled(True)
        self.ui.fast_roi_group_box.setEnabled(True)
        self.ui.tracker_params_group_box.setEnabled(True)
        if self.ui.fast_roi_radio_button.isChecked():
            self.roi_handler.handle_fast_roi(True, self.ui.roi_width_slider.value(), self.ui.roi_height_slider.value(),True)


    @QtCore.Slot()
    def on_connect_button_clicked(self) -> None:
        self.zeroconf_handler.browse()
        self.ui.connection_label.setText(CONNECTION_AWATING)
        self.ui.connect_button.setEnabled(False)
        self.ui.cfs_group_box.setEnabled(True)
        self.ui.params_group_box.setEnabled(False)
        self.ui.cancel_connection_button.setEnabled(True)


    @QtCore.Slot()
    def on_cancel_connection_button_clicked(self) -> None:
        self.zeroconf_handler.clear()
        self.load_start_state_signal.emit()


    @QtCore.Slot()
    def on_toggle_button_clicked(self) -> None:
        self.toggle_view_signal.emit()


    @QtCore.Slot()
    def on_tracker_stop_button_clicked(self) -> None:
        if not self.ui.tracker_stop_button.isEnabled():
            return
        self.handle_ui_when_tracker_is_stopped()
        self.socket_handler.send(Command.STOP_TRACKING)


    @QtCore.Slot()
    def on_reboot_server_button_clicked(self) -> None:
        reply = QMessageBox.question(self, "Stream Receiver", RESTART_SERVER, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.socket_handler.send(Command.REBOOT_SERVER)
        self.socket_handler.disconnect()
        self.roi_handler.try_reset_roi()
        self.viewer.stop()
        self.zeroconf_handler.clear()
        self.load_start_state_signal.emit()


    @QtCore.Slot()
    def on_send_cfs_push_button_clicked(self) -> None:
        cf1 = int(self.ui.line_edit_c1.text())
        cf2 = int(self.ui.line_edit_c2.text())
        cf3 = int(self.ui.line_edit_c3.text())
        self.socket_handler.send(Command.SEND_CFS, [cf1, cf2, cf3])

    @QtCore.Slot()
    def on_change_frame_borders_push_button_clicked(self) -> None:
        borders = self.get_frame_borders_data()
        self.socket_handler.send(Command.CHANGE_FRAME_BORDERS, borders)


class MouseEventFilter(QObject):
    def __init__(self, callback_left_button=None, callbacks_right_button=None, callback_move=None):
        super().__init__()
        self.callback_left_button = callback_left_button
        self.callbacks_right_button = callbacks_right_button
        self.callback_move = callback_move


    def eventFilter(self, obj, event) -> bool:
        if type(event) is QMouseEvent:
            if event.button() == Qt.LeftButton:
                if self.callback_left_button is not None:
                    self.callback_left_button(event.position())
            elif event.button() == Qt.RightButton and event.type() == QEvent.MouseButtonPress:
                if self.callbacks_right_button is not None:
                    for cb in self.callbacks_right_button:
                        cb(event.position())
            else:
                if self.callback_move is not None:
                    self.callback_move(event.position())
            return True
        return super().eventFilter(obj, event)


class KeyPressFilter(QObject):
    def __init__(self, callback_return_key=None, callback_escape_key=None):
        super().__init__()
        self.callback_return_key = callback_return_key
        self.callback_escape_key = callback_escape_key

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key.Key_Return and self.callback_return_key:
                self.callback_return_key()
            if event.key() == Qt.Key.Key_Escape and self.callback_escape_key:
                self.callback_escape_key()
            return True
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app_icon = QIcon()
    app_icon.addFile('gui/icons/16x16.png', QtCore.QSize(16, 16))
    app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24, 24))
    app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32, 32))
    app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48, 48))
    app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
