# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginCsXfvs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(419, 583)
        LoginScreen.setStyleSheet(u"*{\n"
"    border-radius:10px;\n"
"    background-color:transparent;\n"
"    background:transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color:#1f232a;\n"
"}")
        self.centralwidget = QWidget(LoginScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.emailInput = QLineEdit(self.frame_4)
        self.emailInput.setObjectName(u"emailInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.emailInput.sizePolicy().hasHeightForWidth())
        self.emailInput.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.emailInput.setFont(font2)
        self.emailInput.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.emailInput)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(60, 50))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.passwordInput = QLineEdit(self.frame_5)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy2.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy2)
        self.passwordInput.setFont(font2)
        self.passwordInput.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.passwordInput)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logBtn = QPushButton(self.frame_2)
        self.logBtn.setObjectName(u"logBtn")
        sizePolicy1.setHeightForWidth(self.logBtn.sizePolicy().hasHeightForWidth())
        self.logBtn.setSizePolicy(sizePolicy1)
        self.logBtn.setMinimumSize(QSize(200, 70))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Black")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.logBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.logBtn)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.widget)

        LoginScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("LoginScreen", u"TelescriptGenius", None))
        self.label.setText(QCoreApplication.translate("LoginScreen", u"Email Address", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Enter your Email Address", None))
        self.label_2.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Enter your password", None))
        self.logBtn.setText(QCoreApplication.translate("LoginScreen", u"LOGIN", None))
    # retranslateUi

