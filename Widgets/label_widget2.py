import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(850, 600))
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("./images/cat.jpg"))
        widget.setAlignment(Qt.AlignCenter)
        # widget.setScaledContents(True)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
