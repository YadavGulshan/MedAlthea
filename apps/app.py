import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog,QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from django.db import connection
from Frames.welcome_frame import welcomeFrame
# initializing GUI application
app = QApplication(sys.argv)

# window and settings
window = QWidget()
# set the title to the window!
window.setWindowTitle("Get Your Medicine!!")
# set height and width

window.setFixedWidth(900)
window.setFixedHeight(850)
# Set the location of window at desktop
# window.move(400, 100)
# window.setStyleSheet("background: #EEE6CE; padding: 20px;")
# initialize the grid layout
grid = QGridLayout()

# welcomeFrame(grid)

class loginform(QDialog):
    def __init__(self):
        super(loginform,self).__init__()
        loadUi("loginform.ui",self)
        self.Password.setEchoMode(QLineEdit.Password)
        self.SignIn_button.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user=self.Email.text()
        password=self.Password.text()

        if len(user)==0 or len(password)==0:
            self.label.setText("Please input all fields")
        else:
            # connection
            if result_pass==password:
                print("Succesfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

# window.setLayout(grid)

login=loginform()
grid.addWidget(login)
window.show()
sys.exit(app.exec_())
