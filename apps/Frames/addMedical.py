from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMedical(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.medicalName = QtWidgets.QLineEdit(self.widget)
        self.medicalName.setGeometry(QtCore.QRect(70, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.medicalName.setFont(font)
        self.medicalName.setStyleSheet("border-radius:20px;\n"
                                       "border:2px solid black;\n"
                                       "padding:10px;\n"
                                       "color: rgb(52, 52, 52);\n"
                                       "\n"
                                       "")
        self.medicalName.setText("")
        self.medicalName.setObjectName("medicalName")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(70, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.email.setFont(font)
        self.email.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                 "border-radius:20px;\n"
                                 "border:2px solid black;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);\n"
                                 "\n"
                                 "")
        self.email.setText("")
        self.email.setObjectName("email")
        self.pincode = QtWidgets.QLineEdit(self.widget)
        self.pincode.setGeometry(QtCore.QRect(70, 490, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pincode.setFont(font)
        self.pincode.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.pincode.setText("")
        self.pincode.setObjectName("pincode")
        self.submit = QtWidgets.QPushButton(self.widget)
        self.submit.setGeometry(QtCore.QRect(280, 650, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("border-radius:20px;\n"
                                  "background-color: rgb(0, 153, 112);\n"
                                  "color: rgb(255, 255, 255);")
        self.submit.setObjectName("submit")
        self.phoneNumber = QtWidgets.QLineEdit(self.widget)
        self.phoneNumber.setGeometry(QtCore.QRect(450, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.phoneNumber.setFont(font)
        self.phoneNumber.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                       "border-radius:20px;\n"
                                       "border:2px solid black;\n"
                                       "padding:10px;\n"
                                       "color: rgb(52, 52, 52);\n"
                                       "\n"
                                       "")
        self.phoneNumber.setText("")
        self.phoneNumber.setObjectName("phoneNumber")
        self.address = QtWidgets.QLineEdit(self.widget)
        self.address.setGeometry(QtCore.QRect(450, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.address.setFont(font)
        self.address.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.address.setText("")
        self.address.setObjectName("address")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 71))
        self.frame.setStyleSheet("background-color: rgb(0, 153, 112);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(16, 15, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("border-radius:10px;\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 153, 112);;")
        self.back.setObjectName("back")
        self.website = QtWidgets.QLineEdit(self.widget)
        self.website.setGeometry(QtCore.QRect(450, 490, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.website.setFont(font)
        self.website.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.website.setText("")
        self.website.setObjectName("website")
        self.addPhoto = QtWidgets.QPushButton(self.widget)
        self.addPhoto.setGeometry(QtCore.QRect(330, 560, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addPhoto.setFont(font)
        self.addPhoto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addPhoto.setStyleSheet("border-radius:20px;\n"
                                    "background-color: rgb(0, 153, 112);\n"
                                    "color: rgb(255, 255, 255);")
        self.addPhoto.setObjectName("addPhoto")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(260, 140, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:rgb(0, 153, 112);\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.message = QtWidgets.QLabel(self.widget)
        self.message.setGeometry(QtCore.QRect(337, 615, 221, 31))
        self.message.setStyleSheet("color: rgb(255, 21, 0);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.phoneMessage = QtWidgets.QLabel(self.widget)
        self.phoneMessage.setGeometry(QtCore.QRect(470, 360, 291, 31))
        self.phoneMessage.setStyleSheet("color: rgb(255, 21, 0);")
        self.phoneMessage.setText("")
        self.phoneMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneMessage.setObjectName("phoneMessage")
        self.emailMessage = QtWidgets.QLabel(self.widget)
        self.emailMessage.setGeometry(QtCore.QRect(90, 450, 271, 31))
        self.emailMessage.setStyleSheet("color: rgb(255, 21, 0);")
        self.emailMessage.setText("")
        self.emailMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.emailMessage.setObjectName("emailMessage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.medicalName.setPlaceholderText(_translate("Dialog", "Name*"))
        self.email.setPlaceholderText(_translate("Dialog", "Email*"))
        self.pincode.setPlaceholderText(_translate("Dialog", "Pincode*"))
        self.submit.setText(_translate("Dialog", "Create"))
        self.phoneNumber.setPlaceholderText(_translate("Dialog", "Phone*"))
        self.address.setPlaceholderText(_translate("Dialog", "Address*"))
        self.back.setText(_translate("Dialog", "Back"))
        self.website.setPlaceholderText(_translate("Dialog", "Website"))
        self.addPhoto.setText(_translate("Dialog", "Add photo"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "Create Medical Account"))

    def checkValues(self):
        self.medicalName_text = self.medicalName.text()
        self.email_text = self.email.text()
        self.pincode_text = self.pincode.text()
        self.phoneNumber_text = self.phoneNumber.text()
        self.address_text = self.address.text()
        self.website_text = self.website.text()
        # self.addPhoto_text = self.addPhoto.text()