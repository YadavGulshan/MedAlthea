from PyQt5 import QtWidgets



class main:

    def __init__(self, widget, current_screen, homepage):
        self.widget = widget
        self.homeScreen = homepage
        self.current_screen = current_screen
        self.homeScreen.profile_pushButton.clicked.connect(self.openProfile)
        self.homeScreen.add_pushButton.clicked.connect(self.addMedical)
        

    def openProfile(self):
        print("profile")

    def addMedical(self):
        print("Add")
