import sys

from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit

# initializing GUI application
from Frames.welcome_frame import welcomeFrame

app = QApplication(sys.argv)

# window and settings
window = QWidget()
# set the title to the window!
window.setWindowTitle("Get Your Medicine!!")
# set height and width
window.setFixedWidth(800)
# window.setFixedHeight(650)
# Set the location of window at desktop
window.move(400, 100)
window.setStyleSheet("background: #EEE6CE;")
# initialize the grid layout
grid = QGridLayout()

welcomeFrame(grid)

window.setLayout(grid)

window.show()
sys.exit(app.exec_())
