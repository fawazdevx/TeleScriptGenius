# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomejFroEk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_buttons import *
from ui import resources_rc

class Ui_WelcomeScreen(object):
    def setupUi(self, WelcomeScreen):
        if not WelcomeScreen.objectName():
            WelcomeScreen.setObjectName(u"WelcomeScreen")
        WelcomeScreen.resize(800, 547)
        WelcomeScreen.setStyleSheet(u"*{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background:transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#fff;\n"
"}")
        self.centralwidget = QWidget(WelcomeScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.3, radius:1.1,\n"
"        fx:0.5, fy:0.3,\n"
"        stop:0 rgba(30, 35, 60, 255),\n"
"        stop:0.45 rgba(15, 18, 30, 255),\n"
"        stop:1 rgba(8, 10, 18, 255)\n"
"    );\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"spacing: 10px;")
        self.label_2.setIndent(-1)

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.welSignBtn = QPushButton(self.frame_3)
        self.welSignBtn.setObjectName(u"welSignBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.welSignBtn.sizePolicy().hasHeightForWidth())
        self.welSignBtn.setSizePolicy(sizePolicy1)
        self.welSignBtn.setMinimumSize(QSize(150, 45))
        self.welSignBtn.setFont(font)
        self.welSignBtn.setStyleSheet(u"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.welSignBtn)

        self.welRegBtn = QPushButton(self.frame_3)
        self.welRegBtn.setObjectName(u"welRegBtn")
        sizePolicy1.setHeightForWidth(self.welRegBtn.sizePolicy().hasHeightForWidth())
        self.welRegBtn.setSizePolicy(sizePolicy1)
        self.welRegBtn.setMinimumSize(QSize(200, 45))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.welRegBtn.setFont(font2)
        self.welRegBtn.setStyleSheet(u"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.welRegBtn)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setLayoutDirection(Qt.LeftToRight)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(130, 150))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_5{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/icons/icons/zap.svg"))

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(130, 150))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_7{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icons/icons/shield.svg"))

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)


        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(130, 150))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_8{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/icons/icons/globe.svg"))

        self.verticalLayout_3.addWidget(self.label_11)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)


        self.gridLayout.addWidget(self.frame_8, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame)

        WelcomeScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeScreen)

        QMetaObject.connectSlotsByName(WelcomeScreen)
    # setupUi

    def retranslateUi(self, WelcomeScreen):
        WelcomeScreen.setWindowTitle(QCoreApplication.translate("WelcomeScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("WelcomeScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#25bfff;\">TelescriptGenius</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">SCRIPTING SIMPLICITY</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("WelcomeScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#25bfff;\">Scripting Simplicity,</span></p><p align=\"center\">Genius Complexity.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("WelcomeScreen", u"<html><head/><body><p align=\"center\">Professional telecom scripting tool for engineers</p><p align=\"center\"> Generate activation and configuration scripts in</p><p align=\"center\"> seconds.</p></body></html>", None))
        self.welSignBtn.setText(QCoreApplication.translate("WelcomeScreen", u"Sign In", None))
        self.welRegBtn.setText(QCoreApplication.translate("WelcomeScreen", u"Create Account", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("WelcomeScreen", u"Lightning Fast", None))
        self.label_5.setText(QCoreApplication.translate("WelcomeScreen", u"Generate complex\n"
" telecom scripts in\n"
" seconds with our\n"
" optimized engine.", None))
        self.label_8.setText("")
        self.label_7.setText(QCoreApplication.translate("WelcomeScreen", u"Secure & Reliable", None))
        self.label_9.setText(QCoreApplication.translate("WelcomeScreen", u"Enterprise-grade\n"
" security with validated\n"
" script outputs every\n"
" time.", None))
        self.label_11.setText("")
        self.label_10.setText(QCoreApplication.translate("WelcomeScreen", u"Multi-Region", None))
        self.label_12.setText(QCoreApplication.translate("WelcomeScreen", u"Support for Asaba,\n"
" Kano and more regiona\n"
" templates.", None))
    # retranslateUi

