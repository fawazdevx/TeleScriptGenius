# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bdateEldBIq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_buttons import *
import resources_rc

class Ui_bdate(object):
    def setupUi(self, bdate):
        if not bdate.objectName():
            bdate.setObjectName(u"bdate")
        bdate.resize(647, 507)
        bdate.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(bdate)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMinimumSize(QSize(80, 40))
        self.backBtn.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.backBtn, 0, Qt.AlignLeft)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.bdateLbl = QLabel(self.widget)
        self.bdateLbl.setObjectName(u"bdateLbl")
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(15)
        self.bdateLbl.setFont(font)
        self.bdateLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.bdateLbl, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy1)
        self.nextBtn.setMinimumSize(QSize(0, 50))
        self.nextBtn.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Lucida Console")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.nextBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.nextBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        bdate.setCentralWidget(self.centralwidget)

        self.retranslateUi(bdate)

        QMetaObject.connectSlotsByName(bdate)
    # setupUi

    def retranslateUi(self, bdate):
        bdate.setWindowTitle(QCoreApplication.translate("bdate", u"MainWindow", None))
        self.backBtn.setText("")
        self.bdateLbl.setText("")
        self.nextBtn.setText(QCoreApplication.translate("bdate", u"CELEBRATE", None))
    # retranslateUi

