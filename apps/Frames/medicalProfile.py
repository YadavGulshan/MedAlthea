import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from .functions.getData import getMedicalDetails


class Ui_MedicalProfile(object):
    def __init__(self, _id):
        self.is_editable = False
        self.id = _id
        try:
            self.response = getMedicalDetails(self.id)
        except Exception as e:
            print(e)
            print("server not  running")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setObjectName("widget")
        self.titleFrame = QtWidgets.QFrame(self.widget)
        self.titleFrame.setGeometry(QtCore.QRect(0, 0, 901, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleFrame.setFont(font)
        self.titleFrame.setStyleSheet("background-color: rgb(0, 153, 112);")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.title = QtWidgets.QLabel(self.titleFrame)
        self.title.setGeometry(QtCore.QRect(20, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet("color:white;")
        self.title.setObjectName("title")
        self.mainFrame = QtWidgets.QFrame(self.widget)
        self.mainFrame.setGeometry(QtCore.QRect(0, 70, 900, 850))
        self.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.shopeName = QtWidgets.QLineEdit(self.mainFrame)
        self.shopeName.setGeometry(QtCore.QRect(20, 360, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shopeName.setFont(font)
        self.shopeName.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                     "border-radius:20px;\n"
                                     "padding:10px;\n"
                                     "color: rgb(52, 52, 52);")

        self.shopeName.setObjectName("shopName")
        self.shopeName.setText(self.response.get("name"))
        self.profile_picture = QtWidgets.QLabel(self.mainFrame)
        self.profile_picture.setGeometry(QtCore.QRect(360, 80, 180, 180))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.profile_picture.setFont(font)
        self.profile_picture.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                           "color: rgb(52, 52, 52);\n"
                                           "\n"
                                           "")
        self.profile_picture.setText("")
        self.profile_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_picture.setObjectName("profile_picture")
        url_image = 'https://live.staticflickr.com/65535/49251422908_591245c64a_c_d.jpg'
        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        self.profile_picture.setPixmap(QPixmap(image))
        self.save_button = QtWidgets.QPushButton(self.mainFrame)
        self.save_button.setGeometry(QtCore.QRect(610, 710, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("border-radius:10px;\n"
                                       "color: white;\n"
                                       "background-color: rgb(0, 153, 112);\n"
                                       "\n"
                                       "")
        self.save_button.setObjectName("edit_button")
        self.delete_button = QtWidgets.QPushButton(self.mainFrame)
        self.delete_button.setEnabled(True)
        self.delete_button.setGeometry(QtCore.QRect(740, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("border-radius:10px;\n"
                                         "color: white;\n"
                                         "background-color: rgb(255, 89, 91);\n"
                                         "font-weight: 500;\n"
                                         "\n"
                                         "")
        self.delete_button.setObjectName("delete_button")
        self.website = QtWidgets.QLineEdit(self.mainFrame)
        self.website.setGeometry(QtCore.QRect(20, 440, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.website.setFont(font)
        self.website.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.website.setText(self.response.get("website"))
        self.website.setObjectName("website")
        self.zipcode = QtWidgets.QLineEdit(self.mainFrame)
        self.zipcode.setGeometry(QtCore.QRect(470, 440, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zipcode.setFont(font)
        self.zipcode.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.zipcode.setObjectName("zipcode")
        self.zipcode.setText(str(self.response.get("pincode")))
        self.address = QtWidgets.QLineEdit(self.mainFrame)
        self.address.setGeometry(QtCore.QRect(470, 360, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.address.setFont(font)
        self.address.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.address.setObjectName("address")
        self.address.setText(self.response.get("address"))
        self.phonenumber = QtWidgets.QLineEdit(self.mainFrame)
        self.phonenumber.setGeometry(QtCore.QRect(20, 520, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.phonenumber.setFont(font)
        self.phonenumber.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                       "border-radius:20px;\n"
                                       "padding:10px;\n"
                                       "color: rgb(52, 52, 52);")

        self.phonenumber.setText(self.response.get("phone"))

        self.phonenumber.setObjectName("phonenumber")
        self.phonenumber.setReadOnly(True)
        self.email = QtWidgets.QLineEdit(self.mainFrame)
        self.email.setGeometry(QtCore.QRect(470, 520, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email.setFont(font)
        self.email.setStyleSheet("border:2px solid rgb(0, 0, 0);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")
        self.email.setText(self.response.get("email"))
        self.email.setObjectName("email")
        self.email.setReadOnly(True)
        self.back_button = QtWidgets.QPushButton(self.mainFrame)
        self.back_button.setGeometry(QtCore.QRect(480, 710, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("border-radius:10px;\n"
                                       "color: white;\n"
                                       "background-color: rgb(0, 153, 112);\n"
                                       "\n"
                                       "")
        self.back_button.setObjectName("save_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "Medical details"))
        self.shopeName.setPlaceholderText(_translate("Dialog", "first Name"))
        self.save_button.setText(_translate("Dialog", "Save Profile"))
        self.delete_button.setText(_translate("Dialog", "delete Medical"))
        self.website.setPlaceholderText(_translate("Dialog", "Website"))
        self.zipcode.setPlaceholderText(_translate("Dialog", "pincode / zip code"))
        self.address.setPlaceholderText(_translate("Dialog", "Address"))
        self.phonenumber.setPlaceholderText(_translate("Dialog", "Phone Number"))
        self.email.setPlaceholderText(_translate("Dialog", "email"))
        self.back_button.setText(_translate("Dialog", "Back"))

    def updateProfile(self):
        medicalProfile = {}
        submit = []
        if int(self.zipcode.text()) == self.response.get('pincode') and self.address.text() == self.response.get(
                'address') and self.shopeName.text() == self.response.get("name") and self.website.text() == self.response.get(
                'website'):
            submit.append(False)
            print("hello")
        else:
            submit.append(True)
            medicalProfile = {'medicalId': self.response.get('medicalId'), 'name': self.shopeName.text(),
                              'website': self.website.text(), 'address': self.address.text(),
                              "latitude": self.response.get('latitude'),
                              "longitude": self.response.get('longitude'), 'pincode': int(self.zipcode.text())}
        return submit, medicalProfile
