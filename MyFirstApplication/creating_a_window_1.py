from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()

# Start the event loop.
app.exec()
