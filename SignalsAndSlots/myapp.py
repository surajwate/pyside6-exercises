from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print("The button was toggled : ", self.button_is_checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print("The button was released : ", self.button_is_checked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
