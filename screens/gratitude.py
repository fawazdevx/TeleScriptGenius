



from PySide2.QtCore import Qt, QDateTime
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from styles.cyber_theme import CYBER_BG


class GratitudeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thank You")
        self.setFixedSize(800, 500)

        central = QWidget(self)
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(25)
        central.setStyleSheet(CYBER_BG)

        launch_date = QDateTime(2023, 8, 17, 0, 0, 0)
        today = QDateTime.currentDateTime()
        days_since_launch = launch_date.daysTo(today)

        message = (
            "Welcome to <b>TeleScript Genius v2.0.1</b><br><br>"
            "Thank you for believing in this project and standing with us since launch.<br><br>"
            f"It has been <b>{days_since_launch} days</b> since TeleScript Genius was born."
        )

        self.label = QLabel(message)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 14))
        self.label.setWordWrap(True)

        self.next_btn = QPushButton("Continue")
        self.next_btn.setFixedSize(160, 45)
        self.next_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.next_btn.clicked.connect(self.go_welcome)

        layout.addWidget(self.label)
        layout.addWidget(self.next_btn, alignment=Qt.AlignCenter)

    def go_welcome(self):
        self.close()
        from main import show_welcome
        show_welcome()

