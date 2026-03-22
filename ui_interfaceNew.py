# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceNewTgtILi.ui'
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
from clickanywherecombobox import ClickAnywhereComboBox

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 702)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(850, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icons/Telescript.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon1)
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
        self.dashboardBtn = QPushButton(self.frame_2)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        font = QFont()
        font.setFamily(u"Segoe Print")
        self.dashboardBtn.setFont(font)
        self.dashboardBtn.setStyleSheet(u"background-color:#1f232a;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboardBtn.setIcon(icon2)
        self.dashboardBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dashboardBtn)

        self.genBtn = QPushButton(self.frame_2)
        self.genBtn.setObjectName(u"genBtn")
        self.genBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.genBtn.setIcon(icon3)
        self.genBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.genBtn)

        self.linkBtn = QPushButton(self.frame_2)
        self.linkBtn.setObjectName(u"linkBtn")
        self.linkBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/radio.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.linkBtn.setIcon(icon4)
        self.linkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.linkBtn)

        self.settingBtn = QPushButton(self.frame_2)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon5)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.settingBtn)

        self.aboutBtn = QPushButton(self.frame_2)
        self.aboutBtn.setObjectName(u"aboutBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon6)
        self.aboutBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.aboutBtn)


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
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon7)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon8)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy3)
        self.app_icon.setMinimumSize(QSize(0, 0))
        self.app_icon.setIconSize(QSize(40, 30))

        self.horizontalLayout_7.addWidget(self.app_icon)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamily(u"Segoe Print")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon9)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon10)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon11)
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.minimize_window_btn)

        self.restore_window_btn = QPushButton(self.frame_7)
        self.restore_window_btn.setObjectName(u"restore_window_btn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_btn.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.restore_window_btn)

        self.close_window_btn = QPushButton(self.frame_7)
        self.close_window_btn.setObjectName(u"close_window_btn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.close_window_btn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QCustomSlideMenu(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy4)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setStyleSheet(u"QWidget {\n"
"    background-color: #0B0F14;\n"
"    color: #E6F1FF;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"background-color: #1f232a;")
        self.verticalLayout_16 = QVBoxLayout(self.home_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_16 = QFrame(self.home_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_16)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_32.addWidget(self.label_10)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_32.addWidget(self.label_5)


        self.verticalLayout_16.addWidget(self.frame_16, 0, Qt.AlignVCenter)

        self.widget_3 = QWidget(self.home_page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
        self.horizontalLayout_25 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.templates = QFrame(self.widget_3)
        self.templates.setObjectName(u"templates")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.templates.sizePolicy().hasHeightForWidth())
        self.templates.setSizePolicy(sizePolicy6)
        self.templates.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#templates{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.templates.setFrameShape(QFrame.StyledPanel)
        self.templates.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.templates)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_35 = QFrame(self.templates)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_13 = QLabel(self.frame_35)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_13.setFont(font3)

        self.horizontalLayout_27.addWidget(self.label_13)

        self.toolButton = QToolButton(self.frame_35)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setIcon(icon3)

        self.horizontalLayout_27.addWidget(self.toolButton)


        self.verticalLayout_34.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.templates)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_36)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_24 = QLabel(self.frame_36)
        self.label_24.setObjectName(u"label_24")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_24.setFont(font4)

        self.verticalLayout_44.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_36)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_44.addWidget(self.label_25)


        self.verticalLayout_34.addWidget(self.frame_36)


        self.horizontalLayout_25.addWidget(self.templates)

        self.regions = QFrame(self.widget_3)
        self.regions.setObjectName(u"regions")
        sizePolicy6.setHeightForWidth(self.regions.sizePolicy().hasHeightForWidth())
        self.regions.setSizePolicy(sizePolicy6)
        self.regions.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#regions{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.regions.setFrameShape(QFrame.StyledPanel)
        self.regions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.regions)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.frame_41 = QFrame(self.regions)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_34 = QLabel(self.frame_41)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.horizontalLayout_30.addWidget(self.label_34)

        self.toolButton_4 = QToolButton(self.frame_41)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setStyleSheet(u"background-color:(0, 236, 236);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/map-pin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon15)

        self.horizontalLayout_30.addWidget(self.toolButton_4)


        self.verticalLayout_61.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.regions)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_42)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_35 = QLabel(self.frame_42)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font4)

        self.verticalLayout_62.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_42)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_62.addWidget(self.label_36)


        self.verticalLayout_61.addWidget(self.frame_42)


        self.horizontalLayout_25.addWidget(self.regions)

        self.generated = QFrame(self.widget_3)
        self.generated.setObjectName(u"generated")
        sizePolicy6.setHeightForWidth(self.generated.sizePolicy().hasHeightForWidth())
        self.generated.setSizePolicy(sizePolicy6)
        self.generated.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#generated{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.generated.setFrameShape(QFrame.StyledPanel)
        self.generated.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.generated)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_39 = QFrame(self.generated)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_31 = QLabel(self.frame_39)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)

        self.horizontalLayout_29.addWidget(self.label_31)

        self.toolButton_3 = QToolButton(self.frame_39)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon16)

        self.horizontalLayout_29.addWidget(self.toolButton_3)


        self.verticalLayout_59.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.generated)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_40)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.totalgenerated = QLabel(self.frame_40)
        self.totalgenerated.setObjectName(u"totalgenerated")
        self.totalgenerated.setFont(font4)

        self.verticalLayout_60.addWidget(self.totalgenerated)

        self.label_33 = QLabel(self.frame_40)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_60.addWidget(self.label_33)


        self.verticalLayout_59.addWidget(self.frame_40)


        self.horizontalLayout_25.addWidget(self.generated)

        self.success = QFrame(self.widget_3)
        self.success.setObjectName(u"success")
        sizePolicy6.setHeightForWidth(self.success.sizePolicy().hasHeightForWidth())
        self.success.setSizePolicy(sizePolicy6)
        self.success.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#success{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.success.setFrameShape(QFrame.StyledPanel)
        self.success.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.success)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_37 = QFrame(self.success)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.frame_37)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.horizontalLayout_28.addWidget(self.label_26)

        self.toolButton_2 = QToolButton(self.frame_37)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/cloud-lightning.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon17)

        self.horizontalLayout_28.addWidget(self.toolButton_2)


        self.verticalLayout_57.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.success)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_38)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_27 = QLabel(self.frame_38)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font4)

        self.verticalLayout_58.addWidget(self.label_27)

        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_58.addWidget(self.label_30)


        self.verticalLayout_57.addWidget(self.frame_38)


        self.horizontalLayout_25.addWidget(self.success)


        self.verticalLayout_16.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.home_page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(True)
        font5.setWeight(75)
        self.widget_2.setFont(font5)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_18 = QFrame(self.widget_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.quick = QFrame(self.frame_18)
        self.quick.setObjectName(u"quick")
        sizePolicy1.setHeightForWidth(self.quick.sizePolicy().hasHeightForWidth())
        self.quick.setSizePolicy(sizePolicy1)
        self.quick.setFrameShape(QFrame.StyledPanel)
        self.quick.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.quick)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_25 = QFrame(self.quick)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setStyleSheet(u"QFrame#frame_25{\n"
"	border-radius: 12px;\n"
"	border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_25)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.genQuickBtn = QPushButton(self.frame_25)
        self.genQuickBtn.setObjectName(u"genQuickBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.genQuickBtn.sizePolicy().hasHeightForWidth())
        self.genQuickBtn.setSizePolicy(sizePolicy7)
        self.genQuickBtn.setFont(font3)
        self.genQuickBtn.setLayoutDirection(Qt.LeftToRight)
        self.genQuickBtn.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.genQuickBtn.setIcon(icon3)

        self.verticalLayout_22.addWidget(self.genQuickBtn)

        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_22.addWidget(self.label_12)


        self.verticalLayout_33.addWidget(self.frame_25)

        self.frame_4 = QFrame(self.quick)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy8)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_4{\n"
"	border-radius: 12px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFramet#frame_{\n"
"    background-color: #121826;\n"
"    border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(0, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy9)
        self.label_3.setMinimumSize(QSize(100, 20))
        self.label_3.setStyleSheet(u"background-color: rgba(115, 172, 172,150);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)

        self.verticalLayout_6.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_34 = QFrame(self.frame_4)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy10.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy10)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_34)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.startQuickBtn = QPushButton(self.frame_34)
        self.startQuickBtn.setObjectName(u"startQuickBtn")
        sizePolicy9.setHeightForWidth(self.startQuickBtn.sizePolicy().hasHeightForWidth())
        self.startQuickBtn.setSizePolicy(sizePolicy9)
        self.startQuickBtn.setMinimumSize(QSize(120, 35))
        self.startQuickBtn.setFont(font5)
        self.startQuickBtn.setLayoutDirection(Qt.RightToLeft)
        self.startQuickBtn.setStyleSheet(u"border-radius: 10px;\n"
"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.startQuickBtn.setIcon(icon18)

        self.verticalLayout_23.addWidget(self.startQuickBtn, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_34)


        self.verticalLayout_33.addWidget(self.frame_4)


        self.horizontalLayout_14.addWidget(self.quick)

        self.frame_44 = QFrame(self.frame_18)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy1.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy1)
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_44)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_19 = QFrame(self.frame_44)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setStyleSheet(u"QFrame#frame_19{\n"
"border-radius: 12px;\n"
"border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_19)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.linkQuickBtn = QPushButton(self.frame_19)
        self.linkQuickBtn.setObjectName(u"linkQuickBtn")
        sizePolicy7.setHeightForWidth(self.linkQuickBtn.sizePolicy().hasHeightForWidth())
        self.linkQuickBtn.setSizePolicy(sizePolicy7)
        self.linkQuickBtn.setFont(font3)
        self.linkQuickBtn.setLayoutDirection(Qt.LeftToRight)
        self.linkQuickBtn.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.linkQuickBtn.setIcon(icon4)

        self.verticalLayout_24.addWidget(self.linkQuickBtn)

        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_24.addWidget(self.label_4)


        self.verticalLayout_18.addWidget(self.frame_19)

        self.frame_27 = QFrame(self.frame_44)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_27{\n"
"	border-radius: 12px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_20 = QFrame(self.frame_27)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_22 = QLabel(self.frame_20)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_22)

        self.label_28 = QLabel(self.frame_20)
        self.label_28.setObjectName(u"label_28")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setUnderline(True)
        self.label_28.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_20)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_29)

        self.label_37 = QLabel(self.frame_20)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_37)


        self.horizontalLayout_13.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_27)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_38 = QLabel(self.frame_21)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_21)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font6)
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.label_39)

        self.label_41 = QLabel(self.frame_21)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font6)
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font6)
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.label_42)


        self.horizontalLayout_13.addWidget(self.frame_21)


        self.verticalLayout_18.addWidget(self.frame_27)


        self.horizontalLayout_14.addWidget(self.frame_44)


        self.horizontalLayout_23.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.widget_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_17)


        self.verticalLayout_16.addWidget(self.widget_2)

        self.frame_11 = QFrame(self.home_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_11)

        self.mainPages.addWidget(self.home_page)
        self.generator_page = QWidget()
        self.generator_page.setObjectName(u"generator_page")
        sizePolicy1.setHeightForWidth(self.generator_page.sizePolicy().hasHeightForWidth())
        self.generator_page.setSizePolicy(sizePolicy1)
        self.generator_page.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_31 = QVBoxLayout(self.generator_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_11 = QLabel(self.generator_page)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_31.addWidget(self.label_11, 0, Qt.AlignTop)

        self.label_23 = QLabel(self.generator_page)
        self.label_23.setObjectName(u"label_23")
        sizePolicy6.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy6)
        self.label_23.setMinimumSize(QSize(0, 10))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_23.setFont(font7)

        self.verticalLayout_31.addWidget(self.label_23)

        self.frame_23 = QFrame(self.generator_page)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy11)
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setStyleSheet(u"background-color: transparent;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_12 = QFrame(self.frame_23)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy12)
        self.frame_12.setMinimumSize(QSize(300, 300))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_12{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        sizePolicy13 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy13)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_16.setFont(font8)

        self.verticalLayout_7.addWidget(self.label_16)

        self.regionFrame = QFrame(self.frame_12)
        self.regionFrame.setObjectName(u"regionFrame")
        sizePolicy9.setHeightForWidth(self.regionFrame.sizePolicy().hasHeightForWidth())
        self.regionFrame.setSizePolicy(sizePolicy9)
        self.regionFrame.setFrameShape(QFrame.StyledPanel)
        self.regionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.regionFrame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.regionLabel = QLabel(self.regionFrame)
        self.regionLabel.setObjectName(u"regionLabel")
        sizePolicy5.setHeightForWidth(self.regionLabel.sizePolicy().hasHeightForWidth())
        self.regionLabel.setSizePolicy(sizePolicy5)
        self.regionLabel.setMinimumSize(QSize(0, 30))
        self.regionLabel.setFont(font5)

        self.verticalLayout_41.addWidget(self.regionLabel)

        self.regionBox = ClickAnywhereComboBox(self.regionFrame)
        self.regionBox.addItem("")
        self.regionBox.addItem("")
        self.regionBox.addItem("")
        self.regionBox.addItem("")
        self.regionBox.setObjectName(u"regionBox")
        sizePolicy9.setHeightForWidth(self.regionBox.sizePolicy().hasHeightForWidth())
        self.regionBox.setSizePolicy(sizePolicy9)
        self.regionBox.setMinimumSize(QSize(300, 30))
        self.regionBox.setStyleSheet(u"/* COMBOBOX BASE */\n"
"QComboBox {\n"
"    background-color: rgba(15, 20, 30, 220);\n"
"    border: 1px solid rgba(0, 229, 255, 80);\n"
"    border-radius: 14px;\n"
"    padding: 8px 14px;\n"
"    color: #E6F9FF;\n"
"}\n"
"\n"
"/* REMOVE DEFAULT ARROW */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"/* DROPDOWN LIST */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(10, 14, 20, 245);\n"
"    border-radius: 14px;\n"
"    padding: 6px;\n"
"    selection-background-color: rgba(0, 229, 255, 60);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* INDIVIDUAL ITEMS */\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 36px;\n"
"    border-radius: 10px;\n"
"    padding-left: 12px;\n"
"    color: #E6F9FF;\n"
"}\n"
"\n"
"/* HOVER EFFECT */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(0, 229, 255, 50);\n"
"}\n"
"\n"
"/* SELECTED ITEM */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgba(0, 229, 255, 80);\n"
"}\n"
"")
        self.regionBox.setEditable(True)

        self.verticalLayout_41.addWidget(self.regionBox)


        self.verticalLayout_7.addWidget(self.regionFrame)

        self.tempFrame = QFrame(self.frame_12)
        self.tempFrame.setObjectName(u"tempFrame")
        sizePolicy9.setHeightForWidth(self.tempFrame.sizePolicy().hasHeightForWidth())
        self.tempFrame.setSizePolicy(sizePolicy9)
        self.tempFrame.setFrameShape(QFrame.StyledPanel)
        self.tempFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.tempFrame)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.tempLabel = QLabel(self.tempFrame)
        self.tempLabel.setObjectName(u"tempLabel")
        sizePolicy5.setHeightForWidth(self.tempLabel.sizePolicy().hasHeightForWidth())
        self.tempLabel.setSizePolicy(sizePolicy5)
        self.tempLabel.setMinimumSize(QSize(0, 30))
        self.tempLabel.setFont(font5)

        self.verticalLayout_46.addWidget(self.tempLabel)

        self.tempBox = ClickAnywhereComboBox(self.tempFrame)
        self.tempBox.addItem("")
        self.tempBox.addItem("")
        self.tempBox.addItem("")
        self.tempBox.addItem("")
        self.tempBox.addItem("")
        self.tempBox.setObjectName(u"tempBox")
        sizePolicy9.setHeightForWidth(self.tempBox.sizePolicy().hasHeightForWidth())
        self.tempBox.setSizePolicy(sizePolicy9)
        self.tempBox.setMinimumSize(QSize(300, 30))
        self.tempBox.setStyleSheet(u"/* COMBOBOX BASE */\n"
"QComboBox {\n"
"    background-color: rgba(15, 20, 30, 220);\n"
"    border: 1px solid rgba(0, 229, 255, 80);\n"
"    border-radius: 14px;\n"
"    padding: 8px 14px;\n"
"    color: #E6F9FF;\n"
"}\n"
"\n"
"/* REMOVE DEFAULT ARROW */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"/* DROPDOWN LIST */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(10, 14, 20, 245);\n"
"    border-radius: 14px;\n"
"    padding: 6px;\n"
"    selection-background-color: rgba(0, 229, 255, 60);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* INDIVIDUAL ITEMS */\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 36px;\n"
"    border-radius: 10px;\n"
"    padding-left: 12px;\n"
"    color: #E6F9FF;\n"
"}\n"
"\n"
"/* HOVER EFFECT */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(0, 229, 255, 50);\n"
"}\n"
"\n"
"/* SELECTED ITEM */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgba(0, 229, 255, 80);\n"
"}\n"
"")
        self.tempBox.setEditable(True)

        self.verticalLayout_46.addWidget(self.tempBox)


        self.verticalLayout_7.addWidget(self.tempFrame)

        self.siteFrame = QFrame(self.frame_12)
        self.siteFrame.setObjectName(u"siteFrame")
        sizePolicy9.setHeightForWidth(self.siteFrame.sizePolicy().hasHeightForWidth())
        self.siteFrame.setSizePolicy(sizePolicy9)
        self.siteFrame.setFrameShape(QFrame.StyledPanel)
        self.siteFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.siteFrame)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.siteLabel = QLabel(self.siteFrame)
        self.siteLabel.setObjectName(u"siteLabel")
        sizePolicy5.setHeightForWidth(self.siteLabel.sizePolicy().hasHeightForWidth())
        self.siteLabel.setSizePolicy(sizePolicy5)
        self.siteLabel.setFont(font5)

        self.verticalLayout_40.addWidget(self.siteLabel)

        self.sitename = QLineEdit(self.siteFrame)
        self.sitename.setObjectName(u"sitename")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.sitename.sizePolicy().hasHeightForWidth())
        self.sitename.setSizePolicy(sizePolicy14)
        self.sitename.setMinimumSize(QSize(300, 40))
        self.sitename.setStyleSheet(u"/* Combo box container */\n"
"#sitename {\n"
"    border: 2px solid rgb(88, 88, 88);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* Line edit inside combo box (placeholder text) */\n"
"#sitename QLineEdit {\n"
"    color: rgb(200, 200, 200);  /* light gray text for placeholder */\n"
"    padding-left: 6px;           /* optional: nice padding */\n"
"}\n"
"")

        self.verticalLayout_40.addWidget(self.sitename)


        self.verticalLayout_7.addWidget(self.siteFrame)

        self.generateBtn = QPushButton(self.frame_12)
        self.generateBtn.setObjectName(u"generateBtn")
        sizePolicy12.setHeightForWidth(self.generateBtn.sizePolicy().hasHeightForWidth())
        self.generateBtn.setSizePolicy(sizePolicy12)
        self.generateBtn.setMinimumSize(QSize(300, 30))
        self.generateBtn.setFont(font5)
        self.generateBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #00E5FF;\n"
"    color: #000;\n"
"    border-radius: 14px;\n"
"    padding: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1FF7FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #00B8CC;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.generateBtn)


        self.horizontalLayout_32.addWidget(self.frame_12)

        self.widget_5 = QWidget(self.frame_23)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy15 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy15)
        self.widget_5.setMinimumSize(QSize(0, 300))
        self.verticalLayout_45 = QVBoxLayout(self.widget_5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy16)
        self.label_17.setFont(font5)

        self.verticalLayout_45.addWidget(self.label_17)

        self.textEdit_2 = QTextEdit(self.widget_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy7.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy7)
        self.textEdit_2.setMinimumSize(QSize(300, 250))
        self.textEdit_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(20, 24, 31);\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")

        self.verticalLayout_45.addWidget(self.textEdit_2)


        self.horizontalLayout_32.addWidget(self.widget_5)


        self.verticalLayout_31.addWidget(self.frame_23)

        self.mainPages.addWidget(self.generator_page)
        self.link_page = QWidget()
        self.link_page.setObjectName(u"link_page")
        self.verticalLayout_66 = QVBoxLayout(self.link_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_46 = QFrame(self.link_page)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_46)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.backlcBtn = QCheckBox(self.frame_46)
        self.backlcBtn.setObjectName(u"backlcBtn")
        sizePolicy9.setHeightForWidth(self.backlcBtn.sizePolicy().hasHeightForWidth())
        self.backlcBtn.setSizePolicy(sizePolicy9)
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backlcBtn.setIcon(icon19)
        self.backlcBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_68.addWidget(self.backlcBtn)


        self.verticalLayout_66.addWidget(self.frame_46)

        self.label_40 = QLabel(self.link_page)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setFont(font2)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_40)

        self.mainPages.addWidget(self.link_page)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        sizePolicy1.setHeightForWidth(self.settingsPage.sizePolicy().hasHeightForWidth())
        self.settingsPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.settingsPage)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_14)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_29 = QFrame(self.frame_14)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_44 = QLabel(self.frame_29)
        self.label_44.setObjectName(u"label_44")
        sizePolicy17 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy17)
        self.label_44.setPixmap(QPixmap(u":/icons/icons/settings.svg"))

        self.horizontalLayout_3.addWidget(self.label_44)

        self.label_19 = QLabel(self.frame_29)
        self.label_19.setObjectName(u"label_19")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_19.setFont(font9)

        self.horizontalLayout_3.addWidget(self.label_19)


        self.verticalLayout_21.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_14)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_30)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_18 = QLabel(self.frame_30)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_26.addWidget(self.label_18)


        self.verticalLayout_21.addWidget(self.frame_30)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.settingsPage)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy6.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy6)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy10.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy10)
        self.frame_22.setMinimumSize(QSize(500, 0))
        self.frame_22.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_22{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_22)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_31 = QFrame(self.frame_22)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_31)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_45 = QLabel(self.frame_31)
        self.label_45.setObjectName(u"label_45")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy18)
        self.label_45.setFont(font8)

        self.verticalLayout_36.addWidget(self.label_45)


        self.verticalLayout_27.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_22)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy6.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy6)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_32)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_21 = QLabel(self.frame_32)
        self.label_21.setObjectName(u"label_21")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(7)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_21.setFont(font10)

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_32)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy9.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy9)
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/toggle-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon20)
        self.pushButton_3.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.label_43 = QLabel(self.frame_32)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_2.addWidget(self.label_43, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_32)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy10.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy10)
        self.frame_26.setMinimumSize(QSize(500, 0))
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_26{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_26)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_20 = QLabel(self.frame_26)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font8)

        self.verticalLayout_29.addWidget(self.label_20)

        self.frame_24 = QFrame(self.frame_26)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_24)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chooseSaveLocation = QPushButton(self.frame_24)
        self.chooseSaveLocation.setObjectName(u"chooseSaveLocation")
        sizePolicy9.setHeightForWidth(self.chooseSaveLocation.sizePolicy().hasHeightForWidth())
        self.chooseSaveLocation.setSizePolicy(sizePolicy9)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chooseSaveLocation.setIcon(icon21)
        self.chooseSaveLocation.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.chooseSaveLocation, 1, 0, 1, 1)

        self.label_49 = QLabel(self.frame_24)
        self.label_49.setObjectName(u"label_49")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(7)
        self.label_49.setFont(font11)

        self.gridLayout.addWidget(self.label_49, 3, 1, 1, 1)

        self.label_46 = QLabel(self.frame_24)
        self.label_46.setObjectName(u"label_46")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        self.label_46.setFont(font12)

        self.gridLayout.addWidget(self.label_46, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_24)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"border-radius: 12px;")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_24)


        self.verticalLayout_17.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_15)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy10.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy10)
        self.frame_28.setMinimumSize(QSize(500, 0))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_28{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_28)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_45 = QFrame(self.frame_28)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_45)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_48 = QLabel(self.frame_45)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font8)

        self.verticalLayout_28.addWidget(self.label_48)


        self.verticalLayout_30.addWidget(self.frame_45)

        self.frame_47 = QFrame(self.frame_28)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_47)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_3.addWidget(self.label_51, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_47)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy9.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy9)
        self.pushButton.setIcon(icon20)
        self.pushButton.setIconSize(QSize(28, 28))

        self.gridLayout_3.addWidget(self.pushButton, 0, 3, 1, 1)

        self.label_50 = QLabel(self.frame_47)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_3.addWidget(self.label_50, 0, 1, 1, 1)

        self.label_52 = QLabel(self.frame_47)
        self.label_52.setObjectName(u"label_52")
        sizePolicy9.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy9)
        self.label_52.setPixmap(QPixmap(u":/icons/icons/bell.svg"))

        self.gridLayout_3.addWidget(self.label_52, 0, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_47)


        self.verticalLayout_17.addWidget(self.frame_28)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_48 = QFrame(self.settingsPage)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy6.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy6)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_48)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.pushButton_2 = QPushButton(self.frame_48)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy9.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy9)
        self.pushButton_2.setMinimumSize(QSize(100, 40))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;")

        self.verticalLayout_35.addWidget(self.pushButton_2)


        self.verticalLayout_8.addWidget(self.frame_48)

        self.mainPages.addWidget(self.settingsPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.verticalLayout_37 = QVBoxLayout(self.aboutPage)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.heroCard = QFrame(self.aboutPage)
        self.heroCard.setObjectName(u"heroCard")
        sizePolicy16.setHeightForWidth(self.heroCard.sizePolicy().hasHeightForWidth())
        self.heroCard.setSizePolicy(sizePolicy16)
        self.heroCard.setMinimumSize(QSize(0, 300))
        self.heroCard.setStyleSheet(u"/* HERO CARD */\n"
"QFrame#heroCard {\n"
"    background-color: qradialgradient(\n"
"        cx:0.25, cy:0.2, radius:1.1,\n"
"        fx:0.25, fy:0.2,\n"
"        stop:0 rgba(0, 229, 255, 35),\n"
"        stop:0.35 rgba(12, 18, 28, 215),\n"
"        stop:1 rgba(10, 14, 20, 235)\n"
"    );\n"
"\n"
"    border-radius: 22px;\n"
"    border: 1px solid rgba(0, 229, 255, 70);\n"
"}\n"
"\n"
"/* ALL LABELS INSIDE HERO CARD */\n"
"QFrame#heroCard QLabel {\n"
"    background: transparent;\n"
"    color: #E6F9FF;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* TITLE LABEL */\n"
"QFrame#heroCard QLabel#heroTitle {\n"
"    color: #00E5FF;\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"/* SUBTITLE / VERSION */\n"
"QFrame#heroCard QLabel#heroSub {\n"
"    color: rgba(200, 255, 255, 160);\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* PARAGRAPH TEXT */\n"
"QFrame#heroCard QLabel#heroText {\n"
"    color: rgba(220, 240, 255, 180);\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.heroCard.setFrameShape(QFrame.StyledPanel)
        self.heroCard.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.heroCard)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_56 = QLabel(self.heroCard)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_4.addWidget(self.label_56, 2, 1, 1, 1)

        self.label_54 = QLabel(self.heroCard)
        self.label_54.setObjectName(u"label_54")
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(8)
        font13.setBold(True)
        font13.setWeight(62)
        self.label_54.setFont(font13)

        self.gridLayout_4.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_55 = QLabel(self.heroCard)
        self.label_55.setObjectName(u"label_55")
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(10)
        font14.setBold(True)
        font14.setWeight(62)
        self.label_55.setFont(font14)

        self.gridLayout_4.addWidget(self.label_55, 1, 1, 1, 1)

        self.label_53 = QLabel(self.heroCard)
        self.label_53.setObjectName(u"label_53")
        sizePolicy9.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy9)
        self.label_53.setMinimumSize(QSize(40, 40))
        self.label_53.setPixmap(QPixmap(u":/icons/icons/zap.svg"))
        self.label_53.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_53, 0, 0, 1, 1)


        self.verticalLayout_37.addWidget(self.heroCard)

        self.frame_33 = QFrame(self.aboutPage)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy15.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy15)
        self.frame_33.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_49 = QFrame(self.frame_33)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy14.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy14)
        self.frame_49.setMinimumSize(QSize(0, 100))
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_49{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_49)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_57 = QLabel(self.frame_49)
        self.label_57.setObjectName(u"label_57")
        sizePolicy6.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy6)
        self.label_57.setFont(font8)

        self.verticalLayout_42.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_49)
        self.label_58.setObjectName(u"label_58")
        sizePolicy13.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy13)

        self.verticalLayout_42.addWidget(self.label_58)


        self.horizontalLayout_15.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_33)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy14.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy14)
        self.frame_50.setMinimumSize(QSize(0, 100))
        self.frame_50.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_50{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_50)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_59 = QLabel(self.frame_50)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font8)

        self.verticalLayout_39.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_50)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_39.addWidget(self.label_60)


        self.horizontalLayout_15.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_33)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy14.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy14)
        self.frame_51.setMinimumSize(QSize(0, 100))
        self.frame_51.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_51{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_51)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_61 = QLabel(self.frame_51)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font8)

        self.verticalLayout_38.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_51)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_38.addWidget(self.label_62)


        self.horizontalLayout_15.addWidget(self.frame_51)


        self.verticalLayout_37.addWidget(self.frame_33)

        self.frame_43 = QFrame(self.aboutPage)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy14.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy14)
        self.frame_43.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 24, 31);\n"
"}\n"
"QFrame#frame_43{\n"
"	border-radius: 14px;\n"
"    border: 1px solid rgba(0, 255, 255, 0.2);\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_43)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_47 = QLabel(self.frame_43)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: rgb(93, 137, 157);")

        self.gridLayout_5.addWidget(self.label_47, 8, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_43)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"color: rgb(93, 137, 157);\n"
"border-radius: 10px;\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon22)

        self.gridLayout_5.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_43)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: rgb(93, 137, 157);\n"
"border-radius: 10px;\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon23)

        self.gridLayout_5.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_43)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(93, 137, 157);\n"
"border-radius: 10px;\n"
"")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon24)

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.label_32 = QLabel(self.frame_43)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font8)

        self.gridLayout_5.addWidget(self.label_32, 0, 0, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_43)

        self.mainPages.addWidget(self.aboutPage)

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
        font15 = QFont()
        font15.setBold(True)
        font15.setWeight(75)
        self.label_7.setFont(font15)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeRightMenuBtn.setIcon(icon25)
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
        font16 = QFont()
        font16.setFamily(u"Segoe Print")
        font16.setPointSize(13)
        font16.setBold(True)
        font16.setWeight(75)
        self.label_8.setFont(font16)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QCustomSlideMenu()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font16)
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
        font17 = QFont()
        font17.setFamily(u"Segoe Print")
        font17.setPointSize(9)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_14.setFont(font17)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.notificationMssg = QLabel(self.frame_9)
        self.notificationMssg.setObjectName(u"notificationMssg")
        sizePolicy8.setHeightForWidth(self.notificationMssg.sizePolicy().hasHeightForWidth())
        self.notificationMssg.setSizePolicy(sizePolicy8)
        self.notificationMssg.setMinimumSize(QSize(0, 0))
        font18 = QFont()
        font18.setFamily(u"Segoe Print")
        font18.setBold(True)
        font18.setWeight(75)
        self.notificationMssg.setFont(font18)
        self.notificationMssg.setTextFormat(Qt.AutoText)
        self.notificationMssg.setAlignment(Qt.AlignCenter)
        self.notificationMssg.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.notificationMssg)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon26)
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
        self.label_15.setFont(font15)

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
        self.dashboardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.dashboardBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.genBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Script Generator", None))
#endif // QT_CONFIG(tooltip)
        self.genBtn.setText(QCoreApplication.translate("MainWindow", u"Script Generator", None))
#if QT_CONFIG(tooltip)
        self.linkBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Available Regions", None))
#endif // QT_CONFIG(tooltip)
        self.linkBtn.setText(QCoreApplication.translate("MainWindow", u"Link Check", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Generated Scripts", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
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
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Welcome to <span style=\" color:#25bfff;\">TelescriptGenius</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Your professional telecom scripting companion. Generate activation scripts in seconds.</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Templates Available</span></p></body></html>", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Ready to use</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Regions Supported</span></p></body></html>", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Nigeria coverage</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Scripts Generated</span></p></body></html>", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.totalgenerated.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">This month</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Avg. Generation Time</span></p></body></html>", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"1.2s", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Lightning fast</span></p></body></html>", None))
        self.genQuickBtn.setText(QCoreApplication.translate("MainWindow", u"Generate New Script", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Create activation or conviguration scripts</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ready to generate your first script?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#497b7d;\">Select a region and template, enter your parameters, and let TelescriptGenius do the rest.</span></p></body></html>", None))
        self.startQuickBtn.setText(QCoreApplication.translate("MainWindow", u"Start Generating", None))
        self.linkQuickBtn.setText(QCoreApplication.translate("MainWindow", u"Check Link Status", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Verify network connection status</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"System Status", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Script Engine</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Template Database</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Link Check Module</span></p></body></html>", None))
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#117d43;\">Operational</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#127950;\">Operational</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#de7d15;\">Coming Soon</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Script Generator", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Configure parameters and generate telecom activation scripts</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Configuration Parameters", None))
        self.regionLabel.setText(QCoreApplication.translate("MainWindow", u"Regions", None))
        self.regionBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Asaba", None))
        self.regionBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Enugu", None))
        self.regionBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kano", None))
        self.regionBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Owerri", None))

        self.regionBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Region", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Templates *", None))
        self.tempBox.setItemText(0, QCoreApplication.translate("MainWindow", u"10G CP ML Scripts", None))
        self.tempBox.setItemText(1, QCoreApplication.translate("MainWindow", u"10G CS ML Scripts", None))
        self.tempBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Aviat CP Scripts", None))
        self.tempBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Aviat CS Scripts", None))
        self.tempBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Router Scripts", None))

        self.tempBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select template", None))
        self.siteLabel.setText(QCoreApplication.translate("MainWindow", u"Site Name", None))
        self.sitename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g., DL0033", None))
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Scripts", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Generated Script", None))
        self.backlcBtn.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Coming Soon.....", None))
        self.label_44.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Configure your TelescriptGenius preferences.</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Enable dark theme for comfortable viewing</span></p></body></html>", None))
        self.pushButton_3.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Output Settings", None))
        self.chooseSaveLocation.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Scripts will be saved to this location by default</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Default Output Directory", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/TelescriptGenius", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Receive alerts for script generation and updates</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Enable Notifications", None))
        self.label_52.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">TelescriptGenius is a professional telecom scripting tool designed for engineers who need to</span></p><p><span style=\"color:#5d899d;\"> quickly generate activation and configuration scripts for telecom sites across different regions</span></p><p><span style=\" color:#5d899d;\"> and network vendors.</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#25bfff;\">TelescriptGenius</span></p><p>Version 2.0.1</p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00ffff;\">&quot;Scripting Simplicity,</span></p><p><span style=\" color:#00ffff;\">Genius Complexity.&quot;</span></p></body></html>", None))
        self.label_53.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Multi-Region Support", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Generate scripts for 4+ Nigerian regions with region-specific configurations.</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Template Library", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">5 pre-built templates for common telecom</span></p><p><span style=\" color:#5d899d;\"> activation scenarios.</span></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Lightning Fast", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#5d899d;\">Generate complete scripts in under 2 seconds</span></p><p><span style=\" color:#5d899d;\"> with our optimized engine.</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Built with \u2764\ufe0f for Telecom Engineers\n"
"\n"
"\u00a9 2026 TelescriptGenius. All rights reserved.", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Github Rpository", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Support Email", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Credits & Contact", None))
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

