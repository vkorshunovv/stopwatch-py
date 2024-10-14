import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())