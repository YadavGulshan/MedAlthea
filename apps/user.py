import json
import os
import sys
import asyncio

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ipregistry import IpregistryClient

from Frames.functions.getLogin import getTokens
from app import app
from main import main


async def getIpInfo():
    print('running function')
    pathToHome = os.path.expanduser('~')
    client = IpregistryClient("tryout")
    ipInfo = client.lookup()._json
    with open(pathToHome + '/ipinfo.json', "w+") as f:
        json.dump(ipInfo, f)
        f.close()
        print('function end')


class Root(main, app):
    def __init__(self, widget):
        super().__init__(widget)

    def StartShopApp(self):
        self.openHomeScreen()
        self.AddProfile.logout_button.clicked.connect(self.getLogOut)

    def getLogOut(self):
        self.DB.getLogout()
        self.widget.removeWidget(self.homeScreen)
        self.widget.removeWidget(self.AddProfileFrame)
        # self.DB = LocalDB()
        self.startAuthApp()

    def startAuthApp(self):
        self.authApp = app(self.widget)
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
                self.widget.removeWidget(self.authApp.loginScreen)
                self.StartShopApp()
            else:
                self.authApp.login.message.setText("UserName Or Password is incorrect ")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    # asyncio.run(getIpInfo()
    widgetMain = QtWidgets.QStackedWidget()
    RootObject = Root(widgetMain)
    RootObject.setDimension()
    if len(RootObject.DB.getTokens()) == 0:
        RootObject.startAuthApp()
    else:
        if RootObject.isRefreshValid():
            RootObject.StartShopApp()
        else:
            RootObject.startAuthApp()

    sys.exit(App.exec_())
