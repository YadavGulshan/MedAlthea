from PyQt5 import QtWidgets

from apps.Frames.MyMedical import Ui_MyMedical


class main:

    def __init__(self, widget, current_screen, homepage):
        self.widget = widget
        self.homeScreen = homepage
        self.current_screen = current_screen
        self.homeScreen.profile_pushButton.clicked.connect(self.openProfile)
        self.homeScreen.add_pushButton.clicked.connect(self.addMedical)
        self.homeScreen.view_pushButton.clicked.connect(homepage.getShopId)

    def openProfile(self):
        print("profile")

    def addMedical(self):
        print("Add")
