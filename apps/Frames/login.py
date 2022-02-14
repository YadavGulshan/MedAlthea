from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PharmaServices(object):
    def setupUi(self, PharmaServices):
        PharmaServices.setObjectName("PharmaServices")
        PharmaServices.resize(900, 850)
        self.widget = QtWidgets.QWidget(PharmaServices)
        self.widget.setGeometry(QtCore.QRect(0, 0, 921, 850))
        self.widget.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(360, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(0, 0, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Email = QtWidgets.QLineEdit(self.widget)
        self.Email.setGeometry(QtCore.QRect(280, 260, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Email.setFont(font)
        self.Email.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                 "border-radius:20px;\n"
                                 "border:2px solid black;\n"
                                 "padding:10px;\n"
                                 "color: rgb(52, 52, 52);\n"
                                 "\n"
                                 "")
        self.Email.setText("")
        self.Email.setObjectName("Email")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(280, 350, 331, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Password.setFont(font)
        self.Password.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                    "border-radius:20px;\n"
                                    "border:2px solid black;\n"
                                    "padding:10px;\n"
                                    "color: rgb(52, 52, 52);\n"
                                    "\n"
                                    "")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.SignIn_button = QtWidgets.QPushButton(self.widget)
        self.SignIn_button.setGeometry(QtCore.QRect(280, 440, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SignIn_button.setFont(font)
        self.SignIn_button.setStyleSheet("*{border-radius:20px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(85, 0, 255);}\n"
                                         "*:hover{\n"
                                         "    background-color: rgb(85, 85, 255);\n"
                                         "}")
        self.SignIn_button.setObjectName("SignIn_button")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(340, 510, 127, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.signup = QtWidgets.QPushButton(self.widget)
        self.signup.setGeometry(QtCore.QRect(480, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.signup.setFont(font)
        self.signup.setStyleSheet("*{border-radius:20px;\n"
                                  "border:none;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(85, 0, 255);}\n"
                                  "*:hover{\n"
                                  "    background-color: rgb(85, 85, 255);\n"
                                  "}")
        self.signup.setObjectName("signup")
        self.message = QtWidgets.QLabel(self.widget)
        self.message.setGeometry(QtCore.QRect(310, 410, 271, 16))
        self.message.setStyleSheet("color: rgb(194, 0, 0);")
        self.message.setText("")
        self.message.setObjectName("message")

        self.retranslateUi(PharmaServices)
        QtCore.QMetaObject.connectSlotsByName(PharmaServices)
        PharmaServices.setTabOrder(self.SignIn_button, self.signup)
        PharmaServices.setTabOrder(self.signup, self.Password)
        PharmaServices.setTabOrder(self.Password, self.Email)

        # click events on button
        self.SignIn_button.clicked.connect(self.getLogin)
        self.signup.clicked.connect(self.OpenSignUp)

    def retranslateUi(self, PharmaServices):
        _translate = QtCore.QCoreApplication.translate
        PharmaServices.setWindowTitle(_translate("PharmaServices", "Pharma Services"))
        self.Title.setText(_translate("PharmaServices", "LOGIN"))
        self.Email.setPlaceholderText(_translate("PharmaServices", "Email"))
        self.Password.setPlaceholderText(_translate("PharmaServices", "Password"))
        self.SignIn_button.setText(_translate("PharmaServices", "SIGN IN"))
        self.label_4.setText(_translate("PharmaServices", "Not a member yet?"))
        self.signup.setText(_translate("PharmaServices", "Signup"))

    def getLogin(self):
        print("get clicked")

    def OpenSignUp(self):
        print("get clicked")