from PyQt5 import QtCore, QtGui, QtWidgets
import re


class signUpFrame(object):
    def setupUi(self, signUp):
        signUp.setObjectName("signUp")
        signUp.resize(900, 850)
        self.widget = QtWidgets.QWidget(signUp)
        self.widget.setGeometry(QtCore.QRect(0, 0, 921, 850))
        self.widget.setStyleSheet("background-color :rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(390, 180, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(0, 0, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(490, 400, 331, 50))

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
        self.LoginIn_button = QtWidgets.QPushButton(self.widget)
        self.LoginIn_button.setGeometry(QtCore.QRect(310, 620, 321, 41))

        font.setPointSize(12)
        self.LoginIn_button.setFont(font)
        self.LoginIn_button.setStyleSheet("*{border-radius:20px;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(85, 0, 255);}\n"
                                          "*:hover{\n"
                                          "    background-color: rgb(85, 85, 255);\n"
                                          "}")
        self.LoginIn_button.setObjectName("SignIn_button")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(310, 680, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(500, 680, 121, 41))

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
        self.message.setGeometry(QtCore.QRect(340, 600, 271, 16))
        font = QtGui.QFont()
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(194, 0, 0);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.F_Name = QtWidgets.QLineEdit(self.widget)
        self.F_Name.setGeometry(QtCore.QRect(110, 400, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.F_Name.setFont(font)
        self.F_Name.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                  "border-radius:20px;\n"
                                  "border:2px solid black;\n"
                                  "padding:10px;\n"
                                  "color: rgb(52, 52, 52);\n"
                                  "\n"
                                  "")
        self.F_Name.setText("")
        self.F_Name.setObjectName("l_name")
        self.UserName = QtWidgets.QLineEdit(self.widget)
        self.UserName.setGeometry(QtCore.QRect(110, 310, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                    "border-radius:20px;\n"
                                    "border:2px solid black;\n"
                                    "padding:10px;\n"
                                    "color: rgb(52, 52, 52);\n"
                                    "\n"
                                    "")
        self.UserName.setText("")
        self.UserName.setObjectName("F_name")
        self.l_Name = QtWidgets.QLineEdit(self.widget)
        self.l_Name.setGeometry(QtCore.QRect(120, 490, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_Name.setFont(font)
        self.l_Name.setStyleSheet("border:2px solid rgb(85, 0, 255);\n"
                                  "border-radius:20px;\n"
                                  "border:2px solid black;\n"
                                  "padding:10px;\n"
                                  "color: rgb(52, 52, 52);\n"
                                  "\n"
                                  "")
        self.l_Name.setText("")
        self.l_Name.setObjectName("city")
        self.C_Password = QtWidgets.QLineEdit(self.widget)
        self.C_Password.setGeometry(QtCore.QRect(490, 490, 331, 50))
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
        self.checkBox.setGeometry(QtCore.QRect(410, 560, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(18, 18, 18);")
        self.checkBox.setObjectName("checkBox")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(500, 310, 330, 50))
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
        self.message_email = QtWidgets.QLabel(self.widget)
        self.message_email.setGeometry(QtCore.QRect(520, 370, 271, 16))
        font = QtGui.QFont()
        self.message_email.setFont(font)
        self.message_email.setStyleSheet("color: rgb(194, 0, 0);")
        self.message_email.setText("")
        self.message_email.setAlignment(QtCore.Qt.AlignCenter)
        self.message_email.setObjectName("message_email")
        self.message_pass = QtWidgets.QLabel(self.widget)
        self.message_pass.setGeometry(QtCore.QRect(520, 460, 271, 16))
        font = QtGui.QFont()
        self.message_pass.setFont(font)
        self.message_pass.setStyleSheet("color: rgb(194, 0, 0);")
        self.message_pass.setText("")
        self.message_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.message_pass.setObjectName("message_pass")

        self.retranslateUi(signUp)
        QtCore.QMetaObject.connectSlotsByName(signUp)
        signUp.setTabOrder(self.UserName, self.F_Name)
        signUp.setTabOrder(self.F_Name, self.l_Name)
        signUp.setTabOrder(self.l_Name, self.email)
        signUp.setTabOrder(self.email, self.Password)
        signUp.setTabOrder(self.Password, self.C_Password)

    def retranslateUi(self, signUp):
        _translate = QtCore.QCoreApplication.translate
        signUp.setWindowTitle(_translate("signUp", "Sign Up"))
        self.Title.setText(_translate("signUp", "Sign Up"))
        self.Password.setPlaceholderText(_translate("signUp", "Password"))
        self.LoginIn_button.setText(_translate("signUp", "Sign Up"))
        self.label_4.setText(_translate("signUp", "Already a member?"))
        self.login.setText(_translate("signUp", "Login"))
        self.F_Name.setPlaceholderText(_translate("signUp", "First Name"))
        self.UserName.setPlaceholderText(_translate("signUp", "UserName"))
        self.l_Name.setPlaceholderText(_translate("signUp", "Last Name"))
        self.C_Password.setPlaceholderText(_translate("signUp", "Confirm Password"))
        self.checkBox.setText(_translate("signUp", "Have A Shop ?"))
        self.email.setPlaceholderText(_translate("signUp", "Email"))

    def getSignUp(self):
        self.username_text = self.UserName.text()
        self.firstname_text = self.F_Name.text()
        self.lastname_text = self.l_Name.text()
        self.email_text = self.email.text()
        self.password_text = self.Password.text()
        self.c_password_text = self.C_Password.text()
        self.checkbox = self.checkBox.isChecked()

        valid = False

        if len(self.firstname_text) == 0 or len(self.lastname_text) == 0 or len(self.username_text) == 0 or len(
                self.email_text) == 0 or len(self.password_text) == 0 or len(self.c_password_text) == 0:
            self.message.setText("All fields are required")
        else:
            if not (len(self.password_text) >= 8):
                self.message_pass.setText("Password must have 8 characters")
                valid = False

            else:
                self.message_pass.setText("")
                valid = True
            if not (self.password_text == self.c_password_text):
                self.message_pass.setText("Password not match")
                valid = False

            else:
                self.message_pass.setText("")
                valid = True
            if not (self.check()):
                self.message_email.setText("Enter a valid email")
                valid = False
            else:
                self.message_email.setText("")
                valid = True

    def check(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, self.email_text):
            return True
        else:
            return False
