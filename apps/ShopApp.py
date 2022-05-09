import json
import os
import sys
from os.path import exists
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication
from ipregistry import IpregistryClient

from Frames.functions.getLogin import getTokens
from Frames.functions.getData import getTrendingMed
from app import app
from main import main


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
            token = getTokens(username_text, password_text, 'token')
            if token == 200:
                self.widget.removeWidget(self.authApp.loginScreen)
                self.StartShopApp()
            else:
                self.authApp.login.message.setText("UserName Or Password is incorrect ")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    thread = Thread(target=getIpInfo)
    thread.start()
    QFontDatabase.addApplicationFont('Lato2OFL/Lato-Regular.ttf')
    QFontDatabase.addApplicationFont('Lato2OFL/Lato-SemiBold.ttf')
    widgetMain = QtWidgets.QStackedWidget()
    widgetMain.setStyleSheet("font-family:'Lato'")
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


    # trendingMedScreen = QtWidgets.QWidget()
    # data = getTrendingMed(400601).json()
    # trendingMed.setup(trendingMedScreen, data)
    # widgetMain.addWidget(trendingMedScreen)

