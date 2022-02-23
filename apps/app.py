# importing depended modules
import time
from atexit import register
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import DateTime

# importing LocalDb
from Frames.functions.localdb import LocalDB
from Frames.functions.getLogin import getTokens
from Frames.functions.getRegister import userLogin

# importing Frames
from Frames.login import LoginFrame
from Frames.searchFrame import Ui_Form
from Frames.signUp import signUpFrame
from Frames.message import UI_Message


class app:
    """
        Here in Local we Have our tokens
        At first index we have refresh token
        At second index we have date and time of refresh token Last used
        At Third index we have Access token
        At Fourth index we have date and time of access token Last used
    """

    def __init__(self, widget):
        # ---------- Creating .sqlit3 file in apps folder and making connection to local db --------#
        # Crating object of local DB
        self.signUpScreen = QtWidgets.QDialog()
        self.loginScreen = QtWidgets.QDialog()
        self.messageScreen = QtWidgets.QWidget()
        self.searchScreen = QtWidgets.QDialog()
        DB = LocalDB()
        self.TOKENS = DB.getTokens()
        self.widget = widget

    # checking weather the user already login or not
    def showMessage(self, text):
        self.message = UI_Message()
        self.message.setupUi(self.messageScreen, text)
        print("display")
        self.widget.addWidget(self.messageScreen)
        time.sleep(2)
        self.widget.removeWidget(self.messageScreen)
        print("remove")

    def openSearchScreen(self):
        self.search = Ui_Form()
        self.search.setupUi(self.searchScreen)
        self.widget.addWidget(self.searchScreen)
        self.widget.removeWidget(self.loginScreen)
        print("search page")

    def gotoLogin(self):
        self.widget.removeWidget(self.signUpScreen)
        self.widget.addWidget(self.loginScreen)
        print("login page")

    def openLogin(self):
        # initializing login screen
        self.login = LoginFrame()
        self.login.setupUi(self.loginScreen)
        self.widget.addWidget(self.loginScreen)
        self.widget.removeWidget(self.searchScreen)
        self.login.SignIn_button.clicked.connect(self.getLogin)
        self.login.signup.clicked.connect(self.openSignUp)
        print("login page")

    def openSignUp(self):
        # initializing signup screen
        self.signUp = signUpFrame()
        self.signUp.setupUi(self.signUpScreen)
        self.widget.removeWidget(self.loginScreen)
        self.widget.addWidget(self.signUpScreen)
        self.signUp.LoginIn_button.clicked.connect(self.checkValidation)
        self.signUp.login.clicked.connect(self.gotoLogin)
        print("signup page")

    def checkValidation(self):
        if self.signUp.getSignUp():
            userDetails = {
                "username": self.signUp.username_text,
                "password": self.signUp.password_text,
                "password2": self.signUp.password_text,
                "email": self.signUp.email_text,
                "first_name": self.signUp.firstname_text,
                "last_name": self.signUp.lastname_text
            }
            status = userLogin(userDetails)
            if status.status_code == 201:
                self.gotoLogin()
                print("login page")

    def getLogin(self):
        username_text = self.login.UserName.text()
        password_text = self.login.Password.text()
        if len(username_text) == 0 or len(password_text) == 0:
            self.login.message.setText("All Field are required!")
        else:
            self.login.message.setText("")
            token = getTokens(username_text, password_text)
            if token == 200:
                print("success!")
                self.openSearchScreen()
            else:
                print(token)
                self.login.message.setText("UserName Or Password is incorrect ")

    def setDimension(self):
        self.widget.setFixedWidth(900)
        self.widget.setFixedHeight(850)
        self.widget.show()

    def isRefreshValid(self):
        self.db = LocalDB()
        tokens = self.db.getTokens()
        refreshLastUsed = DateTime.DateTime(tokens[0][1])
        today = DateTime.DateTime()
        self.month = refreshLastUsed - today
        if self.month > 90:
            return False
        else:
            return True

    def welcome(self):
        self.showMessage("Welcome Back!!")

    def sessionsExpired(self):
        self.showMessage("Session time Out!!")


if __name__ == '__main__':
    # initializing GUI application
    App = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    app = app(widget)

    if len(app.TOKENS) == 0:
        app.openLogin()
    else:
        if app.isRefreshValid():
            app.welcome()
            app.openSearchScreen()
        else:
            app.sessionsExpired()
            app.openLogin()
    app.setDimension()

    sys.exit(App.exec_())
