from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MedicalPr(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setObjectName("widget")
        self.titleFrame = QtWidgets.QFrame(self.widget)
        self.titleFrame.setGeometry(QtCore.QRect(0, 0, 901, 71))
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
        self.mainFrame.setGeometry(QtCore.QRect(0, 70, 901, 781))
        self.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.fname = QtWidgets.QLineEdit(self.mainFrame)
        self.fname.setGeometry(QtCore.QRect(20, 360, 411, 51))
        self.fname.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")
        self.fname.setReadOnly(True)
        self.fname.setObjectName("fname")
        self.profile_picture = QtWidgets.QLabel(self.mainFrame)
        self.profile_picture.setGeometry(QtCore.QRect(360, 80, 180, 180))
        self.profile_picture.setStyleSheet("border:2px solid  rgb(0, 153, 112); ;\n"
                                           "color: rgb(52, 52, 52);\n"
                                           "\n"
                                           "")
        self.profile_picture.setText("")
        self.profile_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_picture.setObjectName("profile_picture")
        self.edit_button = QtWidgets.QPushButton(self.mainFrame)
        self.edit_button.setEnabled(True)
        self.edit_button.setGeometry(QtCore.QRect(610, 710, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("border-radius:10px;\n"
                                       "color: white;\n"
                                       "background-color: rgb(0, 153, 112);\n"
                                       "\n"
                                       "")
        self.edit_button.setObjectName("edit_button")
        self.delete_button = QtWidgets.QPushButton(self.mainFrame)
        self.delete_button.setGeometry(QtCore.QRect(740, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("border-radius:10px;\n"
                                         "color: white;\n"
                                         "background-color: rgb(255, 89, 91);\n"
                                         "font-weight: 500;\n"
                                         "\n"
                                         "")
        self.delete_button.setObjectName("delete_button")
        self.lname = QtWidgets.QLineEdit(self.mainFrame)
        self.lname.setGeometry(QtCore.QRect(20, 440, 411, 51))
        self.lname.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")
        self.lname.setReadOnly(True)
        self.lname.setObjectName("lname")
        self.zipcode = QtWidgets.QLineEdit(self.mainFrame)
        self.zipcode.setGeometry(QtCore.QRect(470, 440, 411, 51))
        self.zipcode.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.zipcode.setReadOnly(True)
        self.zipcode.setObjectName("zipcode")
        self.address = QtWidgets.QLineEdit(self.mainFrame)
        self.address.setGeometry(QtCore.QRect(470, 360, 411, 51))
        self.address.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.address.setReadOnly(True)
        self.address.setObjectName("address")
        self.phonenumber = QtWidgets.QLineEdit(self.mainFrame)
        self.phonenumber.setGeometry(QtCore.QRect(20, 520, 411, 51))
        self.phonenumber.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                       "border-radius:20px;\n"
                                       "padding:10px;\n"
                                       "color: rgb(52, 52, 52);")
        self.phonenumber.setReadOnly(True)
        self.phonenumber.setObjectName("phonenumber")
        self.email = QtWidgets.QLineEdit(self.mainFrame)
        self.email.setGeometry(QtCore.QRect(470, 520, 411, 51))
        self.email.setStyleSheet("border:2px solid rgb(0, 153, 112);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")
        self.email.setReadOnly(True)
        self.email.setObjectName("email")
        self.save_button = QtWidgets.QPushButton(self.mainFrame)
        self.save_button.setGeometry(QtCore.QRect(610, 710, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("border-radius:10px;\n"
                                       "color: white;\n"
                                       "background-color: rgb(0, 153, 112);\n"
                                       "\n"
                                       "")
        self.save_button.setObjectName("save_button")
        self.logout_button = QtWidgets.QPushButton(self.mainFrame)
        self.logout_button.setGeometry(QtCore.QRect(750, 710, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("border-radius:10px;\n"
                                         "color: white;\n"
                                         "background-color: rgb(255, 89, 90);\n"
                                         "\n"
                                         "")
        self.logout_button.setObjectName("logout_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "Medical details"))
        self.fname.setPlaceholderText(_translate("Dialog", "first Name"))
        self.edit_button.setText(_translate("Dialog", "Edit Profile"))
        self.delete_button.setToolTip(
            _translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.delete_button.setWhatsThis(_translate("Dialog",
                                                   "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.delete_button.setText(_translate("Dialog", "delete Medical"))
        self.lname.setPlaceholderText(_translate("Dialog", "last Name"))
        self.zipcode.setPlaceholderText(_translate("Dialog", "pincode / zip code"))
        self.address.setPlaceholderText(_translate("Dialog", "Address"))
        self.phonenumber.setPlaceholderText(_translate("Dialog", "Phone Number"))
        self.email.setPlaceholderText(_translate("Dialog", "email"))
        self.save_button.setText(_translate("Dialog", "save"))
        self.logout_button.setToolTip(
            _translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.logout_button.setWhatsThis(_translate("Dialog",
                                                   "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.logout_button.setText(_translate("Dialog", "Logout"))
