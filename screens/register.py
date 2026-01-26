from PySide2.QtWidgets import QMainWindow, QMessageBox

from ui.ui_register import Ui_RegScreen
from auth.auth_manager import register_user, validate_email, validate_password


class RegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_RegScreen()
        self.ui.setupUi(self)

        self.ui.regBtn.clicked.connect(self.register)
        self.ui.logNowBtn.clicked.connect(self.go_login)

        self.ui.regBtn.setObjectCustomTheme("cyan", "black")
        self.ui.logNowBtn.setObjectCustomTheme("cyan", "black")

    def register(self):
        email = self.ui.emailInput.text().strip()
        password = self.ui.passwordInput.text().strip()

        if not validate_email(email):
            QMessageBox.warning(self, "Error", "Invalid email")
            return

        if not validate_password(password):
            QMessageBox.warning(self, "Error", "Weak password")
            return

        success, msg = register_user(email, password)

        if success:
            QMessageBox.information(self, "Success", msg)
            self.go_login()
        else:
            QMessageBox.warning(self, "Error", msg)

    def go_login(self):
        self.close()
        from main import show_login
        show_login()
