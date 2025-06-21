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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1093, 800)
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
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.roi_label = QLabel(self.groupBox_4)
        self.roi_label.setObjectName(u"roi_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.roi_label.sizePolicy().hasHeightForWidth())
        self.roi_label.setSizePolicy(sizePolicy1)
        self.roi_label.setMinimumSize(QSize(350, 0))
        self.roi_label.setMaximumSize(QSize(350, 350))
        self.roi_label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
#if QT_CONFIG(tooltip)
        self.roi_label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.roi_label.setFrameShape(QFrame.Shape.Panel)
        self.roi_label.setLineWidth(1)
        self.roi_label.setScaledContents(False)
        self.roi_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.roi_label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.connection_label = QLabel(Widget)
        self.connection_label.setObjectName(u"connection_label")
        sizePolicy1.setHeightForWidth(self.connection_label.sizePolicy().hasHeightForWidth())
        self.connection_label.setSizePolicy(sizePolicy1)
        self.connection_label.setMinimumSize(QSize(0, 0))
        self.connection_label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(11)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.controlsBox.sizePolicy().hasHeightForWidth())
        self.controlsBox.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMinimumSize(QSize(0, 280))
        self.tabWidget.setMaximumSize(QSize(420, 16777215))
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
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
        self.tracker_params_group_box.setMaximumSize(QSize(85, 16777215))
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
        self.training_count_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.training_count_line_edit)

        self.label_7 = QLabel(self.tracker_params_group_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_7)

        self.learning_rate_line_edit = QLineEdit(self.tracker_params_group_box)
        self.learning_rate_line_edit.setObjectName(u"learning_rate_line_edit")
        self.learning_rate_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.learning_rate_line_edit.setFont(font3)
        self.learning_rate_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.learning_rate_line_edit)

        self.label_8 = QLabel(self.tracker_params_group_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_8)

        self.max_corr_line_edit = QLineEdit(self.tracker_params_group_box)
        self.max_corr_line_edit.setObjectName(u"max_corr_line_edit")
        self.max_corr_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.max_corr_line_edit.setFont(font3)
        self.max_corr_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.max_corr_line_edit)

        self.label_9 = QLabel(self.tracker_params_group_box)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.sigma_factor_line_edit = QLineEdit(self.tracker_params_group_box)
        self.sigma_factor_line_edit.setObjectName(u"sigma_factor_line_edit")
        self.sigma_factor_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.sigma_factor_line_edit)


        self.horizontalLayout_2.addWidget(self.tracker_params_group_box)

        self.kalman_group_box = QGroupBox(self.tracking_group_box)
        self.kalman_group_box.setObjectName(u"kalman_group_box")
        self.kalman_group_box.setMaximumSize(QSize(100, 16777215))
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
        self.skip_frame_line_edit.setMaxLength(100)
        self.skip_frame_line_edit.setFrame(True)
        self.skip_frame_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.skip_frame_line_edit)


        self.horizontalLayout_2.addWidget(self.kalman_group_box)

        self.fast_roi_group_box = QGroupBox(self.tracking_group_box)
        self.fast_roi_group_box.setObjectName(u"fast_roi_group_box")
        self.fast_roi_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.fast_roi_group_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.fast_roi_radio_button = QRadioButton(self.fast_roi_group_box)
        self.fast_roi_radio_button.setObjectName(u"fast_roi_radio_button")
        self.fast_roi_radio_button.setFont(font1)
        self.fast_roi_radio_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.fast_roi_radio_button)

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
        self.roi_width_slider.setValue(128)
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
        self.roi_height_slider.setValue(128)
        self.roi_height_slider.setSliderPosition(128)
        self.roi_height_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.roi_height_slider)


        self.horizontalLayout_2.addWidget(self.fast_roi_group_box)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tracker_stop_button = QPushButton(self.tracking_group_box)
        self.tracker_stop_button.setObjectName(u"tracker_stop_button")
        self.tracker_stop_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.tracker_stop_button.sizePolicy().hasHeightForWidth())
        self.tracker_stop_button.setSizePolicy(sizePolicy2)
        self.tracker_stop_button.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setPointSize(12)
        self.tracker_stop_button.setFont(font4)
        self.tracker_stop_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tracker_stop_button.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.tracker_stop_button.setFlat(False)

        self.verticalLayout_5.addWidget(self.tracker_stop_button)


        self.horizontalLayout_3.addWidget(self.tracking_group_box)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_9 = QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.params_group_box = QGroupBox(self.tab_5)
        self.params_group_box.setObjectName(u"params_group_box")
        self.verticalLayout_10 = QVBoxLayout(self.params_group_box)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.params_group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_10.addWidget(self.label_2)

        self.stream_size_combo_box = QComboBox(self.params_group_box)
        self.stream_size_combo_box.setObjectName(u"stream_size_combo_box")
        self.stream_size_combo_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.stream_size_combo_box)

        self.label_3 = QLabel(self.params_group_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_10.addWidget(self.label_3)

        self.bitrate_line_edit = QLineEdit(self.params_group_box)
        self.bitrate_line_edit.setObjectName(u"bitrate_line_edit")
        self.bitrate_line_edit.setFont(font)
        self.bitrate_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.bitrate_line_edit)


        self.verticalLayout_9.addWidget(self.params_group_box)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cfs_group_box = QGroupBox(self.tab_2)
        self.cfs_group_box.setObjectName(u"cfs_group_box")
        self.cfs_group_box.setEnabled(False)
        self.cfs_group_box.setMaximumSize(QSize(400, 16777215))
        self.cfs_group_box.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.cfs_group_box.setFlat(False)
        self.verticalLayout_7 = QVBoxLayout(self.cfs_group_box)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.line_edit_c1 = QLineEdit(self.cfs_group_box)
        self.line_edit_c1.setObjectName(u"line_edit_c1")
        self.line_edit_c1.setFont(font)
        self.line_edit_c1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c1)

        self.line_edit_c2 = QLineEdit(self.cfs_group_box)
        self.line_edit_c2.setObjectName(u"line_edit_c2")
        self.line_edit_c2.setFont(font)
        self.line_edit_c2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c2)

        self.line_edit_c3 = QLineEdit(self.cfs_group_box)
        self.line_edit_c3.setObjectName(u"line_edit_c3")
        self.line_edit_c3.setFont(font)
        self.line_edit_c3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.line_edit_c3)

        self.send_cfs_push_button = QPushButton(self.cfs_group_box)
        self.send_cfs_push_button.setObjectName(u"send_cfs_push_button")
        self.send_cfs_push_button.setFont(font)
        self.send_cfs_push_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.send_cfs_push_button)


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
        self.debug_plain_text_edit.setFont(font4)
        self.debug_plain_text_edit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.debug_plain_text_edit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.debug_plain_text_edit)


        self.horizontalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Stream Receiver", None))
        self.view_label.setText("")
        self.roi_label.setText("")
        self.connection_label.setText(QCoreApplication.translate("Widget", u"\u041d\u0435\u0442 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u043c", None))
        self.groupBox_2.setTitle("")
        self.controlsBox.setTitle(QCoreApplication.translate("Widget", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.connect_button.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.cancel_connection_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.toggle_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u0442\u043e\u043a", None))
        self.reboot_server_button.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.tracking_group_box.setTitle("")
        self.tracker_params_group_box.setTitle(QCoreApplication.translate("Widget", u"\u0422\u0440\u0435\u043a\u0435\u0440", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u0422\u0440\u0435\u043d. \u0438\u0437\u043e.", None))
        self.training_count_line_edit.setText(QCoreApplication.translate("Widget", u"1", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u041a\u0444. \u043e\u0431\u0443\u0447.", None))
        self.learning_rate_line_edit.setText(QCoreApplication.translate("Widget", u"0.015", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u043a\u0441. \u043a\u043e\u0440\u0440.", None))
        self.max_corr_line_edit.setText(QCoreApplication.translate("Widget", u"0.20", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u0421\u0438\u0433\u043c\u0430 \u0444.", None))
        self.sigma_factor_line_edit.setText(QCoreApplication.translate("Widget", u"0.04", None))
        self.kalman_group_box.setTitle(QCoreApplication.translate("Widget", u"\u041c\u043e\u0434\u0435\u043b\u044c \u041a\u0430\u043b\u043c\u0430\u043d\u0430", None))
        self.kalman_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f. \u043a\u0430\u0434\u0440\u043e\u0432:", None))
        self.skip_frame_line_edit.setText(QCoreApplication.translate("Widget", u"1", None))
        self.fast_roi_group_box.setTitle(QCoreApplication.translate("Widget", u"\u0411\u044b\u0441\u0442\u0440\u043e\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.fast_roi_radio_button.setText(QCoreApplication.translate("Widget", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.roi_width_label.setText(QCoreApplication.translate("Widget", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.roi_width_line_edit.setText(QCoreApplication.translate("Widget", u"128", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"px", None))
        self.roi_height_label.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.roi_height_line_edit.setText(QCoreApplication.translate("Widget", u"128", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"px", None))
        self.tracker_stop_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u041e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.params_group_box.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u043e\u0442\u043e\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u0411\u0438\u0442\u0440\u0435\u0439\u0442 (\u043a\u0431\u0438\u0442/\u0441)", None))
        self.bitrate_line_edit.setText(QCoreApplication.translate("Widget", u"2000", None))
        self.bitrate_line_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.cfs_group_box.setTitle("")
        self.line_edit_c1.setPlaceholderText(QCoreApplication.translate("Widget", u"C1", None))
        self.line_edit_c2.setPlaceholderText(QCoreApplication.translate("Widget", u"C2", None))
        self.line_edit_c3.setPlaceholderText(QCoreApplication.translate("Widget", u"C3", None))
        self.send_cfs_push_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043e\u0442\u043b\u0430\u0434\u043a\u0438", None))
    # retranslateUi

