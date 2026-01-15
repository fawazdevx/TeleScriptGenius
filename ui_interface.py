# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacefxOWSQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from custom_buttons import *
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"*{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background:transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"    background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"   text-align:left;\n"
"   padding: 5px 10px;\n"
"   border-top-left-radius: 10px;\n"
"   border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"    background-color:#2c313c;\n"
"}\n"
"#frame_4,#frame_8,#popupNotificationSubContainer{\n"
"	background-color:#16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer,#footerContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	backgr"
                        "ound-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(65, 16777215))
        self.leftMenuContainer.setStyleSheet(u"#centralwidget{\n"
"   background-color:#1f232a;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamily(u"Segoe Print")
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color:#1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.genBtn = QPushButton(self.frame_2)
        self.genBtn.setObjectName(u"genBtn")
        self.genBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.genBtn.setIcon(icon2)
        self.genBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.genBtn)

        self.regionsBtn = QPushButton(self.frame_2)
        self.regionsBtn.setObjectName(u"regionsBtn")
        self.regionsBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.regionsBtn.setIcon(icon3)
        self.regionsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.regionsBtn)

        self.scriptsBtn = QPushButton(self.frame_2)
        self.scriptsBtn.setObjectName(u"scriptsBtn")
        self.scriptsBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scriptsBtn.setIcon(icon4)
        self.scriptsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.scriptsBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon6)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        sizePolicy1.setHeightForWidth(self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy1)
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon8)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.centerMenuPages.sizePolicy().hasHeightForWidth())
        self.centerMenuPages.setSizePolicy(sizePolicy1)
        self.centerMenuPages.setMinimumSize(QSize(0, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.settingsMenu = QFrame(self.page)
        self.settingsMenu.setObjectName(u"settingsMenu")
        sizePolicy1.setHeightForWidth(self.settingsMenu.sizePolicy().hasHeightForWidth())
        self.settingsMenu.setSizePolicy(sizePolicy1)
        self.settingsMenu.setFrameShape(QFrame.NoFrame)
        self.settingsMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.settingsMenu)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.settingsMenu)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Segoe Print")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_2, 0, Qt.AlignTop)

        self.securityBtn = QPushButton(self.settingsMenu)
        self.securityBtn.setObjectName(u"securityBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.securityBtn.sizePolicy().hasHeightForWidth())
        self.securityBtn.setSizePolicy(sizePolicy2)
        self.securityBtn.setMinimumSize(QSize(0, 45))
        self.securityBtn.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/shield.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.securityBtn.setIcon(icon9)
        self.securityBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.securityBtn)

        self.verification = QPushButton(self.settingsMenu)
        self.verification.setObjectName(u"verification")
        self.verification.setMinimumSize(QSize(0, 45))
        self.verification.setFont(font1)
        self.verification.setIcon(icon4)
        self.verification.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.verification)

        self.pushButton_9 = QPushButton(self.settingsMenu)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 45))
        self.pushButton_9.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.pushButton_9)

        self.pushButton_21 = QPushButton(self.settingsMenu)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 45))
        self.pushButton_21.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon11)
        self.pushButton_21.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.pushButton_21)

        self.pushButton_42 = QPushButton(self.settingsMenu)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 45))
        self.pushButton_42.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_42.setIcon(icon12)
        self.pushButton_42.setIconSize(QSize(24, 24))

        self.verticalLayout_42.addWidget(self.pushButton_42)


        self.verticalLayout_7.addWidget(self.settingsMenu, 0, Qt.AlignTop)

        self.centerMenuPages.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.frame_90 = QFrame(self.page_3)
        self.frame_90.setObjectName(u"frame_90")
        sizePolicy.setHeightForWidth(self.frame_90.sizePolicy().hasHeightForWidth())
        self.frame_90.setSizePolicy(sizePolicy)
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.textEdit_3 = QTextEdit(self.frame_90)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QSize(222, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setStyleSheet(u"background: transparent;")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.textEdit_3)


        self.verticalLayout_9.addWidget(self.frame_90)

        self.centerMenuPages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.extraCenter = QFrame(self.page_2)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setStyleSheet(u"")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_43.setSpacing(9)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(9, 9, 9, 9)
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_43.addWidget(self.textEdit)


        self.verticalLayout_8.addWidget(self.extraCenter)

        self.centerMenuPages.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy3)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.app_icon = QPushButton(self.frame_5)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy4)
        self.app_icon.setMinimumSize(QSize(0, 0))
        self.app_icon.setIconSize(QSize(40, 30))

        self.horizontalLayout_7.addWidget(self.app_icon)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamily(u"Segoe Print")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_6.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon13)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon14)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon15)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_btn = QPushButton(self.frame_7)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon16)

        self.horizontalLayout_4.addWidget(self.minimize_window_btn)

        self.restore_window_btn = QPushButton(self.frame_7)
        self.restore_window_btn.setObjectName(u"restore_window_btn")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_btn.setIcon(icon17)

        self.horizontalLayout_4.addWidget(self.restore_window_btn)

        self.close_window_btn = QPushButton(self.frame_7)
        self.close_window_btn.setObjectName(u"close_window_btn")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon18)

        self.horizontalLayout_4.addWidget(self.close_window_btn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QCustomSlideMenu(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy5)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"background-color: #1f232a;")
        self.verticalLayout_16 = QVBoxLayout(self.home_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_10 = QLabel(self.home_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.home_page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.widget_2.setFont(font5)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_44 = QVBoxLayout(self.widget_4)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_25 = QFrame(self.widget_4)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_25)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_24 = QLabel(self.frame_25)
        self.label_24.setObjectName(u"label_24")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setBold(True)
        font6.setWeight(75)
        self.label_24.setFont(font6)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(True)

        self.verticalLayout_57.addWidget(self.label_24)

        self.frame_33 = QFrame(self.frame_25)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border-radius:10px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_33)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_31 = QLabel(self.frame_33)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font5)
        self.label_31.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.verticalLayout_62.addWidget(self.label_31)

        self.frame_38 = QFrame(self.frame_33)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_28.setSpacing(3)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_38)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy6)
        self.pushButton_4.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon19)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_4)

        self.label_32 = QLabel(self.frame_38)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)
        self.label_32.setMinimumSize(QSize(300, 0))
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_32.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.label_32)


        self.verticalLayout_62.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_33)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_30.setSpacing(3)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_5 = QPushButton(self.frame_39)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy6.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy6)
        self.pushButton_5.setStyleSheet(u"")
        self.pushButton_5.setIcon(icon19)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_30.addWidget(self.pushButton_5)

        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_33.setFrameShadow(QFrame.Raised)
        self.label_33.setLineWidth(2)
        self.label_33.setWordWrap(True)

        self.horizontalLayout_30.addWidget(self.label_33)


        self.verticalLayout_62.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_33)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_31.setSpacing(3)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_6 = QPushButton(self.frame_40)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy6.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy6)
        self.pushButton_6.setStyleSheet(u"")
        self.pushButton_6.setIcon(icon19)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_31.addWidget(self.pushButton_6)

        self.label_34 = QLabel(self.frame_40)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_34.setFrameShadow(QFrame.Raised)
        self.label_34.setLineWidth(2)
        self.label_34.setWordWrap(True)

        self.horizontalLayout_31.addWidget(self.label_34)


        self.verticalLayout_62.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_33)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_32.setSpacing(3)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_7 = QPushButton(self.frame_41)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy6.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy6)
        self.pushButton_7.setStyleSheet(u"")
        self.pushButton_7.setIcon(icon19)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.pushButton_7)

        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_35.setFrameShadow(QFrame.Raised)
        self.label_35.setLineWidth(2)
        self.label_35.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.label_35)


        self.verticalLayout_62.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_33)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_33.setSpacing(3)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_8 = QPushButton(self.frame_42)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy6.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy6)
        self.pushButton_8.setStyleSheet(u"")
        self.pushButton_8.setIcon(icon19)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.pushButton_8)

        self.label_36 = QLabel(self.frame_42)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_36.setFrameShadow(QFrame.Raised)
        self.label_36.setLineWidth(2)
        self.label_36.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.label_36)


        self.verticalLayout_62.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_33)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_34.setSpacing(3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_10 = QPushButton(self.frame_43)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy6.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy6)
        self.pushButton_10.setStyleSheet(u"")
        self.pushButton_10.setIcon(icon19)
        self.pushButton_10.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.pushButton_10)

        self.label_37 = QLabel(self.frame_43)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)
        self.label_37.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"")
        self.label_37.setFrameShadow(QFrame.Raised)
        self.label_37.setLineWidth(2)
        self.label_37.setWordWrap(True)

        self.horizontalLayout_34.addWidget(self.label_37)


        self.verticalLayout_62.addWidget(self.frame_43)


        self.verticalLayout_57.addWidget(self.frame_33)


        self.verticalLayout_44.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.widget_4)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.getStartBtn = QPushButton(self.frame_26)
        self.getStartBtn.setObjectName(u"getStartBtn")
        self.getStartBtn.setFont(font5)

        self.horizontalLayout_27.addWidget(self.getStartBtn)


        self.verticalLayout_44.addWidget(self.frame_26)


        self.horizontalLayout_23.addWidget(self.widget_4)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_64 = QVBoxLayout(self.widget_9)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.frame_34 = QFrame(self.widget_9)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy1.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy1)
        self.frame_34.setMaximumSize(QSize(16777215, 16777215))
        self.frame_34.setStyleSheet(u"border-radius:10px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_34)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_13 = QLabel(self.frame_34)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 200))
        self.label_13.setMaximumSize(QSize(200, 200))
        self.label_13.setBaseSize(QSize(100, 200))
        self.label_13.setPixmap(QPixmap(u":/images/images/learning1.png"))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(False)

        self.verticalLayout_61.addWidget(self.label_13)

        self.pushButton = QPushButton(self.frame_34)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font5)

        self.verticalLayout_61.addWidget(self.pushButton)


        self.verticalLayout_64.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.widget_9)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border-radius:10px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_35)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_27 = QLabel(self.frame_35)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setScaledContents(True)

        self.verticalLayout_60.addWidget(self.label_27)


        self.verticalLayout_64.addWidget(self.frame_35)


        self.horizontalLayout_23.addWidget(self.widget_9)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setFont(font1)
        self.widget_3.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout_34 = QVBoxLayout(self.widget_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_16 = QFrame(self.widget_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"border-radius:10px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_5.setFont(font7)

        self.horizontalLayout_25.addWidget(self.label_5)

        self.copyBtn = QPushButton(self.frame_16)
        self.copyBtn.setObjectName(u"copyBtn")
        sizePolicy6.setHeightForWidth(self.copyBtn.sizePolicy().hasHeightForWidth())
        self.copyBtn.setSizePolicy(sizePolicy6)
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.copyBtn.setIcon(icon20)
        self.copyBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.copyBtn)


        self.verticalLayout_34.addWidget(self.frame_16)

        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setFont(font5)
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"	border-radius:10px;\n"
" }\n"
"QScrollArea{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"	border-radius:10px;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 106, 400))
        sizePolicy6.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy6)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(100, 400))
        self.scrollAreaWidgetContents.setFont(font5)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.widget_5.setMinimumSize(QSize(100, 500))
        self.widget_5.setFont(font5)
        self.widget_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"border-radius:10px;")
        self.verticalLayout_33 = QVBoxLayout(self.widget_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")

        self.verticalLayout_32.addWidget(self.widget_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_34.addWidget(self.scrollArea, 0, Qt.AlignTop)


        self.horizontalLayout_23.addWidget(self.widget_3, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.widget_2)

        self.mainPages.addWidget(self.home_page)
        self.region_page = QWidget()
        self.region_page.setObjectName(u"region_page")
        self.region_page.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_31 = QVBoxLayout(self.region_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_11 = QLabel(self.region_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_11, 0, Qt.AlignTop)

        self.label_23 = QLabel(self.region_page)
        self.label_23.setObjectName(u"label_23")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_23.setFont(font8)

        self.verticalLayout_31.addWidget(self.label_23)

        self.frame_23 = QFrame(self.region_page)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet(u"background-color: transparent;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_23)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.scrollArea_3 = QScrollArea(self.frame_23)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 336, 229))
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy7)
        self.scrollAreaWidgetContents_7.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents_7.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_22.setObjectName(u"label_22")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_22.setFont(font9)

        self.verticalLayout_40.addWidget(self.label_22)

        self.frame_31 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_31)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy8)
        self.label_16.setMinimumSize(QSize(300, 0))
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"")

        self.verticalLayout_47.addWidget(self.label_16)


        self.verticalLayout_40.addWidget(self.frame_31)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_27)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_17 = QLabel(self.frame_27)
        self.label_17.setObjectName(u"label_17")
        sizePolicy8.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy8)
        self.label_17.setMinimumSize(QSize(300, 0))
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.label_17)


        self.verticalLayout_40.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_28)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_20 = QLabel(self.frame_28)
        self.label_20.setObjectName(u"label_20")
        sizePolicy8.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy8)
        self.label_20.setMinimumSize(QSize(300, 0))
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.label_20)


        self.verticalLayout_40.addWidget(self.frame_28)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_32)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_21 = QLabel(self.frame_32)
        self.label_21.setObjectName(u"label_21")
        sizePolicy8.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy8)
        self.label_21.setMinimumSize(QSize(300, 0))
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.label_21)


        self.verticalLayout_40.addWidget(self.frame_32)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_24)
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")

        self.verticalLayout_40.addWidget(self.frame_24)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_39.addWidget(self.scrollArea_3)


        self.verticalLayout_31.addWidget(self.frame_23)

        self.mainPages.addWidget(self.region_page)
        self.temp_page = QWidget()
        self.temp_page.setObjectName(u"temp_page")
        self.verticalLayout_22 = QVBoxLayout(self.temp_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_15 = QFrame(self.temp_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_18, 0, Qt.AlignTop)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_19, 0, Qt.AlignLeft)


        self.verticalLayout_22.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.widget = QWidget(self.temp_page)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.ml10GBtn = QPushButton(self.widget)
        self.ml10GBtn.setObjectName(u"ml10GBtn")
        sizePolicy2.setHeightForWidth(self.ml10GBtn.sizePolicy().hasHeightForWidth())
        self.ml10GBtn.setSizePolicy(sizePolicy2)
        self.ml10GBtn.setMinimumSize(QSize(0, 150))
        self.ml10GBtn.setFont(font1)
        self.ml10GBtn.setStyleSheet(u"border-radius:20px;")

        self.gridLayout.addWidget(self.ml10GBtn, 0, 0, 1, 1)

        self.routerBtn = QPushButton(self.widget)
        self.routerBtn.setObjectName(u"routerBtn")
        sizePolicy2.setHeightForWidth(self.routerBtn.sizePolicy().hasHeightForWidth())
        self.routerBtn.setSizePolicy(sizePolicy2)
        self.routerBtn.setMinimumSize(QSize(0, 150))
        self.routerBtn.setFont(font1)
        self.routerBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout.addWidget(self.routerBtn, 0, 1, 1, 1)

        self.aviatBtn = QPushButton(self.widget)
        self.aviatBtn.setObjectName(u"aviatBtn")
        sizePolicy2.setHeightForWidth(self.aviatBtn.sizePolicy().hasHeightForWidth())
        self.aviatBtn.setSizePolicy(sizePolicy2)
        self.aviatBtn.setMinimumSize(QSize(0, 150))
        self.aviatBtn.setFont(font1)
        self.aviatBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout.addWidget(self.aviatBtn, 0, 2, 1, 1)

        self.linkBtn = QPushButton(self.widget)
        self.linkBtn.setObjectName(u"linkBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.linkBtn.sizePolicy().hasHeightForWidth())
        self.linkBtn.setSizePolicy(sizePolicy9)
        self.linkBtn.setFont(font1)
        self.linkBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout.addWidget(self.linkBtn, 0, 3, 1, 1)


        self.verticalLayout_22.addWidget(self.widget)

        self.mainPages.addWidget(self.temp_page)
        self.router_page = QWidget()
        self.router_page.setObjectName(u"router_page")
        self.verticalLayout_65 = QVBoxLayout(self.router_page)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.frame_45 = QFrame(self.router_page)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_45)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.backrsBtn = QPushButton(self.frame_45)
        self.backrsBtn.setObjectName(u"backrsBtn")
        sizePolicy6.setHeightForWidth(self.backrsBtn.sizePolicy().hasHeightForWidth())
        self.backrsBtn.setSizePolicy(sizePolicy6)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backrsBtn.setIcon(icon21)
        self.backrsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_67.addWidget(self.backrsBtn)


        self.verticalLayout_65.addWidget(self.frame_45, 0, Qt.AlignTop)

        self.label_39 = QLabel(self.router_page)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setFont(font2)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.label_39)

        self.mainPages.addWidget(self.router_page)
        self.linkCheck_page = QWidget()
        self.linkCheck_page.setObjectName(u"linkCheck_page")
        self.verticalLayout_66 = QVBoxLayout(self.linkCheck_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_46 = QFrame(self.linkCheck_page)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_46)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.backlcBtn = QPushButton(self.frame_46)
        self.backlcBtn.setObjectName(u"backlcBtn")
        sizePolicy6.setHeightForWidth(self.backlcBtn.sizePolicy().hasHeightForWidth())
        self.backlcBtn.setSizePolicy(sizePolicy6)
        self.backlcBtn.setIcon(icon21)
        self.backlcBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_68.addWidget(self.backlcBtn)


        self.verticalLayout_66.addWidget(self.frame_46)

        self.label_40 = QLabel(self.linkCheck_page)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setFont(font2)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_40)

        self.mainPages.addWidget(self.linkCheck_page)
        self.scripts_page = QWidget()
        self.scripts_page.setObjectName(u"scripts_page")
        self.horizontalLayout_24 = QHBoxLayout(self.scripts_page)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_6 = QWidget(self.scripts_page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setFont(font5)
        self.widget_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.widget_6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)

        self.verticalLayout_35.addWidget(self.label_12)

        self.scrollArea_2 = QScrollArea(self.widget_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFont(font5)
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 255, 255));\n"
"	border-radius:10px;\n"
" }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 36, 36))
        self.scrollAreaWidgetContents_6.setFont(font5)
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_8 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setFont(font5)
        self.verticalLayout_38 = QVBoxLayout(self.widget_8)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")

        self.verticalLayout_37.addWidget(self.widget_8)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_35.addWidget(self.scrollArea_2)


        self.horizontalLayout_24.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.scripts_page)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_36 = QVBoxLayout(self.widget_7)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.view_script = QPushButton(self.widget_7)
        self.view_script.setObjectName(u"view_script")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.view_script.sizePolicy().hasHeightForWidth())
        self.view_script.setSizePolicy(sizePolicy10)
        self.view_script.setMinimumSize(QSize(0, 30))
        self.view_script.setFont(font7)

        self.verticalLayout_36.addWidget(self.view_script)

        self.viewscriptEdit = QTextEdit(self.widget_7)
        self.viewscriptEdit.setObjectName(u"viewscriptEdit")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.viewscriptEdit.setFont(font10)
        self.viewscriptEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"border-radius:10px;")

        self.verticalLayout_36.addWidget(self.viewscriptEdit)


        self.horizontalLayout_24.addWidget(self.widget_7)

        self.mainPages.addWidget(self.scripts_page)
        self.region10G_page = QWidget()
        self.region10G_page.setObjectName(u"region10G_page")
        self.verticalLayout_17 = QVBoxLayout(self.region10G_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_29 = QFrame(self.region10G_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.backRBtn = QPushButton(self.frame_29)
        self.backRBtn.setObjectName(u"backRBtn")
        sizePolicy6.setHeightForWidth(self.backRBtn.sizePolicy().hasHeightForWidth())
        self.backRBtn.setSizePolicy(sizePolicy6)
        self.backRBtn.setIcon(icon21)
        self.backRBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.backRBtn)

        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy11)
        self.label_28.setFont(font2)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_28)


        self.verticalLayout_17.addWidget(self.frame_29, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.region10G_page)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_13)
        self.gridLayout_5.setSpacing(20)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.aRegBtn = QPushButton(self.frame_13)
        self.aRegBtn.setObjectName(u"aRegBtn")
        self.aRegBtn.setMinimumSize(QSize(0, 100))
        self.aRegBtn.setFont(font1)
        self.aRegBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_5.addWidget(self.aRegBtn, 0, 0, 1, 1)

        self.eRegBtn = QPushButton(self.frame_13)
        self.eRegBtn.setObjectName(u"eRegBtn")
        self.eRegBtn.setMinimumSize(QSize(0, 100))
        self.eRegBtn.setFont(font1)
        self.eRegBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_5.addWidget(self.eRegBtn, 0, 1, 1, 1)

        self.kRegBtn = QPushButton(self.frame_13)
        self.kRegBtn.setObjectName(u"kRegBtn")
        self.kRegBtn.setMinimumSize(QSize(0, 100))
        self.kRegBtn.setFont(font1)
        self.kRegBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_5.addWidget(self.kRegBtn, 1, 0, 1, 1)

        self.oRegBtn = QPushButton(self.frame_13)
        self.oRegBtn.setObjectName(u"oRegBtn")
        self.oRegBtn.setMinimumSize(QSize(0, 100))
        self.oRegBtn.setFont(font1)
        self.oRegBtn.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_5.addWidget(self.oRegBtn, 1, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.mainPages.addWidget(self.region10G_page)
        self.regionAV_page = QWidget()
        self.regionAV_page.setObjectName(u"regionAV_page")
        self.verticalLayout_18 = QVBoxLayout(self.regionAV_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_30 = QFrame(self.regionAV_page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.backAVRBtn = QPushButton(self.frame_30)
        self.backAVRBtn.setObjectName(u"backAVRBtn")
        sizePolicy6.setHeightForWidth(self.backAVRBtn.sizePolicy().hasHeightForWidth())
        self.backAVRBtn.setSizePolicy(sizePolicy6)
        self.backAVRBtn.setIcon(icon21)
        self.backAVRBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.backAVRBtn)

        self.label_29 = QLabel(self.frame_30)
        self.label_29.setObjectName(u"label_29")
        sizePolicy11.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy11)
        self.label_29.setFont(font2)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_29)


        self.verticalLayout_18.addWidget(self.frame_30)

        self.frame_18 = QFrame(self.regionAV_page)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_18)
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.aRegBtnAV = QPushButton(self.frame_18)
        self.aRegBtnAV.setObjectName(u"aRegBtnAV")
        self.aRegBtnAV.setMinimumSize(QSize(0, 100))
        self.aRegBtnAV.setFont(font1)
        self.aRegBtnAV.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_6.addWidget(self.aRegBtnAV, 0, 0, 1, 1)

        self.eRegBtnAV = QPushButton(self.frame_18)
        self.eRegBtnAV.setObjectName(u"eRegBtnAV")
        self.eRegBtnAV.setMinimumSize(QSize(0, 100))
        self.eRegBtnAV.setFont(font1)
        self.eRegBtnAV.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_6.addWidget(self.eRegBtnAV, 0, 1, 1, 1)

        self.kRegBtnAV = QPushButton(self.frame_18)
        self.kRegBtnAV.setObjectName(u"kRegBtnAV")
        self.kRegBtnAV.setMinimumSize(QSize(0, 100))
        self.kRegBtnAV.setFont(font1)
        self.kRegBtnAV.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_6.addWidget(self.kRegBtnAV, 1, 0, 1, 1)

        self.oRegBtnAV = QPushButton(self.frame_18)
        self.oRegBtnAV.setObjectName(u"oRegBtnAV")
        self.oRegBtnAV.setMinimumSize(QSize(0, 100))
        self.oRegBtnAV.setFont(font1)
        self.oRegBtnAV.setStyleSheet(u"border-radius:10px;")

        self.gridLayout_6.addWidget(self.oRegBtnAV, 1, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.mainPages.addWidget(self.regionAV_page)
        self.owerri10G_page = QWidget()
        self.owerri10G_page.setObjectName(u"owerri10G_page")
        self.verticalLayout_25 = QVBoxLayout(self.owerri10G_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_71 = QFrame(self.owerri10G_page)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_71)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.frame_11 = QFrame(self.frame_71)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.backOBtn = QPushButton(self.frame_11)
        self.backOBtn.setObjectName(u"backOBtn")
        sizePolicy6.setHeightForWidth(self.backOBtn.sizePolicy().hasHeightForWidth())
        self.backOBtn.setSizePolicy(sizePolicy6)
        self.backOBtn.setIcon(icon21)
        self.backOBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.backOBtn)

        self.label_61 = QLabel(self.frame_11)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font2)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_61)


        self.verticalLayout_55.addWidget(self.frame_11)

        self.label_62 = QLabel(self.frame_71)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font2)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.label_62, 0, Qt.AlignLeft)

        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy8.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy8)
        self.frame_72.setMinimumSize(QSize(500, 0))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_63 = QLabel(self.frame_72)
        self.label_63.setObjectName(u"label_63")
        sizePolicy8.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy8)
        self.label_63.setMinimumSize(QSize(50, 0))
        self.label_63.setFont(font5)
        self.label_63.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"border-radius:10px;")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_63)

        self.sites_Ocp_Input = QLineEdit(self.frame_72)
        self.sites_Ocp_Input.setObjectName(u"sites_Ocp_Input")
        sizePolicy9.setHeightForWidth(self.sites_Ocp_Input.sizePolicy().hasHeightForWidth())
        self.sites_Ocp_Input.setSizePolicy(sizePolicy9)
        self.sites_Ocp_Input.setFont(font1)
        self.sites_Ocp_Input.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")
        self.sites_Ocp_Input.setDragEnabled(True)

        self.horizontalLayout_43.addWidget(self.sites_Ocp_Input)


        self.verticalLayout_55.addWidget(self.frame_72)


        self.verticalLayout_25.addWidget(self.frame_71)

        self.frame_73 = QFrame(self.owerri10G_page)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_73)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_44.setSpacing(20)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.genOCPBtn = QPushButton(self.frame_74)
        self.genOCPBtn.setObjectName(u"genOCPBtn")
        sizePolicy6.setHeightForWidth(self.genOCPBtn.sizePolicy().hasHeightForWidth())
        self.genOCPBtn.setSizePolicy(sizePolicy6)
        self.genOCPBtn.setMinimumSize(QSize(300, 150))
        self.genOCPBtn.setFont(font1)

        self.horizontalLayout_44.addWidget(self.genOCPBtn)

        self.genOCSBtn = QPushButton(self.frame_74)
        self.genOCSBtn.setObjectName(u"genOCSBtn")
        sizePolicy6.setHeightForWidth(self.genOCSBtn.sizePolicy().hasHeightForWidth())
        self.genOCSBtn.setSizePolicy(sizePolicy6)
        self.genOCSBtn.setMinimumSize(QSize(300, 150))
        self.genOCSBtn.setFont(font1)

        self.horizontalLayout_44.addWidget(self.genOCSBtn)


        self.gridLayout_14.addWidget(self.frame_74, 0, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_73)

        self.mainPages.addWidget(self.owerri10G_page)
        self.kano10G_page = QWidget()
        self.kano10G_page.setObjectName(u"kano10G_page")
        self.verticalLayout_24 = QVBoxLayout(self.kano10G_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_67 = QFrame(self.kano10G_page)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_67)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_12 = QFrame(self.frame_67)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.backKBtn = QPushButton(self.frame_12)
        self.backKBtn.setObjectName(u"backKBtn")
        sizePolicy6.setHeightForWidth(self.backKBtn.sizePolicy().hasHeightForWidth())
        self.backKBtn.setSizePolicy(sizePolicy6)
        self.backKBtn.setIcon(icon21)
        self.backKBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.backKBtn)

        self.label_58 = QLabel(self.frame_12)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_58)


        self.verticalLayout_53.addWidget(self.frame_12)

        self.label_59 = QLabel(self.frame_67)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font2)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_59, 0, Qt.AlignLeft)

        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        sizePolicy8.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy8)
        self.frame_68.setMinimumSize(QSize(500, 0))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_60 = QLabel(self.frame_68)
        self.label_60.setObjectName(u"label_60")
        sizePolicy8.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy8)
        self.label_60.setMinimumSize(QSize(50, 0))
        self.label_60.setFont(font5)
        self.label_60.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_60)

        self.sites_Kcp_Input = QLineEdit(self.frame_68)
        self.sites_Kcp_Input.setObjectName(u"sites_Kcp_Input")
        sizePolicy9.setHeightForWidth(self.sites_Kcp_Input.sizePolicy().hasHeightForWidth())
        self.sites_Kcp_Input.setSizePolicy(sizePolicy9)
        self.sites_Kcp_Input.setFont(font1)
        self.sites_Kcp_Input.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")
        self.sites_Kcp_Input.setDragEnabled(True)

        self.horizontalLayout_41.addWidget(self.sites_Kcp_Input)


        self.verticalLayout_53.addWidget(self.frame_68)


        self.verticalLayout_24.addWidget(self.frame_67)

        self.frame_69 = QFrame(self.kano10G_page)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_69)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_42.setSpacing(20)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.genKCPBtn = QPushButton(self.frame_70)
        self.genKCPBtn.setObjectName(u"genKCPBtn")
        sizePolicy6.setHeightForWidth(self.genKCPBtn.sizePolicy().hasHeightForWidth())
        self.genKCPBtn.setSizePolicy(sizePolicy6)
        self.genKCPBtn.setMinimumSize(QSize(300, 150))
        self.genKCPBtn.setFont(font1)

        self.horizontalLayout_42.addWidget(self.genKCPBtn)

        self.genKCSBtn = QPushButton(self.frame_70)
        self.genKCSBtn.setObjectName(u"genKCSBtn")
        sizePolicy6.setHeightForWidth(self.genKCSBtn.sizePolicy().hasHeightForWidth())
        self.genKCSBtn.setSizePolicy(sizePolicy6)
        self.genKCSBtn.setMinimumSize(QSize(300, 150))
        self.genKCSBtn.setFont(font1)

        self.horizontalLayout_42.addWidget(self.genKCSBtn)


        self.gridLayout_13.addWidget(self.frame_70, 0, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.frame_69)

        self.mainPages.addWidget(self.kano10G_page)
        self.enugu10G_page = QWidget()
        self.enugu10G_page.setObjectName(u"enugu10G_page")
        self.verticalLayout_23 = QVBoxLayout(self.enugu10G_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_63 = QFrame(self.enugu10G_page)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_63)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_17 = QFrame(self.frame_63)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.backEBtn = QPushButton(self.frame_17)
        self.backEBtn.setObjectName(u"backEBtn")
        sizePolicy6.setHeightForWidth(self.backEBtn.sizePolicy().hasHeightForWidth())
        self.backEBtn.setSizePolicy(sizePolicy6)
        self.backEBtn.setIcon(icon21)
        self.backEBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.backEBtn)

        self.label_55 = QLabel(self.frame_17)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_55)


        self.verticalLayout_51.addWidget(self.frame_17)

        self.label_56 = QLabel(self.frame_63)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_56, 0, Qt.AlignLeft)

        self.frame_64 = QFrame(self.frame_63)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy8.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy8)
        self.frame_64.setMinimumSize(QSize(500, 0))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_57 = QLabel(self.frame_64)
        self.label_57.setObjectName(u"label_57")
        sizePolicy8.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy8)
        self.label_57.setMinimumSize(QSize(50, 0))
        self.label_57.setFont(font5)
        self.label_57.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius:10px;")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_57)

        self.sites_Ecp_Input = QLineEdit(self.frame_64)
        self.sites_Ecp_Input.setObjectName(u"sites_Ecp_Input")
        sizePolicy9.setHeightForWidth(self.sites_Ecp_Input.sizePolicy().hasHeightForWidth())
        self.sites_Ecp_Input.setSizePolicy(sizePolicy9)
        self.sites_Ecp_Input.setFont(font1)
        self.sites_Ecp_Input.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;border-radius:10px;\n"
"")
        self.sites_Ecp_Input.setDragEnabled(True)

        self.horizontalLayout_39.addWidget(self.sites_Ecp_Input)


        self.verticalLayout_51.addWidget(self.frame_64)


        self.verticalLayout_23.addWidget(self.frame_63)

        self.frame_65 = QFrame(self.enugu10G_page)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_65)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_40.setSpacing(20)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.genECPBtn = QPushButton(self.frame_66)
        self.genECPBtn.setObjectName(u"genECPBtn")
        sizePolicy6.setHeightForWidth(self.genECPBtn.sizePolicy().hasHeightForWidth())
        self.genECPBtn.setSizePolicy(sizePolicy6)
        self.genECPBtn.setMinimumSize(QSize(300, 150))
        self.genECPBtn.setFont(font1)

        self.horizontalLayout_40.addWidget(self.genECPBtn)

        self.genECSBtn = QPushButton(self.frame_66)
        self.genECSBtn.setObjectName(u"genECSBtn")
        sizePolicy6.setHeightForWidth(self.genECSBtn.sizePolicy().hasHeightForWidth())
        self.genECSBtn.setSizePolicy(sizePolicy6)
        self.genECSBtn.setMinimumSize(QSize(300, 150))
        self.genECSBtn.setFont(font1)

        self.horizontalLayout_40.addWidget(self.genECSBtn)


        self.gridLayout_12.addWidget(self.frame_66, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_65)

        self.mainPages.addWidget(self.enugu10G_page)
        self.asaba10G_page = QWidget()
        self.asaba10G_page.setObjectName(u"asaba10G_page")
        self.verticalLayout_21 = QVBoxLayout(self.asaba10G_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_60 = QFrame(self.asaba10G_page)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_60)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_14 = QFrame(self.frame_60)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.backABtn = QPushButton(self.frame_14)
        self.backABtn.setObjectName(u"backABtn")
        sizePolicy6.setHeightForWidth(self.backABtn.sizePolicy().hasHeightForWidth())
        self.backABtn.setSizePolicy(sizePolicy6)
        self.backABtn.setIcon(icon21)
        self.backABtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.backABtn)

        self.label_52 = QLabel(self.frame_14)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_52)


        self.verticalLayout_49.addWidget(self.frame_14)

        self.label_53 = QLabel(self.frame_60)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.label_53, 0, Qt.AlignLeft)

        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy8.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy8)
        self.frame_61.setMinimumSize(QSize(500, 0))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_54 = QLabel(self.frame_61)
        self.label_54.setObjectName(u"label_54")
        sizePolicy8.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy8)
        self.label_54.setMinimumSize(QSize(50, 0))
        self.label_54.setFont(font5)
        self.label_54.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:10px;")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_54)

        self.sites_Acp_Input = QLineEdit(self.frame_61)
        self.sites_Acp_Input.setObjectName(u"sites_Acp_Input")
        sizePolicy9.setHeightForWidth(self.sites_Acp_Input.sizePolicy().hasHeightForWidth())
        self.sites_Acp_Input.setSizePolicy(sizePolicy9)
        self.sites_Acp_Input.setMinimumSize(QSize(0, 0))
        self.sites_Acp_Input.setMaximumSize(QSize(16777215, 16777215))
        self.sites_Acp_Input.setFont(font1)
        self.sites_Acp_Input.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;border-radius:10px;\n"
"")
        self.sites_Acp_Input.setDragEnabled(True)

        self.horizontalLayout_37.addWidget(self.sites_Acp_Input)


        self.verticalLayout_49.addWidget(self.frame_61)


        self.verticalLayout_21.addWidget(self.frame_60)

        self.frame_62 = QFrame(self.asaba10G_page)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_38.setSpacing(20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.genACPBtn = QPushButton(self.frame_62)
        self.genACPBtn.setObjectName(u"genACPBtn")
        sizePolicy6.setHeightForWidth(self.genACPBtn.sizePolicy().hasHeightForWidth())
        self.genACPBtn.setSizePolicy(sizePolicy6)
        self.genACPBtn.setMinimumSize(QSize(300, 150))
        self.genACPBtn.setFont(font1)

        self.horizontalLayout_38.addWidget(self.genACPBtn)

        self.genACSBtn = QPushButton(self.frame_62)
        self.genACSBtn.setObjectName(u"genACSBtn")
        sizePolicy6.setHeightForWidth(self.genACSBtn.sizePolicy().hasHeightForWidth())
        self.genACSBtn.setSizePolicy(sizePolicy6)
        self.genACSBtn.setMinimumSize(QSize(300, 150))
        self.genACSBtn.setFont(font1)

        self.horizontalLayout_38.addWidget(self.genACSBtn)


        self.verticalLayout_21.addWidget(self.frame_62)

        self.mainPages.addWidget(self.asaba10G_page)
        self.asabaAV_page = QWidget()
        self.asabaAV_page.setObjectName(u"asabaAV_page")
        self.verticalLayout_26 = QVBoxLayout(self.asabaAV_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_76 = QFrame(self.asabaAV_page)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_76)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_19 = QFrame(self.frame_76)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.backABtnAV = QPushButton(self.frame_19)
        self.backABtnAV.setObjectName(u"backABtnAV")
        sizePolicy6.setHeightForWidth(self.backABtnAV.sizePolicy().hasHeightForWidth())
        self.backABtnAV.setSizePolicy(sizePolicy6)
        self.backABtnAV.setIcon(icon21)
        self.backABtnAV.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.backABtnAV)

        self.label_64 = QLabel(self.frame_19)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_64)


        self.verticalLayout_50.addWidget(self.frame_19)

        self.label_65 = QLabel(self.frame_76)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_65, 0, Qt.AlignLeft)

        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        sizePolicy8.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy8)
        self.frame_77.setMinimumSize(QSize(500, 0))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_66 = QLabel(self.frame_77)
        self.label_66.setObjectName(u"label_66")
        sizePolicy8.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy8)
        self.label_66.setMinimumSize(QSize(50, 0))
        self.label_66.setFont(font5)
        self.label_66.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:10px;")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.label_66)

        self.sites_Acp_InputAV = QLineEdit(self.frame_77)
        self.sites_Acp_InputAV.setObjectName(u"sites_Acp_InputAV")
        sizePolicy9.setHeightForWidth(self.sites_Acp_InputAV.sizePolicy().hasHeightForWidth())
        self.sites_Acp_InputAV.setSizePolicy(sizePolicy9)
        self.sites_Acp_InputAV.setMinimumSize(QSize(0, 0))
        self.sites_Acp_InputAV.setMaximumSize(QSize(16777215, 16777215))
        self.sites_Acp_InputAV.setFont(font1)
        self.sites_Acp_InputAV.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;border-radius:10px;\n"
"")
        self.sites_Acp_InputAV.setDragEnabled(True)

        self.horizontalLayout_46.addWidget(self.sites_Acp_InputAV)


        self.verticalLayout_50.addWidget(self.frame_77)


        self.verticalLayout_26.addWidget(self.frame_76)

        self.frame_75 = QFrame(self.asabaAV_page)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_45.setSpacing(20)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.genACPBtnAV = QPushButton(self.frame_75)
        self.genACPBtnAV.setObjectName(u"genACPBtnAV")
        sizePolicy6.setHeightForWidth(self.genACPBtnAV.sizePolicy().hasHeightForWidth())
        self.genACPBtnAV.setSizePolicy(sizePolicy6)
        self.genACPBtnAV.setMinimumSize(QSize(300, 150))
        self.genACPBtnAV.setFont(font1)

        self.horizontalLayout_45.addWidget(self.genACPBtnAV)

        self.genACSBtnAV = QPushButton(self.frame_75)
        self.genACSBtnAV.setObjectName(u"genACSBtnAV")
        sizePolicy6.setHeightForWidth(self.genACSBtnAV.sizePolicy().hasHeightForWidth())
        self.genACSBtnAV.setSizePolicy(sizePolicy6)
        self.genACSBtnAV.setMinimumSize(QSize(300, 150))
        self.genACSBtnAV.setFont(font1)

        self.horizontalLayout_45.addWidget(self.genACSBtnAV)


        self.verticalLayout_26.addWidget(self.frame_75)

        self.mainPages.addWidget(self.asabaAV_page)
        self.enuguAV_page = QWidget()
        self.enuguAV_page.setObjectName(u"enuguAV_page")
        self.verticalLayout_27 = QVBoxLayout(self.enuguAV_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_78 = QFrame(self.enuguAV_page)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_78)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_20 = QFrame(self.frame_78)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.backEBtnAV = QPushButton(self.frame_20)
        self.backEBtnAV.setObjectName(u"backEBtnAV")
        sizePolicy6.setHeightForWidth(self.backEBtnAV.sizePolicy().hasHeightForWidth())
        self.backEBtnAV.setSizePolicy(sizePolicy6)
        self.backEBtnAV.setIcon(icon21)
        self.backEBtnAV.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.backEBtnAV)

        self.label_67 = QLabel(self.frame_20)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font2)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_67)


        self.verticalLayout_52.addWidget(self.frame_20)

        self.label_68 = QLabel(self.frame_78)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font2)
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_68, 0, Qt.AlignLeft)

        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        sizePolicy8.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy8)
        self.frame_79.setMinimumSize(QSize(500, 0))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_69 = QLabel(self.frame_79)
        self.label_69.setObjectName(u"label_69")
        sizePolicy8.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy8)
        self.label_69.setMinimumSize(QSize(50, 0))
        self.label_69.setFont(font5)
        self.label_69.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius:10px;")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_69)

        self.sites_Ecp_InputAV = QLineEdit(self.frame_79)
        self.sites_Ecp_InputAV.setObjectName(u"sites_Ecp_InputAV")
        sizePolicy9.setHeightForWidth(self.sites_Ecp_InputAV.sizePolicy().hasHeightForWidth())
        self.sites_Ecp_InputAV.setSizePolicy(sizePolicy9)
        self.sites_Ecp_InputAV.setFont(font1)
        self.sites_Ecp_InputAV.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;border-radius:10px;\n"
"")
        self.sites_Ecp_InputAV.setDragEnabled(True)

        self.horizontalLayout_47.addWidget(self.sites_Ecp_InputAV)


        self.verticalLayout_52.addWidget(self.frame_79)


        self.verticalLayout_27.addWidget(self.frame_78)

        self.frame_80 = QFrame(self.enuguAV_page)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_80)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_48.setSpacing(20)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.genECPBtnAV = QPushButton(self.frame_81)
        self.genECPBtnAV.setObjectName(u"genECPBtnAV")
        sizePolicy6.setHeightForWidth(self.genECPBtnAV.sizePolicy().hasHeightForWidth())
        self.genECPBtnAV.setSizePolicy(sizePolicy6)
        self.genECPBtnAV.setMinimumSize(QSize(300, 150))
        self.genECPBtnAV.setFont(font1)

        self.horizontalLayout_48.addWidget(self.genECPBtnAV)

        self.genECSBtnAV = QPushButton(self.frame_81)
        self.genECSBtnAV.setObjectName(u"genECSBtnAV")
        sizePolicy6.setHeightForWidth(self.genECSBtnAV.sizePolicy().hasHeightForWidth())
        self.genECSBtnAV.setSizePolicy(sizePolicy6)
        self.genECSBtnAV.setMinimumSize(QSize(300, 150))
        self.genECSBtnAV.setFont(font1)

        self.horizontalLayout_48.addWidget(self.genECSBtnAV)


        self.gridLayout_15.addWidget(self.frame_81, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_80)

        self.mainPages.addWidget(self.enuguAV_page)
        self.kanoAV_page = QWidget()
        self.kanoAV_page.setObjectName(u"kanoAV_page")
        self.verticalLayout_28 = QVBoxLayout(self.kanoAV_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_84 = QFrame(self.kanoAV_page)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_84)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_21 = QFrame(self.frame_84)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.backKBtnAV = QPushButton(self.frame_21)
        self.backKBtnAV.setObjectName(u"backKBtnAV")
        sizePolicy6.setHeightForWidth(self.backKBtnAV.sizePolicy().hasHeightForWidth())
        self.backKBtnAV.setSizePolicy(sizePolicy6)
        self.backKBtnAV.setIcon(icon21)
        self.backKBtnAV.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.backKBtnAV)

        self.label_70 = QLabel(self.frame_21)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font2)
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_70)


        self.verticalLayout_54.addWidget(self.frame_21)

        self.label_71 = QLabel(self.frame_84)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font2)
        self.label_71.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_71, 0, Qt.AlignLeft)

        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy8.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy8)
        self.frame_85.setMinimumSize(QSize(500, 0))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_72 = QLabel(self.frame_85)
        self.label_72.setObjectName(u"label_72")
        sizePolicy8.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy8)
        self.label_72.setMinimumSize(QSize(50, 0))
        self.label_72.setFont(font5)
        self.label_72.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_72)

        self.sites_Kcp_InputAV = QLineEdit(self.frame_85)
        self.sites_Kcp_InputAV.setObjectName(u"sites_Kcp_InputAV")
        sizePolicy9.setHeightForWidth(self.sites_Kcp_InputAV.sizePolicy().hasHeightForWidth())
        self.sites_Kcp_InputAV.setSizePolicy(sizePolicy9)
        self.sites_Kcp_InputAV.setFont(font1)
        self.sites_Kcp_InputAV.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")
        self.sites_Kcp_InputAV.setDragEnabled(True)

        self.horizontalLayout_50.addWidget(self.sites_Kcp_InputAV)


        self.verticalLayout_54.addWidget(self.frame_85)


        self.verticalLayout_28.addWidget(self.frame_84)

        self.frame_82 = QFrame(self.kanoAV_page)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_82)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_49.setSpacing(20)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.genKCPBtnAV = QPushButton(self.frame_83)
        self.genKCPBtnAV.setObjectName(u"genKCPBtnAV")
        sizePolicy6.setHeightForWidth(self.genKCPBtnAV.sizePolicy().hasHeightForWidth())
        self.genKCPBtnAV.setSizePolicy(sizePolicy6)
        self.genKCPBtnAV.setMinimumSize(QSize(300, 150))
        self.genKCPBtnAV.setFont(font1)

        self.horizontalLayout_49.addWidget(self.genKCPBtnAV)

        self.genKCSBtnAV = QPushButton(self.frame_83)
        self.genKCSBtnAV.setObjectName(u"genKCSBtnAV")
        sizePolicy6.setHeightForWidth(self.genKCSBtnAV.sizePolicy().hasHeightForWidth())
        self.genKCSBtnAV.setSizePolicy(sizePolicy6)
        self.genKCSBtnAV.setMinimumSize(QSize(300, 150))
        self.genKCSBtnAV.setFont(font1)

        self.horizontalLayout_49.addWidget(self.genKCSBtnAV)


        self.gridLayout_16.addWidget(self.frame_83, 0, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_82)

        self.mainPages.addWidget(self.kanoAV_page)
        self.owerriAV_page = QWidget()
        self.owerriAV_page.setObjectName(u"owerriAV_page")
        self.verticalLayout_29 = QVBoxLayout(self.owerriAV_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_86 = QFrame(self.owerriAV_page)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_86)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_22 = QFrame(self.frame_86)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.backOBtnAV = QPushButton(self.frame_22)
        self.backOBtnAV.setObjectName(u"backOBtnAV")
        sizePolicy6.setHeightForWidth(self.backOBtnAV.sizePolicy().hasHeightForWidth())
        self.backOBtnAV.setSizePolicy(sizePolicy6)
        self.backOBtnAV.setIcon(icon21)
        self.backOBtnAV.setIconSize(QSize(24, 24))

        self.horizontalLayout_22.addWidget(self.backOBtnAV)

        self.label_73 = QLabel(self.frame_22)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font2)
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_73)


        self.verticalLayout_56.addWidget(self.frame_22)

        self.label_74 = QLabel(self.frame_86)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font2)
        self.label_74.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_74, 0, Qt.AlignLeft)

        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        sizePolicy8.setHeightForWidth(self.frame_87.sizePolicy().hasHeightForWidth())
        self.frame_87.setSizePolicy(sizePolicy8)
        self.frame_87.setMinimumSize(QSize(500, 0))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_75 = QLabel(self.frame_87)
        self.label_75.setObjectName(u"label_75")
        sizePolicy8.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy8)
        self.label_75.setMinimumSize(QSize(50, 0))
        self.label_75.setFont(font5)
        self.label_75.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"border-radius:10px;")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_75)

        self.sites_Ocp_InputAV = QLineEdit(self.frame_87)
        self.sites_Ocp_InputAV.setObjectName(u"sites_Ocp_InputAV")
        sizePolicy9.setHeightForWidth(self.sites_Ocp_InputAV.sizePolicy().hasHeightForWidth())
        self.sites_Ocp_InputAV.setSizePolicy(sizePolicy9)
        self.sites_Ocp_InputAV.setFont(font1)
        self.sites_Ocp_InputAV.setStyleSheet(u"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"border-radius:10px;")
        self.sites_Ocp_InputAV.setDragEnabled(True)

        self.horizontalLayout_51.addWidget(self.sites_Ocp_InputAV)


        self.verticalLayout_56.addWidget(self.frame_87)


        self.verticalLayout_29.addWidget(self.frame_86)

        self.frame_88 = QFrame(self.owerriAV_page)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_88)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_52.setSpacing(20)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.genOCPBtnAV = QPushButton(self.frame_89)
        self.genOCPBtnAV.setObjectName(u"genOCPBtnAV")
        sizePolicy6.setHeightForWidth(self.genOCPBtnAV.sizePolicy().hasHeightForWidth())
        self.genOCPBtnAV.setSizePolicy(sizePolicy6)
        self.genOCPBtnAV.setMinimumSize(QSize(300, 150))
        self.genOCPBtnAV.setFont(font1)

        self.horizontalLayout_52.addWidget(self.genOCPBtnAV)

        self.genOCSBtnAV = QPushButton(self.frame_89)
        self.genOCSBtnAV.setObjectName(u"genOCSBtnAV")
        sizePolicy6.setHeightForWidth(self.genOCSBtnAV.sizePolicy().hasHeightForWidth())
        self.genOCSBtnAV.setSizePolicy(sizePolicy6)
        self.genOCSBtnAV.setMinimumSize(QSize(300, 150))
        self.genOCSBtnAV.setFont(font1)

        self.horizontalLayout_52.addWidget(self.genOCSBtnAV)


        self.gridLayout_17.addWidget(self.frame_89, 0, 0, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_88)

        self.mainPages.addWidget(self.owerriAV_page)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 0, 0)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon8)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QCustomSlideMenu()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font11 = QFont()
        font11.setFamily(u"Segoe Print")
        font11.setPointSize(9)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_14.setFont(font11)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.notificationMssg = QLabel(self.frame_9)
        self.notificationMssg.setObjectName(u"notificationMssg")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.notificationMssg.sizePolicy().hasHeightForWidth())
        self.notificationMssg.setSizePolicy(sizePolicy12)
        self.notificationMssg.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setFamily(u"Segoe Print")
        font12.setBold(True)
        font12.setWeight(75)
        self.notificationMssg.setFont(font12)
        self.notificationMssg.setTextFormat(Qt.AutoText)
        self.notificationMssg.setAlignment(Qt.AlignCenter)
        self.notificationMssg.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.notificationMssg)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon22)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.genBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Generate scripts", None))
#endif // QT_CONFIG(tooltip)
        self.genBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Script", None))
#if QT_CONFIG(tooltip)
        self.regionsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Available Regions", None))
#endif // QT_CONFIG(tooltip)
        self.regionsBtn.setText(QCoreApplication.translate("MainWindow", u"Regions", None))
#if QT_CONFIG(tooltip)
        self.scriptsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Generated Scripts", None))
#endif // QT_CONFIG(tooltip)
        self.scriptsBtn.setText(QCoreApplication.translate("MainWindow", u"Scripts", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.securityBtn.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.verification.setText(QCoreApplication.translate("MainWindow", u"Verification", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Referrals", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"API", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textEdit_3.setMarkdown(QCoreApplication.translate("MainWindow", u"**TelescriptGenius**\n"
"\n"
"`Scripting Simplicity, Genius Complexity`\n"
"\n"
"Get Help from us by getting in contact from any of our social media platform.\n"
"\n"
"MIT License\n"
"\n"
"**Email: oyebodefawaz2020@gmail.com**\n"
"\n"
"**Created by: Fawaz H. Oyebode**\n"
"\n"
"**Script Generator PC App **\n"
"\n"
"", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Print'; font-size:16pt; font-weight:600; color:#0000ff;\">TelescriptGenius</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','monospace'; font-size:9.8pt; color:#c9c9d1; background-color:#1d1d26;\">Scripting Simplicity, Genius Complexity</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">Get Help from us by getting in contact from any of our social media platform.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#432498;\">Email: oyebodefawaz2020@gmail.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#bd93f9;\">Created by: Fawaz H. Oyebode</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0000ff;\">Script Generator PC App</span><span style=\" font-weight:600; color:#ee208b;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Informtion", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**TelescriptGenius**\n"
"\n"
"`Scripting Simplicity, Genius Complexity`\n"
"\n"
"An interface created using Python, PyQt5 and PySide (support for PyQt). The PC\n"
"Application features script generation based on available regions and has up to\n"
"3 different scripts templates.There are also plans to include Link Check\n"
"feature and some other features to improve Telecom workspace.\n"
"\n"
"MIT License\n"
"\n"
"**Created by: Fawaz H. Oyebode**\n"
"\n"
"**Script Generator PC App **\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Print'; font-size:16pt; font-weight:600; color:#0000ff;\">TelescriptGenius</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','monospace'; font-size:9.8pt; color:#c9c9d1; background-color:#1d1d26;\">Scripting Simplicity, Genius Complexity</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">An interface created using Python, PyQt5 and PySide (support for PyQt). The PC Application features script generation based on available regions and has up to 3 different scripts templates.There are also plans to include Link Check feature and some other features to improve Telecom workspace.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#bd93f9;\">Created by: Fawaz H. Oyebode</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-weight:600; color:#0000ff;\">Script Generator PC App </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.app_icon.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TeleScriptGenius", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_window_btn.setText("")
#if QT_CONFIG(tooltip)
        self.restore_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restore_window_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.close_window_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Unleash Your Creativity with Intelligent Script Generation", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"STEPS TO GENERATE NEW SCRIPT", None))
        self.pushButton_4.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Click on Get Started Button to begin process of script generation", None))
        self.pushButton_5.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Click on your preferred script template you would like to generate", None))
        self.pushButton_6.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Click on the region you would like like to create script for", None))
        self.pushButton_7.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Type in the CP_ID", None))
        self.pushButton_8.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Click on CP Script or CS script Button to create your scripts", None))
        self.pushButton_10.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Wow !!! You have now successfully created a scripts ", None))
#if QT_CONFIG(tooltip)
        self.getStartBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Generate your scripts now", None))
#endif // QT_CONFIG(tooltip)
        self.getStartBtn.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.label_13.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Online Support", None))
        self.label_27.setText("")
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"View Recently Generated scripts here", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quick Access", None))
#if QT_CONFIG(tooltip)
        self.copyBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Browse", None))
#endif // QT_CONFIG(tooltip)
        self.copyBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Available Regions", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Africa", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nigeria", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Asaba", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Enugu", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Kano", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Owerri", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Scripts Templates", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Choose preferred templates below:", None))
        self.ml10GBtn.setText(QCoreApplication.translate("MainWindow", u"ML10G ML scripts", None))
        self.routerBtn.setText(QCoreApplication.translate("MainWindow", u"Router scripts", None))
        self.aviatBtn.setText(QCoreApplication.translate("MainWindow", u"Aviat Scripts", None))
        self.linkBtn.setText(QCoreApplication.translate("MainWindow", u"Link Check", None))
        self.backrsBtn.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Coming Soon.....", None))
        self.backlcBtn.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Coming Soon.....", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Generated Scripts", None))
        self.view_script.setText(QCoreApplication.translate("MainWindow", u"View Scripts here", None))
        self.backRBtn.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ML10G Available Regions", None))
        self.aRegBtn.setText(QCoreApplication.translate("MainWindow", u"Asaba", None))
        self.eRegBtn.setText(QCoreApplication.translate("MainWindow", u"Enugu", None))
        self.kRegBtn.setText(QCoreApplication.translate("MainWindow", u"Kano", None))
        self.oRegBtn.setText(QCoreApplication.translate("MainWindow", u"Owerri", None))
        self.backAVRBtn.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Aviat Available Regions", None))
        self.aRegBtnAV.setText(QCoreApplication.translate("MainWindow", u"Asaba", None))
        self.eRegBtnAV.setText(QCoreApplication.translate("MainWindow", u"Enugu", None))
        self.kRegBtnAV.setText(QCoreApplication.translate("MainWindow", u"Kano", None))
        self.oRegBtnAV.setText(QCoreApplication.translate("MainWindow", u"Owerri", None))
        self.backOBtn.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"ML10G for Owerri Region", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Ocp_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genOCPBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CP script", None))
        self.genOCSBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CS scripts", None))
        self.backKBtn.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"ML10G for Kano Region", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Kcp_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genKCPBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CP script", None))
        self.genKCSBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CS scripts", None))
        self.backEBtn.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"ML10G for Enugu Region", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Ecp_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genECPBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CP script", None))
        self.genECSBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CS scripts", None))
        self.backABtn.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"ML10G for Asaba Region", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Acp_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genACPBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CP script", None))
        self.genACSBtn.setText(QCoreApplication.translate("MainWindow", u"Generate ML10G CS scripts", None))
        self.backABtnAV.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Aviat for Asaba Region", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Acp_InputAV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genACPBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CP script", None))
        self.genACSBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CS scripts", None))
        self.backEBtnAV.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Aviat for Enugu Region", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Ecp_InputAV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genECPBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CP script", None))
        self.genECSBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CS scripts", None))
        self.backKBtnAV.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Aviat for Kano Region", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Kcp_InputAV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genKCPBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CP script", None))
        self.genKCSBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CS scripts", None))
        self.backOBtnAV.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Aviat for Owerri Region", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Creates preferred scripts below", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"CP ID", None))
        self.sites_Ocp_InputAV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter CP_ID here", None))
        self.genOCPBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CP script", None))
        self.genOCSBtnAV.setText(QCoreApplication.translate("MainWindow", u"Generate Aviat CS scripts", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More....", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.notificationMssg.setText(QCoreApplication.translate("MainWindow", u"Notification message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright Unreal Softwares", None))
    # retranslateUi

