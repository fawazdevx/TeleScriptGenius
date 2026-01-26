import random
from PySide2.QtCore import Qt, QTimer, QRectF
from PySide2.QtGui import QColor, QFont, QPainter
from PySide2.QtWidgets import QWidget


class Confetti:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = random.uniform(1, 5)

    def move(self, width, height):
        self.y += self.speed
        if self.y > height:
            self.y = -self.size
            self.x = random.randint(0, width)
            self.speed = random.uniform(1, 5)


class ConfettiWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.confetti_list = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(30)

        self.create_confetti(150)

    def create_confetti(self, count):
        for _ in range(count):
            self.confetti_list.append(
                Confetti(
                    random.randint(0, 800),
                    random.randint(0, 600),
                    random.randint(6, 14),
                    QColor(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    ),
                )
            )

    def update_animation(self):
        for c in self.confetti_list:
            c.move(self.width(), self.height())
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(10, 10, 20))

        for c in self.confetti_list:
            painter.setBrush(c.color)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(QRectF(c.x, c.y, c.size, c.size))

        painter.setPen(Qt.white)
        painter.setFont(QFont("Arial", 36, QFont.Bold))
        painter.drawText(self.rect(), Qt.AlignCenter, "🎉 Happy Birthday 🎉")
