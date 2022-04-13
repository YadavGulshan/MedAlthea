import datetime
import json
import os
import sys
from os.path import exists
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ipregistry import IpregistryClient

from Frames.functions.getLogin import getTokens
# from Frames.map import MyApp
from Frames.functions.getRegister import userRegister
from Frames.functions.localdb import LocalDB
from Frames.login import LoginFrame
from Frames.signUp import signUpFrame
from Frames.userHomePage import Ui_userHomePage


def getIpInfo():
    pathToHome = os.path.expanduser('~')
    if not exists(pathToHome + "/ipinfo.json"):
        print(exists(pathToHome + "/ipinfo.json"))
        print("creating file for ipInfo")
        client = IpregistryClient("tryout")
        ipInfo = client.lookup()._json
        with open(pathToHome + '/ipinfo.json', "w+") as f:
            json.dump(ipInfo, f)
            f.close()
            print('function end')
    else:
        print("file exists")


class userApp:
    def __init__(self, widget):
        self.homePageScreen = None
        self.month = 0
        self.widgetMain = widget
        self.localDB = LocalDB("userToken")
        self.tokens = self.localDB.getTokens()
        self.signUpScreen = QtWidgets.QDialog()
        self.loginScreen = QtWidgets.QDialog()

    def isRefreshValid(self):
        refreshLastUsed = datetime.datetime.strptime(self.tokens[0][1], "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.datetime.now()
        self.month = refreshLastUsed - today
        if self.month > datetime.timedelta(days=90):
            return False
        else:
            return True

    def gotoLogin(self):
        self.widgetMain.removeWidget(self.signUpScreen)
        self.widgetMain.addWidget(self.loginScreen)
        self.widgetMain.setWindowTitle("Login")

    def openLogin(self):
        self.widgetMain.setWindowTitle("Login")
        # initializing login screen
        self.login = LoginFrame()
        self.login.setupUi(self.loginScreen)
        self.widgetMain.addWidget(self.loginScreen)
        self.login.signup.clicked.connect(self.openSignUp)
        self.login.SignIn_button.clicked.connect(self.getLogin)

    def getLogin(self):
        username = self.login.UserName.text()
        password = self.login.Password.text()

        if len(username) == 0 or len(password) == 0:
            self.login.message.setText("All Field are required!")
        else:
            self.login.message.setText("")
            token = getTokens(username, password, 'userToken')
            if token == 200:
                self.ShowHomePage()
            else:
                self.login.message.setText("UserName Or Password is incorrect ")

    def openSignUp(self):
        self.widgetMain.setWindowTitle("Sign Up")
        self.signUp = signUpFrame()
        self.signUp.setupUi(self.signUpScreen)
        self.widgetMain.removeWidget(self.loginScreen)
        self.widgetMain.addWidget(self.signUpScreen)
        self.signUp.LoginIn_button.clicked.connect(self.checkValidation)
        self.signUp.login.clicked.connect(self.gotoLogin)

    def checkValidation(self):
        if self.signUp.getSignUp():
            userDetails = dict(username=self.signUp.username_text, password=self.signUp.password_text,
                               password2=self.signUp.password_text, email=self.signUp.email_text,
                               first_name=self.signUp.firstname_text, last_name=self.signUp.lastname_text,
                               isStaff=str(self.signUp.checkbox))
            status = userRegister(userDetails, 'userToken')
            if status.status_code == 201:
                self.gotoLogin()

    def ShowHomePage(self):
        self.homePage = Ui_userHomePage()
        self.homePageScreen = QtWidgets.QWidget()
        self.homePage.setupUi(self.homePageScreen)
        self.widgetMain.addWidget(self.homePageScreen)
        self.widgetMain.removeWidget(self.loginScreen)


if __name__ == '__main__':
    thread = Thread(target=getIpInfo)
    thread.start()
    App = QApplication(sys.argv)
    widgetMain = QtWidgets.QStackedWidget()
    userHomePage = userApp(widgetMain)
    widgetMain.setFixedWidth(900)
    widgetMain.setFixedHeight(850)
    widgetMain.show()
    if len(userHomePage.tokens) == 0:
        userHomePage.openLogin()
    else:
        if userHomePage.isRefreshValid():
            userHomePage.ShowHomePage()
        else:
            userHomePage.openLogin()
    sys.exit(App.exec_())
