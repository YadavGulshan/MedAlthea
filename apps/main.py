import re
import os
from PyQt5 import QtWidgets

from Frames.addMedical import Ui_addMedical
from Frames.HomePage import Ui_HomePage
from Frames.ownerProfile import Ui_ownerProfile
from Frames.functions.getData import createMedical


class main:

    def __init__(self, widget):
        self.email_text = None
        self.widget = widget
        self.homeScreen = QtWidgets.QDialog()
        self.openHomeScreen()
        self.valid = False

    def openOwnerProfile(self):
        self.AddProfileFrame = QtWidgets.QDialog()
        AddProfile = Ui_ownerProfile()
        AddProfile.setupUi(self.AddProfileFrame)
        self.widget.removeWidget(self.homeScreen)
        self.widget.addWidget(self.AddProfileFrame)
        AddProfile.back.clicked.connect(self.profileToHome)

    def profileToHome(self):
        self.widget.removeWidget(self.AddProfileFrame)
        self.widget.addWidget(self.homeScreen)

    def addMedical(self):
        self.AddMedicalScreen = QtWidgets.QDialog()
        self.AddMedical = Ui_addMedical()
        self.AddMedical.setupUi(self.AddMedicalScreen)
        self.widget.addWidget(self.AddMedicalScreen)
        self.widget.removeWidget(self.homeScreen)
        self.AddMedical.back.clicked.connect(self.goBack)
        self.AddMedical.submit.clicked.connect(self.checkValues)
        self.AddMedical.addPhoto.clicked.connect(self.selectPhoto)

    def goBack(self):
        self.widget.removeWidget(self.AddMedicalScreen)
        self.openHomeScreen()

    def openHomeScreen(self):
        self.search = Ui_HomePage(self.widget)
        self.search.setupUi(self.homeScreen)
        self.widget.addWidget(self.homeScreen)
        self.search.profile_pushButton.clicked.connect(self.openOwnerProfile)
        self.search.add_pushButton.clicked.connect(self.addMedical)

    def selectPhoto(self):
        pathToHome = os.path.expanduser('~')
        selectedPhoto = QtWidgets.QFileDialog.getOpenFileName(self.AddMedicalScreen, "select Photo", pathToHome,
                                                              "Image Files (*.png *.jpg *.jpeg)")
        if not selectedPhoto[0] == "":
            with open(selectedPhoto[0], "r+") as photo:
                print(photo)
                self.photo = photo

    def checkValues(self):
        medicalName_text = self.AddMedical.medicalName.text()
        email_text = self.AddMedical.email.text()
        pincode_text = self.AddMedical.pincode.text()
        phoneNumber_text = self.AddMedical.phoneNumber.text()
        address_text = self.AddMedical.address.text()
        website_text = self.AddMedical.website.text()
        phoneNumber = "+91"

        if len(medicalName_text.replace(" ", "")) == 0 or len(email_text.replace(" ", "")) == 0 or len(
                phoneNumber_text.replace(" ", "")) == 0 or len(
                pincode_text.replace(" ", "")) == 0 or len(address_text.replace(" ", "")) == 0:
            self.AddMedical.message.setText("all filed are required!")
        else:
            self.AddMedical.message.setText("")
            if len(phoneNumber_text.replace(" ", "")) == 10:
                if phoneNumber_text.isnumeric():
                    phoneNumber += str(phoneNumber_text)
                    self.AddMedical.phoneMessage.setText("")
                    self.valid = True
                else:
                    self.AddMedical.phoneMessage.setText("phone number should not contain characters")
                    self.valid = False

                if self.check(email_text):
                    self.AddMedical.emailMessage.setText("")
                    self.valid = True
                else:
                    self.AddMedical.emailMessage.setText("Enter a valid email")
                    self.valid = False
                if len(pincode_text) == 6:
                    if not pincode_text.isnumeric():
                        print(pincode_text.isnumeric())
                        self.valid = False
                        self.AddMedical.message.setText("Pincode must be numerical")
                    else:
                        print(pincode_text.isnumeric())
                        self.valid = True
                else:
                    self.valid = False
                    self.AddMedical.message.setText("Pincode must be 6 digit long")
            else:
                self.AddMedical.phoneMessage.setText("phone number should be 10 digit long")
                self.valid = False
        if self.valid:
            response = createMedical(
                {"name": medicalName_text, "pincode": pincode_text, "address": address_text, "phone": phoneNumber,
                 "email": email_text,
                 "latitude": 0.0, "longitude": 0.0, "website": website_text, "image": self.photo})
            if response.status_code == 201:
                message = QtWidgets.QMessageBox()
                message.setWindowTitle("Medical registered")
                message.setText("Registration done")
                message.setIcon(QtWidgets.QMessageBox.Information)
                message.exec_()
                self.widget.removeWidget(self.AddMedicalScreen)
                self.openHomeScreen()

    @staticmethod
    def check(email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return True
        else:
            return False
