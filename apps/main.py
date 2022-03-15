from PyQt5 import QtWidgets

from Frames.addMedical import Ui_addMedical
from Frames.HomePage import Ui_HomePage


class main:

    def __init__(self, widget):
        self.widget = widget
        self.homeScreen = QtWidgets.QDialog()
        self.openHomeScreen()

    def openProfile(self):
        print("profile")

    def addMedical(self):
        self.AddMedicalScreen = QtWidgets.QDialog()
        self.AddMedical = Ui_addMedical()
        self.AddMedical.setupUi(self.AddMedicalScreen)
        self.widget.addWidget(self.AddMedicalScreen)
        self.widget.removeWidget(self.homeScreen)
        self.AddMedical.back.clicked.connect(self.goBack)
        self.AddMedical.submit.clicked.connect(self.checkValues)

    def goBack(self):
        self.widget.removeWidget(self.AddMedicalScreen)
        self.openHomeScreen()

    def openHomeScreen(self):
        self.search = Ui_HomePage(self.widget)
        self.search.setupUi(self.homeScreen)
        self.widget.addWidget(self.homeScreen)
        self.search.profile_pushButton.clicked.connect(self.openProfile)
        self.search.add_pushButton.clicked.connect(self.addMedical)

    def checkValues(self):
        medicalName_text = self.AddMedical.medicalName.text()
        email_text = self.AddMedical.email.text()
        pincode_text = self.AddMedical.pincode.text()
        phoneNumber_text = self.AddMedical.phoneNumber.text()
        address_text = self.AddMedical.address.text()
        website_text = self.AddMedical.website.text()
        print(medicalName_text, email_text, pincode_text, phoneNumber_text, address_text,
              website_text)
        # self.addPhoto_text = self.addPhoto.text()
