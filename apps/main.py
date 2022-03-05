from PyQt5 import QtWidgets

from Frames.addMedical import Ui_addMedical
from apps.Frames.HomePage import Ui_HomePage


class main:

    def __init__(self, widget):
        self.widget = widget
        self.homeScreen = QtWidgets.QDialog()
        self.openHomeScreen()

    def openProfile(self):
        print("profile")

    def addMedical(self):
        self.AddMedicalScreen = QtWidgets.QDialog()
        AddMedical = Ui_addMedical()
        AddMedical.setupUi(self.AddMedicalScreen)
        self.widget.addWidget(self.AddMedicalScreen)
        self.widget.removeWidget(self.homeScreen)
        AddMedical.back.clicked.connect(self.goBack)

    def goBack(self):
        self.widget.removeWidget(self.AddMedicalScreen)
        self.openHomeScreen()

    def openHomeScreen(self):
        self.search = Ui_HomePage(self.widget)
        self.search.setupUi(self.homeScreen)
        self.widget.addWidget(self.homeScreen)
        self.search.profile_pushButton.clicked.connect(self.openProfile)
        self.search.add_pushButton.clicked.connect(self.addMedical)
