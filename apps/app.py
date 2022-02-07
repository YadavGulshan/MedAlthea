import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit
from PyQt5.uic import loadUi
import Frames


# welcomeFrame(grid)

class loginform(QDialog):
    def __init__(self):
        super(loginform, self).__init__()
        loadUi('', self)
        self.Password.setEchoMode(QLineEdit.Password)
        self.SignIn_button.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.Email.text()
        password = self.Password.text()

        if len(user) == 0 or len(password) == 0:
            self.label.setText("Please input all fields")
        else:
            # connection
            if 'result_pass' == password:
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")


# initializing GUI application
app = QApplication(sys.argv)


window = QtWidgets.QStackedWidget()

login = loginform()
# set height and width
window.addWidget(login)
window.setFixedWidth(900)
window.setFixedHeight(850)





window.show()
sys.exit(app.exec_())
