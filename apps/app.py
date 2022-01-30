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
window.setFixedHeight(800)
window.move(400, 100)
window.setStyleSheet("background: white;")

# initialize the grid layout
grid = QGridLayout()

window.setLayout(grid)

window.show()
sys.exit(app.exec_())
