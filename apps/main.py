import asyncio
import json
import os
import re

from PyQt5 import QtWidgets

from Frames.HomePage import Ui_HomePage
from Frames.addMedical import Ui_addMedical
from Frames.functions.getData import createMedical
from Frames.functions.localdb import LocalDB
from Frames.ownerProfile import Ui_ownerProfile


class main:

    def __init__(self, widget):
        self.photo = None
        self.widget = widget
        self.DB = LocalDB("token")
        self.valid = False
        self.email_text = None

        self.AddProfileFrame = QtWidgets.QDialog()
        self.AddMedicalScreen = QtWidgets.QDialog()
        self.AddMedical = Ui_addMedical()
        self.homePage = Ui_HomePage(self.widget)
        self.AddProfile = Ui_ownerProfile(self.AddProfileFrame)

    def openHomeScreen(self):
        self.homeScreen = QtWidgets.QDialog()
        self.widget.setWindowTitle("Home page")
        self.homePage.setupUi(self.homeScreen)
        self.widget.addWidget(self.homeScreen)
        self.homePage.profile_pushButton.clicked.connect(self.openOwnerProfile)
        self.homePage.add_pushButton.clicked.connect(self.addMedical)

    def openOwnerProfile(self):
        self.AddProfile.setupUi('token')
        self.widget.removeWidget(self.homeScreen)
        self.widget.addWidget(self.AddProfileFrame)
        self.AddProfile.back.clicked.connect(self.profileToHome)

    def profileToHome(self):
        self.widget.removeWidget(self.AddProfileFrame)
        self.widget.addWidget(self.homeScreen)

    def addMedical(self):
        self.AddMedical.setupUi(self.AddMedicalScreen)
        self.widget.addWidget(self.AddMedicalScreen)
        self.widget.removeWidget(self.homeScreen)
        self.AddMedical.back.clicked.connect(self.goBack)
        self.AddMedical.submit.clicked.connect(self.checkValues)
        self.AddMedical.addPhoto.clicked.connect(self.selectPhoto)

    def goBack(self):
        self.widget.removeWidget(self.AddMedicalScreen)
        self.openHomeScreen()

    def selectPhoto(self):
        pathToHome = os.path.expanduser('~')
        selectedPhoto, _ = QtWidgets.QFileDialog.getOpenFileName(self.AddMedicalScreen, "select Photo", pathToHome,
                                                                 "Image Files (*.png *.jpg *.jpeg)")
        if not selectedPhoto == "":
            extension = selectedPhoto.split(".")
            fileName = selectedPhoto.split("/")
            self.photo = [
                ('image', (fileName[-1], open(selectedPhoto, 'rb'), 'image/' + extension[-1]))
            ]
            self.AddMedical.addPhoto.setText(fileName[-1])

    def checkValues(self):
        medicalName_text = self.AddMedical.medicalName.text()
        email_text = self.AddMedical.email.text()
        pincode_text = self.AddMedical.pincode.text()
        phoneNumber_text = self.AddMedical.phoneNumber.text()
        address_text = self.AddMedical.address.text()
        website_text = self.AddMedical.website.text()

        if len(medicalName_text.replace(" ", "")) == 0 or len(email_text.replace(" ", "")) == 0 or len(
                phoneNumber_text.replace(" ", "")) == 0 or len(
            pincode_text.replace(" ", "")) == 0 or len(address_text.replace(" ", "")) == 0:
            self.AddMedical.message.setText("all filed are required!")
        else:
            self.AddMedical.message.setText("")
            if len(phoneNumber_text.replace(" ", "")) == 10:
                if phoneNumber_text.isnumeric():

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
                        self.valid = False
                        self.AddMedical.message.setText("Pincode must be numerical")
                    else:
                        self.valid = True
                else:
                    self.valid = False
                    self.AddMedical.message.setText("Pincode must be 6 digit long")
            else:
                self.AddMedical.phoneMessage.setText("phone number should be 10 digit long")
                self.valid = False
        if self.valid:
            pathToHome = os.path.expanduser('~')
            # loading the file which contain ipinfo such calling id lan and lon of the user
            with open(pathToHome + '/ipinfo.json', 'r') as f:
                ipinfo = json.load(f)
                f.close()

            calling_code = ipinfo.get('location')['country']['calling_code']
            lon = ipinfo.get('location')['longitude']
            lat = ipinfo.get('location')['latitude']
            phoneNumber = '+' + calling_code + phoneNumber_text
            # sending request to backend for creating the medical
            response = createMedical(
                {"name": medicalName_text, "pincode": pincode_text, "address": address_text,
                 "phone": phoneNumber,
                 "email": email_text,
                 "latitude": lat, "longitude": lon, "website": website_text}, file=self.photo)
            if response.status_code == 201:
                # loop = asyncio.new_event_loop()
                # coroutine = showMessage()
                asyncio.run(showMessage())
                self.widget.removeWidget(self.AddMedicalScreen)
                self.widget.removeWidget(self.homeScreen)
                self.openHomeScreen()

    @staticmethod
    def check(email):
        regex = re.compile(r'([A-Za-z\d]+[.-_])*[A-Za-z\d]+@[A-Za-z\d-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return True
        else:
            return False


async def showMessage():
    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Medical registered")
    message.setText("Registration done")
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.exec_()
