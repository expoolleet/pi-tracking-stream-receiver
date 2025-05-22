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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1280, 960)
        Widget.setMinimumSize(QSize(640, 480))
        Widget.setMaximumSize(QSize(1920, 1440))
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewLabel = QLabel(Widget)
        self.viewLabel.setObjectName(u"viewLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewLabel.sizePolicy().hasHeightForWidth())
        self.viewLabel.setSizePolicy(sizePolicy)
        self.viewLabel.setMinimumSize(QSize(0, 720))
        self.viewLabel.setCursor(QCursor(Qt.CursorShape.CrossCursor))
#if QT_CONFIG(tooltip)
        self.viewLabel.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.viewLabel.setFrameShape(QFrame.Shape.Panel)
        self.viewLabel.setLineWidth(-2)
        self.viewLabel.setScaledContents(False)
        self.viewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.viewLabel)

        self.connectionLabel = QLabel(Widget)
        self.connectionLabel.setObjectName(u"connectionLabel")
        sizePolicy.setHeightForWidth(self.connectionLabel.sizePolicy().hasHeightForWidth())
        self.connectionLabel.setSizePolicy(sizePolicy)
        self.connectionLabel.setMinimumSize(QSize(0, 0))
        self.connectionLabel.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setPointSize(11)
        self.connectionLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.connectionLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.controlsBox = QGroupBox(Widget)
        self.controlsBox.setObjectName(u"controlsBox")
        self.controlsBox.setMinimumSize(QSize(150, 0))
        self.controlsBox.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout = QVBoxLayout(self.controlsBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.connectButton = QPushButton(self.controlsBox)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setEnabled(False)
        self.connectButton.setMinimumSize(QSize(0, 40))
        self.connectButton.setMaximumSize(QSize(16777215, 16777215))
        self.connectButton.setFont(font)

        self.verticalLayout.addWidget(self.connectButton)

        self.toggleButton = QPushButton(self.controlsBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 40))
        self.toggleButton.setFont(font)

        self.verticalLayout.addWidget(self.toggleButton)


        self.horizontalLayout.addWidget(self.controlsBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 310))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEditDebug = QPlainTextEdit(self.groupBox)
        self.plainTextEditDebug.setObjectName(u"plainTextEditDebug")
        self.plainTextEditDebug.setMaximumSize(QSize(16777215, 300))
        font1 = QFont()
        font1.setPointSize(12)
        self.plainTextEditDebug.setFont(font1)
        self.plainTextEditDebug.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.plainTextEditDebug.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEditDebug)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Streamer", None))
        self.viewLabel.setText("")
        self.connectionLabel.setText(QCoreApplication.translate("Widget", u"Connection...", None))
        self.controlsBox.setTitle(QCoreApplication.translate("Widget", u"Controls", None))
        self.connectButton.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.toggleButton.setText(QCoreApplication.translate("Widget", u"Play", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Debug messages", None))
    # retranslateUi

