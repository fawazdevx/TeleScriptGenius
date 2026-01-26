CYBER_BG = """
QWidget {
    background-color: qradialgradient(
        cx:0.25, cy:0.2, radius:1.1,
        fx:0.25, fy:0.2,
        stop:0 rgba(0, 229, 255, 35),
        stop:0.35 rgba(12, 18, 28, 215),
        stop:1 rgba(10, 14, 20, 235)
    );
    
    border-radius: 22px;
    border: 1px solid rgba(0, 229, 255, 70);
}

/* Main text labels */
QLabel {
    color: #e8faff;
}

/* Primary buttons */
QPushButton {
    background-color: rgba(0, 229, 255, 160);
    color: #02080c;
    border: none;
    border-radius: 14px;
    padding: 10px 26px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: rgba(0, 229, 255, 220);
}

QPushButton:pressed {
    background-color: rgba(0, 200, 225, 200);
}

/* Optional glow effect */
QPushButton {
    box-shadow: 0px 0px 14px rgba(0, 229, 255, 80);
}
"""
