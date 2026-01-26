import os
import json

from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from ui.ui_splash import Ui_SplashScreen


class SplashScreen(QMainWindow):
    def __init__(self, finished_callback):
        super().__init__()

        self.finished_callback = finished_callback

        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 200))
        self.ui.dropShadowFrame.setGraphicsEffect(shadow)

        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)

    def update_progress(self):
        self.counter += 1
        self.ui.progressBar.setValue(self.counter)

        if self.counter >= 100:
            self.timer.stop()
            self.finish()

    def finish(self):
        base_dir = "userdata_01e4.dat"
        os.makedirs(base_dir, exist_ok=True)

        flag = os.path.join(base_dir, "first_run.json")
        first_run = not os.path.exists(flag)

        if first_run:
            with open(flag, "w") as f:
                json.dump({"done": True}, f)

        self.close()
        self.finished_callback(first_run)
