import datetime
import json
import os
import sys
from os.path import exists
from threading import Thread

import ocrspace as ocr
import requests as rs
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCompleter
from PyQt6.QtGui import QFontDatabase
from ipregistry import IpregistryClient

from Frames.functions.getLogin import getTokens
from Frames.functions.getRegister import userRegister
from Frames.functions.localdb import LocalDB
from Frames.functions.makerequest import makeRequest
from Frames.functions.userOperations import getNearByShop
from Frames.login import LoginFrame
from Frames.map import MyApp
from Frames.ownerProfile import Ui_ownerProfile
from Frames.signUp import signUpFrame
from Frames.userHomePage import Ui_userHomePage

pathToHome = os.path.expanduser('~')


def getAllMedicines():
    make = makeRequest('userToken')
    make.checkAccessToken()

    try:
        make.headers["Authorization"] = "Bearer {}".format(make.accessToken)
        resp = rs.get(make.API + "/medicine/", headers=make.headers, json={})
        if resp.status_code == 200:
            return resp
        else:
            raise Exception("Unauthorized")
    except Exception as e:
        print(e)


def getDetails():
    with open(pathToHome + '/ipinfo.json', "r") as f:
        ipinfo = json.load(f)
        f.close()
    lon = ipinfo.get('location')['longitude']
    lat = ipinfo.get('location')['latitude']
    pincode = ipinfo.get('location')['postal']
    return pincode, lon, lat


def getIpInfo():
    if not exists(pathToHome + "/ipinfo.json"):
        print("creating file for ipInfo")
        client = IpregistryClient("tryout")
        ipInfo = client.lookup()._json
        with open(pathToHome + '/ipinfo.json', "w+") as f:
            json.dump(ipInfo, f)
            f.close()
            print('function end')


def showMessage(messageText):
    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Medical Not Found")
    message.setText(messageText)
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.exec_()


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
        self.model = QStandardItemModel()
        self.completer = QCompleter(self.model, self.widgetMain)
        self.homePage.search_input.setCompleter(self.completer)
        self.widgetMain.addWidget(self.homePageScreen)
        self.widgetMain.removeWidget(self.loginScreen)
        self.homePage.profile.clicked.connect(self.userProfile)
        self.homePage.ocrButton.clicked.connect(self.getPicture)
        self.homePage.findIt.clicked.connect(self.openMap)
        thread1 = Thread(target=self.addCompleter)
        thread1.start()

    def openMap(self):
        medicine = self.homePage.search_input.text()
        if not len(medicine) == 0:
            pincode, lat, lon = getDetails()
            resp = getNearByShop(medicine, pincode, lat, lon)
            if len(resp.json()) == 0:
                showMessage("\nShop not found \nwith given medicine. \nSorry for inconvenience!!\n")
            else:
                self.mapScreen = QtWidgets.QWidget()
                map = MyApp(resp.json(), self.mapScreen, (lon, lat))
                self.mapScreen.show()
                self.homePageScreen.show()

    def getPicture(self):
        ocrImage, _ = QtWidgets.QFileDialog.getOpenFileName(self.widgetMain, "select CSV", pathToHome,
                                                            "Image Files (*.png *.jpeg)")
        if not ocrImage == "":
            self.homePage.search_input.setText("")
            api = ocr.API(OCREngine=2)
            resp = api.ocr_file(open(ocrImage, 'rb'))
            self.homePage.search_input.setText(resp)

    def userProfile(self):
        self.userProfileScreen = QtWidgets.QWidget()
        userprofile = Ui_ownerProfile(self.userProfileScreen)
        userprofile.setupUi("userToken")
        self.widgetMain.addWidget(self.userProfileScreen)
        self.widgetMain.removeWidget(self.homePageScreen)
        userprofile.back.clicked.connect(self.closeUserProfile)
        userprofile.logout_button.clicked.connect(self.logout)

    def closeUserProfile(self):
        self.widgetMain.removeWidget(self.userProfileScreen)
        self.widgetMain.addWidget(self.homePageScreen)

    def logout(self):
        self.localDB.getLogout()
        self.widgetMain.removeWidget(self.homePageScreen)
        self.widgetMain.removeWidget(self.userProfileScreen)
        self.openLogin()

    def addCompleter(self):
        try:
            allMedicines = getAllMedicines()
            for i in allMedicines.json():
                self.model.appendRow(QStandardItem(i.get('name')))
            self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    thread = Thread(target=getIpInfo)
    thread.start()
    App = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(os.getcwd() + '/apps/Lato2OFL/Lato-Semibold.ttf')
    QFontDatabase.addApplicationFont(os.getcwd() + '/apps/Lato2OFL/Lato-Regular.ttf')
    widgetMain = QtWidgets.QStackedWidget()
    widgetMain.setStyleSheet("font-family:'Lato'")
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
