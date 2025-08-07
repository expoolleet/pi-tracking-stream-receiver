# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1129, 800)
        Widget.setMinimumSize(QSize(1000, 800))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        Widget.setWindowOpacity(1.000000000000000)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
#if QT_CONFIG(tooltip)
        self.groupBox_4.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(u"")
        self.groupBox_4.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(185, 0))
        self.groupBox_3.setMaximumSize(QSize(185, 16777215))
        self.groupBox_3.setFlat(True)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tracker_data_plain_text = QPlainTextEdit(self.groupBox_3)
        self.tracker_data_plain_text.setObjectName(u"tracker_data_plain_text")
        self.tracker_data_plain_text.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.tracker_data_plain_text.setFont(font)
        self.tracker_data_plain_text.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.tracker_data_plain_text.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.tracker_data_plain_text)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.view_label = QLabel(self.groupBox_4)
        self.view_label.setObjectName(u"view_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_label.sizePolicy().hasHeightForWidth())
        self.view_label.setSizePolicy(sizePolicy)
        self.view_label.setMinimumSize(QSize(0, 0))
        self.view_label.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.view_label.setMouseTracking(True)
#if QT_CONFIG(tooltip)
        self.view_label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.view_label.setAutoFillBackground(False)
        self.view_label.setFrameShape(QFrame.Shape.Panel)
        self.view_label.setLineWidth(0)
        self.view_label.setTextFormat(Qt.TextFormat.PlainText)
        self.view_label.setScaledContents(False)
        self.view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.view_label)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setMinimumSize(QSize(350, 0))
        self.groupBox_7.setMaximumSize(QSize(500, 500))
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.roi_label = QLabel(self.groupBox_7)
        self.roi_label.setObjectName(u"roi_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.roi_label.sizePolicy().hasHeightForWidth())
        self.roi_label.setSizePolicy(sizePolicy2)
        self.roi_label.setMinimumSize(QSize(350, 0))
        self.roi_label.setMaximumSize(QSize(500, 500))
        self.roi_label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
#if QT_CONFIG(tooltip)
        self.roi_label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.roi_label.setFrameShape(QFrame.Shape.Panel)
        self.roi_label.setLineWidth(1)
        self.roi_label.setScaledContents(False)
        self.roi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.roi_label)

        self.roi_brightness_label = QLabel(self.groupBox_7)
        self.roi_brightness_label.setObjectName(u"roi_brightness_label")
        self.roi_brightness_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_14.addWidget(self.roi_brightness_label)

        self.roi_frame_brightness_slider = QSlider(self.groupBox_7)
        self.roi_frame_brightness_slider.setObjectName(u"roi_frame_brightness_slider")
        self.roi_frame_brightness_slider.setMaximumSize(QSize(16777215, 15))
        self.roi_frame_brightness_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roi_frame_brightness_slider.setMinimum(-100)
        self.roi_frame_brightness_slider.setMaximum(100)
        self.roi_frame_brightness_slider.setSingleStep(1)
        self.roi_frame_brightness_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.roi_frame_brightness_slider)

        self.roi_contrast_label = QLabel(self.groupBox_7)
        self.roi_contrast_label.setObjectName(u"roi_contrast_label")
        self.roi_contrast_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_14.addWidget(self.roi_contrast_label)

        self.roi_frame_contrast_slider = QSlider(self.groupBox_7)
        self.roi_frame_contrast_slider.setObjectName(u"roi_frame_contrast_slider")
        self.roi_frame_contrast_slider.setMaximumSize(QSize(16777215, 15))
        self.roi_frame_contrast_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roi_frame_contrast_slider.setMinimum(0)
        self.roi_frame_contrast_slider.setMaximum(100)
        self.roi_frame_contrast_slider.setPageStep(50)
        self.roi_frame_contrast_slider.setValue(50)
        self.roi_frame_contrast_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.roi_frame_contrast_slider)


        self.horizontalLayout.addWidget(self.groupBox_7)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.connection_label = QLabel(Widget)
        self.connection_label.setObjectName(u"connection_label")
        sizePolicy2.setHeightForWidth(self.connection_label.sizePolicy().hasHeightForWidth())
        self.connection_label.setSizePolicy(sizePolicy2)
        self.connection_label.setMinimumSize(QSize(0, 0))
        self.connection_label.setMaximumSize(QSize(16777215, 20))
        self.connection_label.setFont(font)

        self.verticalLayout_2.addWidget(self.connection_label)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 300))
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.controlsBox = QGroupBox(self.groupBox_2)
        self.controlsBox.setObjectName(u"controlsBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.controlsBox.sizePolicy().hasHeightForWidth())
        self.controlsBox.setSizePolicy(sizePolicy3)
        self.controlsBox.setMinimumSize(QSize(0, 240))
        self.controlsBox.setMaximumSize(QSize(170, 16777215))
        self.controlsBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.controlsBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.connect_button = QPushButton(self.controlsBox)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setEnabled(True)
        self.connect_button.setMinimumSize(QSize(0, 40))
        self.connect_button.setMaximumSize(QSize(16777215, 16777215))
        self.connect_button.setFont(font)
        self.connect_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.connect_button)

        self.cancel_connection_button = QPushButton(self.controlsBox)
        self.cancel_connection_button.setObjectName(u"cancel_connection_button")
        self.cancel_connection_button.setEnabled(False)

        self.verticalLayout.addWidget(self.cancel_connection_button)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toggle_button = QPushButton(self.controlsBox)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setEnabled(False)
        self.toggle_button.setMinimumSize(QSize(0, 40))
        self.toggle_button.setFont(font)
        self.toggle_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.toggle_button)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.reboot_server_button = QPushButton(self.controlsBox)
        self.reboot_server_button.setObjectName(u"reboot_server_button")
        self.reboot_server_button.setEnabled(False)
        self.reboot_server_button.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.reboot_server_button.setFont(font1)
        self.reboot_server_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.reboot_server_button)


        self.horizontalLayout_4.addWidget(self.controlsBox)

        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setMinimumSize(QSize(0, 280))
        self.tabWidget.setMaximumSize(QSize(435, 16777215))
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tracking_group_box = QGroupBox(self.tab)
        self.tracking_group_box.setObjectName(u"tracking_group_box")
        self.tracking_group_box.setEnabled(True)
        self.tracking_group_box.setMaximumSize(QSize(16777215, 16777215))
        self.tracking_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tracking_group_box.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.tracking_group_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tracker_params_group_box = QGroupBox(self.tracking_group_box)
        self.tracker_params_group_box.setObjectName(u"tracker_params_group_box")
        self.tracker_params_group_box.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.tracker_params_group_box)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.label_6 = QLabel(self.tracker_params_group_box)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_6.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_6)

        self.training_count_line_edit = QLineEdit(self.tracker_params_group_box)
        self.training_count_line_edit.setObjectName(u"training_count_line_edit")
        self.training_count_line_edit.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(9)
        self.training_count_line_edit.setFont(font3)
        self.training_count_line_edit.setMaxLength(2)
        self.training_count_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.training_count_line_edit)

        self.label_7 = QLabel(self.tracker_params_group_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_7)

        self.alpha_smoothing_line_edit = QLineEdit(self.tracker_params_group_box)
        self.alpha_smoothing_line_edit.setObjectName(u"alpha_smoothing_line_edit")
        self.alpha_smoothing_line_edit.setEnabled(True)
        self.alpha_smoothing_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.alpha_smoothing_line_edit.setFont(font3)
        self.alpha_smoothing_line_edit.setMaxLength(5)
        self.alpha_smoothing_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.alpha_smoothing_line_edit)

        self.label_8 = QLabel(self.tracker_params_group_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_8)

        self.max_corr_line_edit = QLineEdit(self.tracker_params_group_box)
        self.max_corr_line_edit.setObjectName(u"max_corr_line_edit")
        self.max_corr_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.max_corr_line_edit.setFont(font3)
        self.max_corr_line_edit.setMaxLength(5)
        self.max_corr_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.max_corr_line_edit)

        self.label_9 = QLabel(self.tracker_params_group_box)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.sigma_factor_line_edit = QLineEdit(self.tracker_params_group_box)
        self.sigma_factor_line_edit.setObjectName(u"sigma_factor_line_edit")
        self.sigma_factor_line_edit.setMaxLength(5)
        self.sigma_factor_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.sigma_factor_line_edit)


        self.horizontalLayout_2.addWidget(self.tracker_params_group_box)

        self.kalman_group_box = QGroupBox(self.tracking_group_box)
        self.kalman_group_box.setObjectName(u"kalman_group_box")
        self.kalman_group_box.setMaximumSize(QSize(95, 16777215))
        self.kalman_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.kalman_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, -1, 24)
        self.kalman_radio_button = QRadioButton(self.kalman_group_box)
        self.kalman_radio_button.setObjectName(u"kalman_radio_button")
        self.kalman_radio_button.setFont(font1)
        self.kalman_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.kalman_radio_button)

        self.label = QLabel(self.kalman_group_box)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font2)

        self.verticalLayout_4.addWidget(self.label)

        self.skip_frame_line_edit = QLineEdit(self.kalman_group_box)
        self.skip_frame_line_edit.setObjectName(u"skip_frame_line_edit")
        self.skip_frame_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.skip_frame_line_edit.setFont(font)
        self.skip_frame_line_edit.setInputMask(u"")
        self.skip_frame_line_edit.setMaxLength(2)
        self.skip_frame_line_edit.setFrame(True)
        self.skip_frame_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.skip_frame_line_edit)


        self.horizontalLayout_2.addWidget(self.kalman_group_box)

        self.fast_roi_group_box = QGroupBox(self.tracking_group_box)
        self.fast_roi_group_box.setObjectName(u"fast_roi_group_box")
        self.fast_roi_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.fast_roi_group_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 2, -1, 2)
        self.fast_roi_radio_button = QRadioButton(self.fast_roi_group_box)
        self.fast_roi_radio_button.setObjectName(u"fast_roi_radio_button")
        self.fast_roi_radio_button.setFont(font1)
        self.fast_roi_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fast_roi_radio_button.setChecked(True)
        self.fast_roi_radio_button.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.fast_roi_radio_button)

        self.optimal_fast_roi_step_radio_button = QRadioButton(self.fast_roi_group_box)
        self.optimal_fast_roi_step_radio_button.setObjectName(u"optimal_fast_roi_step_radio_button")
        self.optimal_fast_roi_step_radio_button.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.optimal_fast_roi_step_radio_button)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.roi_width_label = QLabel(self.fast_roi_group_box)
        self.roi_width_label.setObjectName(u"roi_width_label")
        self.roi_width_label.setFont(font1)
        self.roi_width_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.roi_width_label)

        self.roi_width_line_edit = QLineEdit(self.fast_roi_group_box)
        self.roi_width_line_edit.setObjectName(u"roi_width_line_edit")
        self.roi_width_line_edit.setMinimumSize(QSize(0, 0))
        self.roi_width_line_edit.setMaximumSize(QSize(50, 16777215))
        self.roi_width_line_edit.setFont(font)
        self.roi_width_line_edit.setMaxLength(3)

        self.horizontalLayout_5.addWidget(self.roi_width_line_edit)

        self.label_4 = QLabel(self.fast_roi_group_box)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.roi_width_slider = QSlider(self.fast_roi_group_box)
        self.roi_width_slider.setObjectName(u"roi_width_slider")
        self.roi_width_slider.setEnabled(True)
        self.roi_width_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roi_width_slider.setMinimum(32)
        self.roi_width_slider.setMaximum(256)
        self.roi_width_slider.setValue(64)
        self.roi_width_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.roi_width_slider)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.roi_height_label = QLabel(self.fast_roi_group_box)
        self.roi_height_label.setObjectName(u"roi_height_label")
        self.roi_height_label.setFont(font1)
        self.roi_height_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.roi_height_label)

        self.roi_height_line_edit = QLineEdit(self.fast_roi_group_box)
        self.roi_height_line_edit.setObjectName(u"roi_height_line_edit")
        self.roi_height_line_edit.setMaximumSize(QSize(50, 16777215))
        self.roi_height_line_edit.setFont(font)
        self.roi_height_line_edit.setMaxLength(3)

        self.horizontalLayout_6.addWidget(self.roi_height_line_edit)

        self.label_5 = QLabel(self.fast_roi_group_box)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.roi_height_slider = QSlider(self.fast_roi_group_box)
        self.roi_height_slider.setObjectName(u"roi_height_slider")
        self.roi_height_slider.setEnabled(True)
        self.roi_height_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roi_height_slider.setMinimum(32)
        self.roi_height_slider.setMaximum(256)
        self.roi_height_slider.setValue(64)
        self.roi_height_slider.setSliderPosition(64)
        self.roi_height_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.roi_height_slider)


        self.horizontalLayout_2.addWidget(self.fast_roi_group_box)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tracker_stop_button = QPushButton(self.tracking_group_box)
        self.tracker_stop_button.setObjectName(u"tracker_stop_button")
        self.tracker_stop_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.tracker_stop_button.sizePolicy().hasHeightForWidth())
        self.tracker_stop_button.setSizePolicy(sizePolicy3)
        self.tracker_stop_button.setMaximumSize(QSize(16777215, 30))
        self.tracker_stop_button.setFont(font)
        self.tracker_stop_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tracker_stop_button.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.tracker_stop_button.setFlat(False)

        self.horizontalLayout_9.addWidget(self.tracker_stop_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_3.addWidget(self.tracking_group_box)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_9 = QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.params_group_box = QGroupBox(self.tab_5)
        self.params_group_box.setObjectName(u"params_group_box")
        self.params_group_box.setFlat(True)
        self.horizontalLayout_7 = QHBoxLayout(self.params_group_box)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stream_quality_group_box = QGroupBox(self.params_group_box)
        self.stream_quality_group_box.setObjectName(u"stream_quality_group_box")
        self.verticalLayout_13 = QVBoxLayout(self.stream_quality_group_box)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_2 = QLabel(self.stream_quality_group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))
        self.label_2.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_2)

        self.stream_size_combo_box = QComboBox(self.stream_quality_group_box)
        self.stream_size_combo_box.setObjectName(u"stream_size_combo_box")
        self.stream_size_combo_box.setFont(font)
        self.stream_size_combo_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.stream_size_combo_box)

        self.label_3 = QLabel(self.stream_quality_group_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_3)

        self.bitrate_line_edit = QLineEdit(self.stream_quality_group_box)
        self.bitrate_line_edit.setObjectName(u"bitrate_line_edit")
        self.bitrate_line_edit.setFont(font)
        self.bitrate_line_edit.setMaxLength(4)
        self.bitrate_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.bitrate_line_edit)


        self.horizontalLayout_7.addWidget(self.stream_quality_group_box)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.groupBox_6 = QGroupBox(self.params_group_box)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.groupBox_6.setFlat(False)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_10)

        self.stream_fps_line_edit = QLineEdit(self.groupBox_6)
        self.stream_fps_line_edit.setObjectName(u"stream_fps_line_edit")
        self.stream_fps_line_edit.setFont(font)
        self.stream_fps_line_edit.setMaxLength(2)
        self.stream_fps_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.stream_fps_line_edit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy5)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stream_check_box = QCheckBox(self.groupBox_8)
        self.stream_check_box.setObjectName(u"stream_check_box")
        self.stream_check_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stream_check_box.setChecked(True)
        self.stream_check_box.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.stream_check_box)

        self.transmitter_check_box = QCheckBox(self.groupBox_8)
        self.transmitter_check_box.setObjectName(u"transmitter_check_box")
        self.transmitter_check_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.transmitter_check_box.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.transmitter_check_box)


        self.verticalLayout_10.addWidget(self.groupBox_8)


        self.horizontalLayout_7.addWidget(self.groupBox_6)


        self.verticalLayout_9.addWidget(self.params_group_box)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, -1, -1, -1)
        self.toggle_roi_radio_button = QRadioButton(self.groupBox_5)
        self.toggle_roi_radio_button.setObjectName(u"toggle_roi_radio_button")
        self.toggle_roi_radio_button.setFont(font1)
        self.toggle_roi_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggle_roi_radio_button.setCheckable(True)
        self.toggle_roi_radio_button.setChecked(True)
        self.toggle_roi_radio_button.setAutoExclusive(False)

        self.verticalLayout_16.addWidget(self.toggle_roi_radio_button)

        self.toggle_server_roi_radio_button = QRadioButton(self.groupBox_5)
        self.toggle_server_roi_radio_button.setObjectName(u"toggle_server_roi_radio_button")
        self.toggle_server_roi_radio_button.setFont(font1)
        self.toggle_server_roi_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggle_server_roi_radio_button.setAutoExclusive(False)

        self.verticalLayout_16.addWidget(self.toggle_server_roi_radio_button)

        self.toggle_crosshair_radio_button = QRadioButton(self.groupBox_5)
        self.toggle_crosshair_radio_button.setObjectName(u"toggle_crosshair_radio_button")
        self.toggle_crosshair_radio_button.setFont(font1)
        self.toggle_crosshair_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggle_crosshair_radio_button.setCheckable(True)
        self.toggle_crosshair_radio_button.setChecked(True)
        self.toggle_crosshair_radio_button.setAutoExclusive(False)

        self.verticalLayout_16.addWidget(self.toggle_crosshair_radio_button)

        self.toggle_server_crosshair_radio_button = QRadioButton(self.groupBox_5)
        self.toggle_server_crosshair_radio_button.setObjectName(u"toggle_server_crosshair_radio_button")
        self.toggle_server_crosshair_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggle_server_crosshair_radio_button.setAutoExclusive(False)

        self.verticalLayout_16.addWidget(self.toggle_server_crosshair_radio_button)


        self.horizontalLayout_12.addWidget(self.groupBox_5)

        self.groupBox_9 = QGroupBox(self.tab_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.keep_frame_aspect_ratio_radio_button = QRadioButton(self.groupBox_9)
        self.keep_frame_aspect_ratio_radio_button.setObjectName(u"keep_frame_aspect_ratio_radio_button")
        self.keep_frame_aspect_ratio_radio_button.setFont(font3)
        self.keep_frame_aspect_ratio_radio_button.setAcceptDrops(False)

        self.verticalLayout_21.addWidget(self.keep_frame_aspect_ratio_radio_button)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_14)

        self.frame_upper_border_line_edit = QLineEdit(self.groupBox_9)
        self.frame_upper_border_line_edit.setObjectName(u"frame_upper_border_line_edit")
        self.frame_upper_border_line_edit.setFont(font3)
        self.frame_upper_border_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.frame_upper_border_line_edit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_13)

        self.frame_lower_border_line_edit = QLineEdit(self.groupBox_9)
        self.frame_lower_border_line_edit.setObjectName(u"frame_lower_border_line_edit")
        self.frame_lower_border_line_edit.setFont(font3)
        self.frame_lower_border_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.frame_lower_border_line_edit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_11)

        self.frame_right_border_line_edit = QLineEdit(self.groupBox_9)
        self.frame_right_border_line_edit.setObjectName(u"frame_right_border_line_edit")
        self.frame_right_border_line_edit.setFont(font3)
        self.frame_right_border_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.frame_right_border_line_edit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_12)

        self.frame_left_border_line_edit = QLineEdit(self.groupBox_9)
        self.frame_left_border_line_edit.setObjectName(u"frame_left_border_line_edit")
        self.frame_left_border_line_edit.setFont(font3)
        self.frame_left_border_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.frame_left_border_line_edit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)


        self.verticalLayout_21.addLayout(self.horizontalLayout_11)

        self.change_frame_borders_push_button = QPushButton(self.groupBox_9)
        self.change_frame_borders_push_button.setObjectName(u"change_frame_borders_push_button")

        self.verticalLayout_21.addWidget(self.change_frame_borders_push_button)


        self.horizontalLayout_12.addWidget(self.groupBox_9)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cfs_group_box = QGroupBox(self.tab_2)
        self.cfs_group_box.setObjectName(u"cfs_group_box")
        self.cfs_group_box.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cfs_group_box.sizePolicy().hasHeightForWidth())
        self.cfs_group_box.setSizePolicy(sizePolicy2)
        self.cfs_group_box.setMaximumSize(QSize(400, 16777215))
        self.cfs_group_box.setTitle(u"")
        self.cfs_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cfs_group_box.setFlat(False)
        self.horizontalLayout_8 = QHBoxLayout(self.cfs_group_box)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.line_edit_c1 = QLineEdit(self.cfs_group_box)
        self.line_edit_c1.setObjectName(u"line_edit_c1")
        self.line_edit_c1.setMaximumSize(QSize(250, 16777215))
        self.line_edit_c1.setFont(font)
        self.line_edit_c1.setMaxLength(4)
        self.line_edit_c1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c1)

        self.line_edit_c2 = QLineEdit(self.cfs_group_box)
        self.line_edit_c2.setObjectName(u"line_edit_c2")
        self.line_edit_c2.setMaximumSize(QSize(250, 16777215))
        self.line_edit_c2.setFont(font)
        self.line_edit_c2.setMaxLength(4)
        self.line_edit_c2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c2)

        self.line_edit_c3 = QLineEdit(self.cfs_group_box)
        self.line_edit_c3.setObjectName(u"line_edit_c3")
        self.line_edit_c3.setMaximumSize(QSize(250, 16777215))
        self.line_edit_c3.setFont(font)
        self.line_edit_c3.setMaxLength(4)
        self.line_edit_c3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c3)

        self.send_cfs_push_button = QPushButton(self.cfs_group_box)
        self.send_cfs_push_button.setObjectName(u"send_cfs_push_button")
        self.send_cfs_push_button.setEnabled(False)
        self.send_cfs_push_button.setMaximumSize(QSize(250, 16777215))
        self.send_cfs_push_button.setFont(font)
        self.send_cfs_push_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.send_cfs_push_button)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.cfs_group_box)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.debug_plain_text_edit = QPlainTextEdit(self.groupBox)
        self.debug_plain_text_edit.setObjectName(u"debug_plain_text_edit")
        self.debug_plain_text_edit.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.debug_plain_text_edit.setFont(font4)
        self.debug_plain_text_edit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.debug_plain_text_edit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.debug_plain_text_edit)


        self.horizontalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.stream_size_combo_box.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Stream Receiver", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.view_label.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("Widget", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0430", None))
        self.roi_label.setText("")
        self.roi_brightness_label.setText(QCoreApplication.translate("Widget", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c: 100%", None))
#if QT_CONFIG(tooltip)
        self.roi_frame_brightness_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.roi_frame_brightness_slider.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.roi_contrast_label.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u043d\u043e\u0441\u0442\u044c: 100%", None))
        self.connection_label.setText(QCoreApplication.translate("Widget", u"\u041d\u0435\u0442 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u043c", None))
        self.groupBox_2.setTitle("")
        self.controlsBox.setTitle(QCoreApplication.translate("Widget", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.connect_button.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.cancel_connection_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.toggle_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u0442\u043e\u043a", None))
        self.reboot_server_button.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.tracking_group_box.setTitle("")
        self.tracker_params_group_box.setTitle(QCoreApplication.translate("Widget", u"\u0422\u0440\u0435\u043a\u0435\u0440", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u0422\u0440\u0435\u043d\u0438\u0440. \u0438\u0437\u043e\u0431\u0440.", None))
        self.training_count_line_edit.setText(QCoreApplication.translate("Widget", u"9", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u041a\u0444. \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d.", None))
        self.alpha_smoothing_line_edit.setText(QCoreApplication.translate("Widget", u"0.7", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432. \u043a\u043e\u0440\u0440.", None))
        self.max_corr_line_edit.setText(QCoreApplication.translate("Widget", u"0.25", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u0424\u0430\u043a\u0442\u043e\u0440 \u0440. \u0446\u0435\u043b\u0438", None))
        self.sigma_factor_line_edit.setText(QCoreApplication.translate("Widget", u"0.05", None))
        self.kalman_group_box.setTitle(QCoreApplication.translate("Widget", u"\u041a\u0430\u043b\u043c\u0430\u043d", None))
        self.kalman_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f. \u043a\u0430\u0434\u0440\u043e\u0432:", None))
        self.skip_frame_line_edit.setText(QCoreApplication.translate("Widget", u"1", None))
        self.fast_roi_group_box.setTitle(QCoreApplication.translate("Widget", u"\u0411\u044b\u0441\u0442\u0440\u043e\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.fast_roi_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.optimal_fast_roi_step_radio_button.setText(QCoreApplication.translate("Widget", u"\u041e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0448\u0430\u0433", None))
        self.roi_width_label.setText(QCoreApplication.translate("Widget", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.roi_width_line_edit.setText(QCoreApplication.translate("Widget", u"64", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"px", None))
        self.roi_height_label.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.roi_height_line_edit.setText(QCoreApplication.translate("Widget", u"64", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"px", None))
        self.tracker_stop_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u041e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.params_group_box.setTitle("")
        self.stream_quality_group_box.setTitle(QCoreApplication.translate("Widget", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u0430\u043d\u0441\u043b\u044f\u0446\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u043e\u0442\u043e\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u0411\u0438\u0442\u0440\u0435\u0439\u0442 (\u043a\u0431\u0438\u0442/\u0441)", None))
        self.bitrate_line_edit.setText(QCoreApplication.translate("Widget", u"2000", None))
        self.bitrate_line_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0447\u0435\u0435", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"FPS", None))
        self.stream_fps_line_edit.setText(QCoreApplication.translate("Widget", u"30", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u043a\u0430\u0437 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.stream_check_box.setText(QCoreApplication.translate("Widget", u"\u0422\u0440\u0430\u043d\u0441\u043b\u044f\u0446\u0438\u044f", None))
        self.transmitter_check_box.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0442\u0447\u0438\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.groupBox_5.setTitle("")
        self.toggle_roi_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b. \u0440\u0430\u043c\u043a\u0443 ROI (\u043a\u043b\u0438\u0435\u043d\u0442)", None))
        self.toggle_server_roi_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b. \u0440\u0430\u043c\u043a\u0443 ROI (\u0441\u0435\u0440\u0432\u0435\u0440)", None))
        self.toggle_crosshair_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b. \u043f\u0440\u0438\u0446\u0435\u043b (\u0446\u0435\u043d\u0442\u0440) (\u043a\u043b\u0438\u0435\u043d\u0442) ", None))
        self.toggle_server_crosshair_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b. \u043f\u0440\u0438\u0446\u0435\u043b (\u0446\u0435\u043d\u0442\u0440) (\u0441\u0435\u0440\u0432\u0435\u0440)", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Widget", u"\u041e\u0442\u0441\u0442\u0443\u043f\u044b (\u043f\u0435\u0440\u0435\u0434\u0430\u0442\u0447\u0438\u043a)", None))
        self.keep_frame_aspect_ratio_radio_button.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440. \u0441\u043e\u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0441\u0442\u043e\u0440\u043e\u043d", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"\u0412\u0435\u0440\u0445", None))
        self.frame_upper_border_line_edit.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u041d\u0438\u0437", None))
        self.frame_lower_border_line_edit.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0430\u0432\u043e", None))
        self.frame_right_border_line_edit.setText(QCoreApplication.translate("Widget", u"0", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u041b\u0435\u0432\u043e", None))
        self.frame_left_border_line_edit.setText(QCoreApplication.translate("Widget", u"0", None))
        self.change_frame_borders_push_button.setText(QCoreApplication.translate("Widget", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.line_edit_c1.setPlaceholderText(QCoreApplication.translate("Widget", u"C1", None))
        self.line_edit_c2.setPlaceholderText(QCoreApplication.translate("Widget", u"C2", None))
        self.line_edit_c3.setPlaceholderText(QCoreApplication.translate("Widget", u"C3", None))
        self.send_cfs_push_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043e\u0442\u043b\u0430\u0434\u043a\u0438", None))
    # retranslateUi

