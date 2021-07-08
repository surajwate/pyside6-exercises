from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    'My App',
    'My app',
    'Still My App',
    'Still My app',
    'What on Earth',
    'What on earth',
    'This is surprising',
    'This is Surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("Signals and Slots")

        self.button = QPushButton("Press Me")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)
        """ Hook up our custom slot method the_window_title_changed to the windows .windowTitleChanged signal"""

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        """
        """
        print("Clicked")
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")

        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
