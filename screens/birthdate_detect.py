from PySide2.QtCore import Qt, QDateTime
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from styles.cyber_theme import CYBER_BG


class BirthdayDetectScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("System Message")
        self.setFixedSize(800, 500)

        central = QWidget(self)
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(25)

        today = QDateTime.currentDateTime()
        yesterday = today.addDays(-1)

        message = (
            f"Our system detected from your device that<br>"
            f"<b>{yesterday.toString('dd MMMM yyyy')}</b> was your birthday.<br><br>"
        )

        self.label = QLabel(message)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Segoe UI", 15))
        self.label.setWordWrap(True)

        self.next_btn = QPushButton("Continue")
        self.next_btn.setFixedSize(160, 45)
        self.next_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.next_btn.clicked.connect(self.go_birthdate)
        central.setStyleSheet(CYBER_BG)

        layout.addWidget(self.label)
        layout.addWidget(self.next_btn, alignment=Qt.AlignCenter)

    def go_birthdate(self):
        self.close()
        from main import show_birthdate
        show_birthdate()


