import datetime

from PyQt5 import QtWidgets

from Frames.functions.localdb import LocalDB
from Frames.functions.getRegister import userRegister

from Frames.login import LoginFrame
from Frames.signUp import signUpFrame


class app:
    """
        Here in Local we Have our tokens
        At first index we have refresh token
        At second index we have date and time of refresh token Last used
        At Third index we have Access token
        At Fourth index we have date and time of access token Last used
    """

    def __init__(self, widget):
        self.month = None
        self.signUpScreen = QtWidgets.QDialog()
        self.loginScreen = QtWidgets.QDialog()
        self.messageScreen = QtWidgets.QWidget()
        self.searchScreen = QtWidgets.QDialog()
        self.DB = LocalDB("token")
        self.TOKENS = self.DB.getTokens()
        self.widget = widget

    def gotoLogin(self):
        self.widget.removeWidget(self.signUpScreen)
        self.widget.addWidget(self.loginScreen)
        self.widget.setWindowTitle("Login")

    def openLogin(self):
        self.widget.setWindowTitle("Login")
        # initializing login screen
        self.login = LoginFrame()
        self.login.setupUi(self.loginScreen)
        self.widget.addWidget(self.loginScreen)
        self.login.signup.clicked.connect(self.openSignUp)

    def openSignUp(self):
        # initializing signup screen
        self.widget.setWindowTitle("Sign Up")
        self.signUp = signUpFrame()
        self.signUp.setupUi(self.signUpScreen)
        self.widget.removeWidget(self.loginScreen)
        self.widget.addWidget(self.signUpScreen)
        self.signUp.LoginIn_button.clicked.connect(self.checkValidation)
        self.signUp.login.clicked.connect(self.gotoLogin)

    def checkValidation(self):
        if self.signUp.getSignUp():
            userDetails = dict(username=self.signUp.username_text, password=self.signUp.password_text,
                               password2=self.signUp.password_text, email=self.signUp.email_text,
                               first_name=self.signUp.firstname_text, last_name=self.signUp.lastname_text,
                               isStaff=str(self.signUp.checkbox))
            status = userRegister(userDetails, 'token')
            if status.status_code == 201:
                self.gotoLogin()

    def setDimension(self):
        self.widget.setFixedWidth(900)
        self.widget.setFixedHeight(850)
        self.widget.show()

    def isRefreshValid(self):
        tokens = self.DB.getTokens()
        refreshLastUsed = datetime.datetime.strptime(tokens[0][1], "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.datetime.now()
        self.month = refreshLastUsed - today
        if self.month > datetime.timedelta(days=90):
            return False
        else:
            return True
