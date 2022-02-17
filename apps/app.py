# importing depended modules
# from signal import SIGHUP
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import re

# importing LocalDb
from Frames.functions.localdb import LocalDB
from Frames.functions.getLogin import getTokens

# importing Frames
from Frames.login import LoginFrame
from Frames.searchFrame import Ui_Form
from Frames.signUp import signUpFrame

# initializing GUI application
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

# ---------- Creating .sqlit3 file in apps folder and making connection to local db --------#

# Crating object of local DB

DB = LocalDB()

# Here in Local we Have our tokens
# At first index we have refresh token
# At second index we have date and time of refresh token Last used
# At Third index we have Access token
# At Fourth index we have date and time of access token Last used

TOKENS = DB.getTokens()
# checking weather the user already login or not

if len(TOKENS) == 0:

    # initializing login screen
    loginScreen = QtWidgets.QDialog()
    login = LoginFrame()
    login.setupUi(loginScreen)
    widget.addWidget(loginScreen)

    # initializing signup screen
    signUpScreen = QtWidgets.QDialog()
    signUp = signUpFrame()
    signUp.setupUi(signUpScreen)

    def openLogin():
        widget.removeWidget(signUpScreen)
        widget.addWidget(loginScreen)

    def getSignUp():
        firstname_text=signUp.F_name.text()
        lastname_text=signUp.l_name.text()
        city_text=signUp.city.text()
        email_text=signUp.F_name.text()
        password_text=signUp.Password.text()
        c_password_text=signUp.C_Password.text()
        if len(firstname_text)==0 or len(lastname_text)==0 or len(city_text)==0 or len(email_text)==0 or len(password_text)==0 or len(c_password_text)==0:
            signUp.message.setText("All fields are required")
        else:
            if password_text==c_password_text:
                print("password match")
                if check(email_text):
                    print("Valid email")
                else:
                    print("Invalid email")
        
    def check(email):  
        regex = '/^w+[+.w-]*@([w-]+.)*w+[w-]*.([a-z]{2,4}|d+)$/i'

        if(re.search(regex,email)):  
            return True  
        else:  
            return False




        

        print('click')

    def openSignUp():
        widget.removeWidget(loginScreen)
        widget.addWidget(signUpScreen)

    def getLogin():
        username_text = login.UserName.text()
        password_text = login.Password.text()
        if len(username_text) == 0 or len(password_text) == 0:
            login.message.setText("All Field are required!")
        else:
            login.message.setText("")
            token = getTokens(username_text, password_text)
            if token.status_code == 200:
                print("success!")
            else:
                login.message.setText("UserName Or Password is incorrect ")

    # adding click events to buttons
    login.SignIn_button.clicked.connect(getLogin)
    login.signup.clicked.connect(openSignUp)
    signUp.LoginIn_button.clicked.connect(getSignUp)
    signUp.login.clicked.connect(openLogin)

else:
    searchScreen = QtWidgets.QDialog()
    search = Ui_Form()
    search.setupUi(searchScreen)
    widget.addWidget(searchScreen)







# set height and width
widget.setFixedWidth(900)
widget.setFixedHeight(850)
widget.show()
sys.exit(app.exec_())
