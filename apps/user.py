import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from app import app
from Frames.functions.localdb import LocalDB
from main import main
from Frames.functions.getLogin import getTokens


class Root(main, app):
    def __init__(self, widget):
        super().__init__(widget)
        self.authApp = app(widget)

    def StartShopApp(self):
        self.openHomeScreen()
        self.AddProfile.logout_button.clicked.connect(self.getLogOut)

    def getLogOut(self):
        self.DB.getLogout()
        self.widget.removeWidget(self.homeScreen)
        self.widget.removeWidget(self.AddProfileFrame)
        self.DB = LocalDB()
        self.startAuthApp()

    def startAuthApp(self):
        self.authApp.openLogin()
        self.authApp.login.SignIn_button.clicked.connect(self.getLogin)

    def getLogin(self):
        username_text = self.authApp.login.UserName.text()
        password_text = self.authApp.login.Password.text()
        if len(username_text) == 0 or len(password_text) == 0:
            self.authApp.login.message.setText("All Field are required!")
        else:
            self.authApp.login.message.setText("")
            token = getTokens(username_text, password_text)
            if token == 200:
                print("success!")
                self.widget.removeWidget(self.authApp.loginScreen)
                self.StartShopApp()
            else:
                print(token)
                self.authApp.login.message.setText("UserName Or Password is incorrect ")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    widgetMain = QtWidgets.QStackedWidget()
    RootObject = Root(widgetMain)
    RootObject.setDimension()
    if len(RootObject.DB.getTokens()) == 0:
        RootObject.startAuthApp()
    else:
        if RootObject.isRefreshValid():
            print("checking refresh")
            RootObject.StartShopApp()
        else:
            RootObject.startAuthApp()

    sys.exit(App.exec_())
