# importing depended modules
import datetime
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# importing LocalDb and Functions
from Frames.functions.localdb import LocalDB
from Frames.functions.getLogin import getTokens
from Frames.functions.getRegister import userRegister

# importing Frames
from Frames.login import LoginFrame
from Frames.signUp import signUpFrame
from Frames.searchFrame import Ui_Form
from Frames.homePage import Ui_HomePage


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
        self.month = None
        self.signUpScreen = QtWidgets.QDialog()
        self.loginScreen = QtWidgets.QDialog()
        self.messageScreen = QtWidgets.QWidget()
        self.searchScreen = QtWidgets.QDialog()
        self.homeScreen = QtWidgets.QDialog()
        DB = LocalDB()
        self.TOKENS = DB.getTokens()
        self.widget = widget

    def openHomeScreen(self):
        self.search = Ui_HomePage()
        self.search.setupUi(self.homeScreen)
        self.widget.removeWidget(self.messageScreen)
        self.widget.addWidget(self.homeScreen)
        self.widget.removeWidget(self.loginScreen)

    def gotoLogin(self):
        self.widget.removeWidget(self.signUpScreen)
        self.widget.addWidget(self.loginScreen)
        # print("login page")

    def openLogin(self):
        # initializing login screen
        self.login = LoginFrame()
        self.login.setupUi(self.loginScreen)
        self.widget.addWidget(self.loginScreen)
        # self.widget.removeWidget(self.searchScreen)
        self.widget.removeWidget(self.homeScreen)
        self.login.SignIn_button.clicked.connect(self.getLogin)
        self.login.signup.clicked.connect(self.openSignUp)
        # print("login page")

    def openSignUp(self):
        # initializing signup screen
        self.signUp = signUpFrame()
        self.signUp.setupUi(self.signUpScreen)
        self.widget.removeWidget(self.loginScreen)
        self.widget.addWidget(self.signUpScreen)
        self.signUp.LoginIn_button.clicked.connect(self.checkValidation)
        self.signUp.login.clicked.connect(self.gotoLogin)
        # print("signup page")

    def checkValidation(self):
        if self.signUp.getSignUp():
            userDetails = dict(username=self.signUp.username_text, password=self.signUp.password_text,
                               password2=self.signUp.password_text, email=self.signUp.email_text,
                               first_name=self.signUp.firstname_text, last_name=self.signUp.lastname_text,
                               isStaff=str(self.signUp.checkbox))
            status = userRegister(userDetails)
            if status.status_code == 201:
                self.gotoLogin()

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
                # self.openSearchScreen()
                self.openHomeScreen()
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
        refreshLastUsed = datetime.datetime.strptime(tokens[0][1], "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.datetime.now()
        self.month = refreshLastUsed - today
        if self.month > datetime.timedelta(days=90):
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
    app.setDimension()
    if len(app.TOKENS) == 0:
        app.openLogin()
    else:
        if app.isRefreshValid():
            # app.welcome()
            # app.openSearchScreen()
            app.openHomeScreen()
        else:
            # app.sessionsExpired()
            app.openLogin()

    sys.exit(App.exec_())
