from PyQt5 import QtCore, QtGui, QtWidgets
import functions
from .signUp import signUpFrame


class LoginFrame(object):
    def __init__(self, widget1):
        self.widgetstacket = widget1

    def setupUi(self, PharmaServices):
        PharmaServices.setObjectName("loginscreen")
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
        self.UserName = QtWidgets.QLineEdit(self.widget)
        self.UserName.setGeometry(QtCore.QRect(280, 260, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet(
            "border:2px solid rgb(85, 0, 255);\n"
            "border-radius:20px;\n"
            "border:2px solid black;\n"
            "padding:10px;\n"
            "color: rgb(52, 52, 52);\n"
            "\n"
            ""
        )
        self.UserName.setText("")
        self.UserName.setObjectName("Email")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(280, 350, 331, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Password.setFont(font)
        self.Password.setStyleSheet(
            "border:2px solid rgb(85, 0, 255);\n"
            "border-radius:20px;\n"
            "border:2px solid black;\n"
            "padding:10px;\n"
            "color: rgb(52, 52, 52);\n"
            "\n"
            ""
        )
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.SignIn_button = QtWidgets.QPushButton(self.widget)
        self.SignIn_button.setGeometry(QtCore.QRect(280, 440, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SignIn_button.setFont(font)
        self.SignIn_button.setStyleSheet(
            "*{border-radius:20px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 0, 255);}\n"
            "*:hover{\n"
            "    background-color: rgb(85, 85, 255);\n"
            "}"
        )
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
        self.signup.setStyleSheet(
            "*{border-radius:20px;\n"
            "border:none;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 0, 255);}\n"
            "*:hover{\n"
            "    background-color: rgb(85, 85, 255);\n"
            "}"
        )
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
        PharmaServices.setTabOrder(self.Password, self.UserName)

        # click events on button
        self.SignIn_button.clicked.connect(self.getLogin)
        self.signup.clicked.connect(self.OpenSignUp)

    def retranslateUi(self, PharmaServices):
        _translate = QtCore.QCoreApplication.translate
        PharmaServices.setWindowTitle(_translate("loginscreen", "Pharma Services"))
        self.Title.setText(_translate("loginscreen", "LOGIN"))
        self.UserName.setPlaceholderText(_translate("loginscreen", "User Name"))
        self.Password.setPlaceholderText(_translate("loginscreen", "Password"))
        self.SignIn_button.setText(_translate("loginscreen", "SIGN IN"))
        self.label_4.setText(_translate("loginscreen", "Not a member yet?"))
        self.signup.setText(_translate("loginscreen", "Signup"))

    def getLogin(self):
        userName_text = self.UserName.text()
        password_text = self.Password.text()
        if len(userName_text) == 0 or len(password_text)==0:
            self.message.setText("All Field are required!")
        else:
            self.message.setText("")
            token = functions.getLogin.getTokens(userName_text, password_text)
            if token.status_code == 200:
                print("success!")
            else:
                self.message.setText("UserName Or Password is incorrect ")

    def OpenSignUp(self):
        print("get clicked")
        signUpScreen = QtWidgets.QDialog()
        signUp = signUpFrame()
        signUp.setupUi(signUpScreen)
        self.widgetstacket.addWidget(signUpScreen)
