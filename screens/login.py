import json
import os

from PySide2.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PySide2.QtGui import QIcon

from ui.ui_login import Ui_LoginScreen
from auth.security import verify_password

USER_DIR = "userdata_01e4.dat"
USERS_FILE = os.path.join(USER_DIR, "users.json")
SESSION_FILE = os.path.join(USER_DIR, "user_session.json")


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)

        self.ui.logBtn.clicked.connect(self.login)
        self.ui.regNowBtn.clicked.connect(self.go_register)
        self.ui.logBtn.setObjectCustomTheme("cyan", "black")
        self.ui.regNowBtn.setObjectCustomTheme("cyan", "black")

        self.ui.passwordInput.setEchoMode(QLineEdit.Password)

    def login(self):
        email = self.ui.emailInput.text().strip().lower()
        password = self.ui.passwordInput.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Fill all fields")
            return

        if not os.path.exists(USERS_FILE):
            QMessageBox.warning(self, "Error", "No users found")
            return

        with open(USERS_FILE, "r") as f:
            users = json.load(f)

        if email not in users or not verify_password(users[email]["password"], password):
            QMessageBox.warning(self, "Error", "Invalid credentials")
            return

        os.makedirs(USER_DIR, exist_ok=True)
        with open(SESSION_FILE, "w") as f:
            json.dump({"user": email}, f)

        self.close()
        from main import show_main
        show_main()

    def go_register(self):
        self.close()
        from main import show_register
        show_register()
