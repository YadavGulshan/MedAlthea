import sys


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# from Frames.login import loginform
from Frames.login import LoginFrame

# welcomeFrame(grid)


# initializing GUI application
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

loginScreen = QtWidgets.QDialog()
login = LoginFrame(widget)
login.setupUi(loginScreen)

# set height and width
widget.addWidget(loginScreen)
widget.setFixedWidth(900)
widget.setFixedHeight(850)

widget.show()
sys.exit(app.exec_())
