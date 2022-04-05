from PyQt5 import QtCore, QtGui, QtWidgets
from .functions.getData import getUserDetails


class Ui_ownerProfile(object):

    def __init__(self, owner_profile):
        owner_profile.setObjectName("owner_profile")
        owner_profile.resize(900, 850)
        self.widget = QtWidgets.QWidget(owner_profile)
        self.firstname = None
        self.logout_button = QtWidgets.QPushButton(self.widget)

    def setupUi(self):
        self.response = getUserDetails().json()[0]
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.firstname = QtWidgets.QLineEdit(self.widget)
        self.lastname = QtWidgets.QLineEdit(self.widget)
        self.Title = QtWidgets.QLabel(self.widget)
        self.email = QtWidgets.QLineEdit(self.widget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.Title.setGeometry(QtCore.QRect(400, 180, 151, 61))
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(0, 0, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.firstname.setGeometry(QtCore.QRect(120, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.firstname.setFont(font)
        self.firstname.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                     "border-radius:20px;\n"
                                     "border:2px solid black;\n"
                                     "padding:10px;\n"
                                     "color: rgb(52, 52, 52);\n"
                                     "\n"
                                     "")
        self.firstname.setReadOnly(True)
        self.firstname.setObjectName("firstname")
        self.firstname.setText(self.response.get("first_name"))
        self.lastname.setGeometry(QtCore.QRect(500, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lastname.setFont(font)
        self.lastname.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                    "border-radius:20px;\n"
                                    "border:2px solid black;\n"
                                    "padding:10px;\n"
                                    "color: rgb(52, 52, 52);\n"
                                    "\n"
                                    "")
        self.lastname.setReadOnly(True)
        self.lastname.setObjectName("lastname")
        self.lastname.setText(self.response.get("last_name"))
        self.email.setGeometry(QtCore.QRect(120, 400, 330, 50))
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
        self.email.setReadOnly(True)
        self.email.setObjectName("email")
        self.email.setText(self.response.get("email"))
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(500, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username.setFont(font)
        self.username.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                    "border-radius:20px;\n"
                                    "border:2px solid black;\n"
                                    "padding:10px;\n"
                                    "color: rgb(52, 52, 52);\n"
                                    "\n"
                                    "")
        self.username.setReadOnly(True)
        self.username.setObjectName("username")
        self.username.setText(self.response.get("username"))
        self.logout_button.setGeometry(QtCore.QRect(310, 600, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logout_button.setFont(font)
        self.logout_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_button.setStyleSheet("border-radius:20px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 94, 69);")
        self.logout_button.setObjectName("logout_button")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(16, 15, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("border-radius:10px;\n"
                                "background-color: rgb(0, 94, 69);\n"
                                "color: rgb(255, 255, 255);")
        self.back.setObjectName("back")
        self.back.setText("Back")
        self.retranslateUi(self.widget)
        QtCore.QMetaObject.connectSlotsByName(self.widget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Title.setText(_translate("Dialog", "Profile"))
        self.firstname.setPlaceholderText(_translate("Dialog", "First Name"))
        self.lastname.setPlaceholderText(_translate("Dialog", "Last Name"))
        self.email.setPlaceholderText(_translate("Dialog", "Email"))
        self.username.setPlaceholderText(_translate("Dialog", "User Name"))
        self.logout_button.setText(_translate("Dialog", "Logout"))
