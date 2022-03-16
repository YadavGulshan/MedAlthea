from PyQt5 import QtCore, QtGui, QtWidgets
from .functions.getData import getMedicalDetails


class Ui_MedicalProfile(object):
    def __init__(self, _id):
        self.is_editable = True
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
        self.fname = QtWidgets.QLineEdit(self.mainFrame)
        self.fname.setGeometry(QtCore.QRect(20, 360, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fname.setFont(font)
        self.fname.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")

        self.fname.setReadOnly(self.is_editable)
        self.fname.setObjectName("fname")
        self.fname.setText(self.response.get("name"))
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
        self.edit_button = QtWidgets.QPushButton(self.mainFrame)
        self.edit_button.setEnabled(self.is_editable)
        self.edit_button.setGeometry(QtCore.QRect(610, 710, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("border-radius:10px;\n"
                                       "color: white;\n"
                                       "background-color: rgb(0, 153, 112);\n"
                                       "\n"
                                       "")
        self.edit_button.setObjectName("edit_button")
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
        self.lname = QtWidgets.QLineEdit(self.mainFrame)
        self.lname.setGeometry(QtCore.QRect(20, 440, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lname.setFont(font)
        self.lname.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                 "border-radius:20px;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);")
        self.lname.setReadOnly(self.is_editable)
        self.lname.setText(self.response.get("last_name"))
        self.lname.setObjectName("lname")
        self.zipcode = QtWidgets.QLineEdit(self.mainFrame)
        self.zipcode.setGeometry(QtCore.QRect(470, 440, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zipcode.setFont(font)
        self.zipcode.setStyleSheet("border:2px solid rgb(0,0,0);\n"
                                   "border-radius:20px;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);")
        self.zipcode.setReadOnly(self.is_editable)
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
        self.address.setReadOnly(self.is_editable)
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
        self.phonenumber.setReadOnly(self.is_editable)

        self.phonenumber.setText(self.response.get("phone"))

        self.phonenumber.setObjectName("phonenumber")
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
        self.email.setReadOnly(self.is_editable)
        self.email.setObjectName("email")
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
        self.fname.setPlaceholderText(_translate("Dialog", "first Name"))
        self.edit_button.setText(_translate("Dialog", "Edit Profile"))
        self.delete_button.setText(_translate("Dialog", "delete Medical"))
        self.lname.setPlaceholderText(_translate("Dialog", "last Name"))
        self.zipcode.setPlaceholderText(_translate("Dialog", "pincode / zip code"))
        self.address.setPlaceholderText(_translate("Dialog", "Address"))
        self.phonenumber.setPlaceholderText(_translate("Dialog", "Phone Number"))
        self.email.setPlaceholderText(_translate("Dialog", "email"))
        self.back_button.setText(_translate("Dialog", "Back"))
