from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userHomePage(object):
    def setupUi(self, userHomePage):
        userHomePage.setObjectName("userHomePage")
        userHomePage.resize(900, 850)
        self.widget = QtWidgets.QWidget(userHomePage)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.profile = QtWidgets.QPushButton(self.widget)
        self.profile.setGeometry(QtCore.QRect(784, 12, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.profile.setFont(font)
        self.profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profile.setStyleSheet("border-radius:10px;\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "color: rgb(56, 136, 122);\n"
                                   "font-size:16px;")
        self.profile.setObjectName("profile")
        self.findIt = QtWidgets.QPushButton(self.widget)
        self.findIt.setGeometry(QtCore.QRect(590, 400, 81, 61))
        self.findIt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findIt.setMouseTracking(False)
        self.findIt.setStyleSheet("font-size: 25px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: #38887A;\n"
                                  "background-color: rgb(0, 170, 127);\n"
                                  "border-top-right-radius: 13px;\n"
                                  "border-bottom-right-radius: 13px;\n"
                                  "border:none;")
        self.findIt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("apps/Frames/ui/../../images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.findIt.setIcon(icon)
        self.findIt.setIconSize(QtCore.QSize(30, 30))
        self.findIt.setObjectName("findIt")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 310, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 127);\n"
                                   "")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setGeometry(QtCore.QRect(200, 400, 391, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input.sizePolicy().hasHeightForWidth())
        self.search_input.setSizePolicy(sizePolicy)
        self.search_input.setStyleSheet("QLineEdit {border-top-left-radius: 10px;\n"
                                        "border-bottom-left-radius: 10px;\n"
                                        "font-size:28px;\n"
                                        "padding:2px 8px;\n"
                                        "border: 1px solid #000;\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QLineEdit::placeholder{\n"
                                        "color:rgb(127, 127, 128);\n"
                                        "}")
        self.search_input.setText("")
        self.search_input.setObjectName("search_input")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 901, 71))
        self.widget_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 0, 161, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font-size:20px;\n"
                                 "font-weight:bold;")
        self.label.setObjectName("label")
        self.widget_2.raise_()
        self.profile.raise_()
        self.findIt.raise_()
        self.label_2.raise_()
        self.search_input.raise_()

        self.retranslateUi(userHomePage)
        QtCore.QMetaObject.connectSlotsByName(userHomePage)

    def retranslateUi(self, userHomePage):
        _translate = QtCore.QCoreApplication.translate
        userHomePage.setWindowTitle(_translate("userHomePage", "userHomePage"))
        self.profile.setText(_translate("userHomePage", "Profile"))
        self.label_2.setText(_translate("userHomePage", "Search Your Medicines here!"))
        self.search_input.setPlaceholderText(_translate("userHomePage", "Type your Medicine...."))
        self.label.setText(_translate("userHomePage", "MedAlthea"))
