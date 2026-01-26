from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QMainWindow, QPushButton, QLabel
from screens.confetti import ConfettiWidget
from styles.cyber_theme import CYBER_BG



class BirthdayScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Happy Birthday!")
        self.setGeometry(100, 100, 800, 600)

        self.confetti = ConfettiWidget(self)
        self.setCentralWidget(self.confetti)

        self.happy_label = QLabel("<b>Happy Belated Birthday 🎉\n We hope it was filled with joy and celebration.", self)
        self.happy_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                text-shadow: 0px 0px 18px rgba(0, 229, 255, 180);
            }
        """)

        self.happy_label.setFont(QFont("Sergio Print", 40, QFont.Bold))

        self.confetti.setStyleSheet(CYBER_BG)

        self.happy_label.setAlignment(Qt.AlignCenter)
        self.happy_label.setGeometry(50, 50, 700, 100)

        self.next_button = QPushButton("CONTINUE", self)
        self.next_button.setFont(QFont("Lucida console", 15, QFont.Bold))
        self.next_button.setGeometry(350, 500, 100, 40)
        self.next_button.clicked.connect(self.go_welcome)


    def go_welcome(self):
        self.close()
        from main import show_welcome
        show_welcome()