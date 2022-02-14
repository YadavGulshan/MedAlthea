from PyQt5 import QtCore, QtGui, QtWidgets


class signUpFrame(object):
    def setupUi(self, PharmaServices):
        PharmaServices.setObjectName("loginscreen")
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
        self.Signup_button = QtWidgets.QPushButton(self.widget)
        self.Signup_button.setGeometry(QtCore.QRect(310, 620, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Signup_button.setFont(font)
        self.Signup_button.setStyleSheet("*{border-radius:20px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(85, 0, 255);}\n"
                                         "*:hover{\n"
                                         "    background-color: rgb(85, 85, 255);\n"
                                         "}")
        self.Signup_button.setObjectName("SignIn_button")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(340, 690, 127, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(500, 680, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.login.setFont(font)
        self.login.setStyleSheet("*{border-radius:20px;\n"
                                  "border:none;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(85, 0, 255);}\n"
                                  "*:hover{\n"
                                  "    background-color: rgb(85, 85, 255);\n"
                                  "}")
        self.login.setObjectName("signup")
        self.message = QtWidgets.QLabel(self.widget)
        self.message.setGeometry(QtCore.QRect(340, 560, 271, 16))
        self.message.setStyleSheet("color: rgb(194, 0, 0);")
        self.message.setText("")
        self.message.setObjectName("message")
        self.l_name = QtWidgets.QLineEdit(self.widget)
        self.l_name.setGeometry(QtCore.QRect(120, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_name.setFont(font)
        self.l_name.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                  "border-radius:20px;\n"
                                  "border:2px solid black;\n"
                                  "padding:10px;\n"
                                  "color: rgb(52, 52, 52);\n"
                                  "\n"
                                  "")
        self.l_name.setText("")
        self.l_name.setObjectName("l_name")
        self.F_name = QtWidgets.QLineEdit(self.widget)
        self.F_name.setGeometry(QtCore.QRect(120, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.F_name.setFont(font)
        self.F_name.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                  "border-radius:20px;\n"
                                  "border:2px solid black;\n"
                                  "padding:10px;\n"
                                  "color: rgb(52, 52, 52);\n"
                                  "\n"
                                  "")
        self.F_name.setText("")
        self.F_name.setObjectName("F_name")
        self.city = QtWidgets.QLineEdit(self.widget)
        self.city.setGeometry(QtCore.QRect(120, 490, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.city.setFont(font)
        self.city.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                "border-radius:20px;\n"
                                "border:2px solid black;\n"
                                "padding:10px;\n"
                                "color: rgb(52, 52, 52);\n"
                                "\n"
                                "")
        self.city.setText("")
        self.city.setObjectName("city")
        self.C_Password = QtWidgets.QLineEdit(self.widget)
        self.C_Password.setGeometry(QtCore.QRect(500, 490, 331, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.C_Password.setFont(font)
        self.C_Password.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                      "border-radius:20px;\n"
                                      "border:2px solid black;\n"
                                      "padding:10px;\n"
                                      "color: rgb(52, 52, 52);\n"
                                      "\n"
                                      "")
        self.C_Password.setText("")
        self.C_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.C_Password.setObjectName("Password_2")

        self.retranslateUi(PharmaServices)
        QtCore.QMetaObject.connectSlotsByName(PharmaServices)
        PharmaServices.setTabOrder(self.Signup_button, self.login)
        PharmaServices.setTabOrder(self.login, self.Password)
        PharmaServices.setTabOrder(self.Password, self.Email)

    def retranslateUi(self, PharmaServices):
        _translate = QtCore.QCoreApplication.translate
        PharmaServices.setWindowTitle(_translate("loginscreen", "Pharma Services"))
        self.Title.setText(_translate("loginscreen", "Sign Up"))
        self.Email.setPlaceholderText(_translate("loginscreen", "Email"))
        self.Password.setPlaceholderText(_translate("loginscreen", "Password"))
        self.Signup_button.setText(_translate("loginscreen", "Sign Up"))
        self.label_4.setText(_translate("loginscreen", "Already a Member?"))
        self.login.setText(_translate("loginscreen", "Login"))
        self.l_name.setPlaceholderText(_translate("loginscreen", "Last Name"))
        self.F_name.setPlaceholderText(_translate("loginscreen", "First Name"))
        self.city.setPlaceholderText(_translate("loginscreen", "City"))
        self.C_Password.setPlaceholderText(_translate("loginscreen", "Confirm Password"))
