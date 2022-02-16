from PyQt5 import QtCore, QtGui, QtWidgets
# from .login import LoginFrame


class signUpFrame(object):
    def setupUi(self, signUp, Widget):
        self.Widget = Widget
        signUp.setObjectName("signUp")
        signUp.resize(900, 850)
        self.widget = QtWidgets.QWidget(signUp)
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
        self.label_4.setGeometry(QtCore.QRect(350, 690, 130, 18))
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
        self.login.setObjectName("login")
        self.message = QtWidgets.QLabel(self.widget)
        self.message.setGeometry(QtCore.QRect(330, 590, 271, 16))
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
        self.C_Password.setObjectName("C_Password")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(420, 560, 111, 22))
        self.checkBox.setStyleSheet("color: rgb(18, 18, 18);")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(signUp)
        QtCore.QMetaObject.connectSlotsByName(signUp)
        signUp.setTabOrder(self.F_name, self.l_name)
        signUp.setTabOrder(self.l_name, self.city)
        signUp.setTabOrder(self.Email, self.Password)
        signUp.setTabOrder(self.Password, self.C_Password)
        self.F_name.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.login.clicked.connect(self.loadLogin)


    def retranslateUi(self, signUp):
        _translate = QtCore.QCoreApplication.translate
        signUp.setWindowTitle(_translate("signUp", "Sign Up"))
        self.Title.setText(_translate("signUp", "Sign Up"))
        self.Email.setPlaceholderText(_translate("signUp", "Email"))
        self.Password.setPlaceholderText(_translate("signUp", "Password"))
        self.SignIn_button.setText(_translate("signUp", "Sign Up"))
        self.label_4.setText(_translate("signUp", "Already a member?"))
        self.login.setText(_translate("signUp", "Login"))
        self.l_name.setPlaceholderText(_translate("signUp", "Last Name"))
        self.F_name.setPlaceholderText(_translate("signUp", "First Name"))
        self.city.setPlaceholderText(_translate("signUp", "City"))
        self.C_Password.setPlaceholderText(_translate("signUp", "Confirm Password"))
        self.checkBox.setText(_translate("signUp", "Have A Shop ?"))

    def loadLogin(self):
        # loginScreen = QtWidgets.QDialog()
        # login = LoginFrame(self.Widget)
        # login.setupUi(loginScreen)
        print("click")
        self.Widget.setCurrentIndex(self.Widget.currentIndex() - 2)
