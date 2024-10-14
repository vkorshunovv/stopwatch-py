import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter) 
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                QPushButton, QLabel {
                    padding: 20px;
                    font-weight: semi-bold;
                    font-family: Inter;
                }                   
                QPushButton {
                    font-size: 50px; 
                }
                QLabel {
                    font-size: 120px;
                    background-color: #c1f5e8;
                    border-radius: 20px;
                    color: #383838;
                }
        """)
        
    
    def start(self):
        pass

    def stop(self):
        pass
    
    def reset(self):
        pass
    
    def format_time(self, time):
        pass
    
    def update_display(self):
        pass
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())