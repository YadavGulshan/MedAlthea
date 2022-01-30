import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore

# initializing GUI application
app = QApplication(sys.argv)

# window and settings
window = QWidget()
window.setWindowTitle("Get Your Medicine!!")
window.setFixedWidth(1000)
window.move(2700, 200)
window.setStyleSheet("background: #161219;")

# initialize the grid layout
grid = QGridLayout()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
