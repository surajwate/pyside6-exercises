from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App 4")

        self.label = QLabel()

        self.input = QLineEdit()
        # To connect the input to the label, the input and label must both be defined.
        self.input.textChanged.connect(self.label.setText)

        # This adds the two widgets to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()