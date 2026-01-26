import json
import os
from PyQt5 import *
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PySide2.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PySide2.QtGui import QIcon
from screens.login import LoginScreen
from screens.register import RegisterScreen

from ui.ui_welcome import Ui_WelcomeScreen


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WelcomeScreen()
        self.ui.setupUi(self)

        self.setWindowTitle("Welcome to TeleScript Genius!")
        self.setGeometry(100, 100, 800, 600)

        launch_date = QDateTime(2023, 8, 17, 0, 0, 0)
        today_date = QDateTime.currentDateTime()
        days_since_launch = launch_date.daysTo(today_date)

        self.ui.welSignBtn.clicked.connect(self.go_login)
        self.ui.welRegBtn.clicked.connect(self.go_register)
        self.ui.welSignBtn.setObjectCustomTheme("cyan", "black")
        self.ui.welRegBtn.setObjectCustomTheme("cyan", "black")

    def go_register(self):
        self.close()
        from main import show_register
        show_register()

    def go_login(self):
        self.close()
        from main import show_login
        show_login()
