# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confettiBoidIO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QColor, QFont, QPainter
from PySide2.QtWidgets import QWidget
from custom_buttons import *


class Ui_Confetti(object):
    def setupUi(self, Confetti):
        if not Confetti.objectName():
            Confetti.setObjectName(u"Confetti")
        Confetti.resize(622, 519)
        Confetti.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(Confetti)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"*{\n"
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
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.happyLbl = QLabel(self.widget)
        self.happyLbl.setObjectName(u"happyLbl")
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(15)
        self.happyLbl.setFont(font)

        self.horizontalLayout.addWidget(self.happyLbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.widget)

        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Lucida Console")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.nextBtn.setFont(font1)

        self.verticalLayout.addWidget(self.nextBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        Confetti.setCentralWidget(self.centralwidget)

        self.retranslateUi(Confetti)

        QMetaObject.connectSlotsByName(Confetti)
    # setupUi

    def retranslateUi(self, Confetti):
        Confetti.setWindowTitle(QCoreApplication.translate("Confetti", u"MainWindow", None))
        self.happyLbl.setText("")
        self.nextBtn.setText(QCoreApplication.translate("Confetti", u"CONTINUE", None))
    # retranslateUi

