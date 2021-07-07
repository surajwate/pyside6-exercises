from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QPushButton("Push Me")
window.show()

# Start the event loop.
app.exec()
