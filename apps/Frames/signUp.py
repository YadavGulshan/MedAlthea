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
        self.Title.setGeometry(QtCore.QRect(410, 210, 105, 33))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(0, 0, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Email = QtWidgets.QLineEdit(self.widget)
        self.Email.setGeometry(QtCore.QRect(500, 310, 330, 50))
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
        self.Password.setGeometry(QtCore.QRect(500, 400, 331, 50))
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
        self.SignIn_button.setGeometry(QtCore.QRect(310, 620, 321, 41))
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
        self.label_4.setGeometry(QtCore.QRect(340, 690, 127, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.signup = QtWidgets.QPushButton(self.widget)
        self.signup.setGeometry(QtCore.QRect(500, 680, 101, 41))
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
        self.message.setGeometry(QtCore.QRect(340, 560, 271, 16))
        self.message.setStyleSheet("color: rgb(194, 0, 0);")
        self.message.setText("")
        self.message.setObjectName("message")
        self.Email_2 = QtWidgets.QLineEdit(self.widget)
        self.Email_2.setGeometry(QtCore.QRect(120, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Email_2.setFont(font)
        self.Email_2.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.Email_2.setText("")
        self.Email_2.setObjectName("Email_2")
        self.Email_3 = QtWidgets.QLineEdit(self.widget)
        self.Email_3.setGeometry(QtCore.QRect(120, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Email_3.setFont(font)
        self.Email_3.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.Email_3.setText("")
        self.Email_3.setObjectName("Email_3")
        self.Email_4 = QtWidgets.QLineEdit(self.widget)
        self.Email_4.setGeometry(QtCore.QRect(120, 490, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Email_4.setFont(font)
        self.Email_4.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                   "border-radius:20px;\n"
                                   "border:2px solid black;\n"
                                   "padding:10px;\n"
                                   "color: rgb(52, 52, 52);\n"
                                   "\n"
                                   "")
        self.Email_4.setText("")
        self.Email_4.setObjectName("Email_4")
        self.Password_2 = QtWidgets.QLineEdit(self.widget)
        self.Password_2.setGeometry(QtCore.QRect(500, 490, 331, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Password_2.setFont(font)
        self.Password_2.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                      "border-radius:20px;\n"
                                      "border:2px solid black;\n"
                                      "padding:10px;\n"
                                      "color: rgb(52, 52, 52);\n"
                                      "\n"
                                      "")
        self.Password_2.setText("")
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_2.setObjectName("Password_2")

        self.retranslateUi(PharmaServices)
        QtCore.QMetaObject.connectSlotsByName(PharmaServices)
        PharmaServices.setTabOrder(self.SignIn_button, self.signup)
        PharmaServices.setTabOrder(self.signup, self.Password)
        PharmaServices.setTabOrder(self.Password, self.Email)

    def retranslateUi(self, PharmaServices):
        _translate = QtCore.QCoreApplication.translate
        PharmaServices.setWindowTitle(_translate("PharmaServices", "Pharma Services"))
        self.Title.setText(_translate("PharmaServices", "Sign Up"))
        self.Email.setPlaceholderText(_translate("PharmaServices", "Email"))
        self.Password.setPlaceholderText(_translate("PharmaServices", "Password"))
        self.SignIn_button.setText(_translate("PharmaServices", "Sign Up"))
        self.label_4.setText(_translate("PharmaServices", "Not a member yet?"))
        self.signup.setText(_translate("PharmaServices", "Login"))
        self.Email_2.setPlaceholderText(_translate("PharmaServices", "Email"))
        self.Email_3.setPlaceholderText(_translate("PharmaServices", "Email"))
        self.Email_4.setPlaceholderText(_translate("PharmaServices", "Email"))
        self.Password_2.setPlaceholderText(_translate("PharmaServices", "Password"))
