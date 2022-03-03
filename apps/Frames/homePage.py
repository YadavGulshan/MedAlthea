from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomePage(object):
    def __init__(self):
        self.view = None

    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(900, 850)
        self.widget = QtWidgets.QWidget(HomePage)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(30, 30, 30);\n"
                                 "background-color: rgb(0, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_home = QtWidgets.QPushButton(self.frame)
        self.pushButton_home.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_home.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:4px;")
        self.pushButton_home.setObjectName("pushButton_2")
        self.pushButton_profile = QtWidgets.QPushButton(self.frame)
        self.pushButton_profile.setGeometry(QtCore.QRect(470, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_profile.setFont(font)
        self.pushButton_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_profile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:4px;")
        self.pushButton_profile.setObjectName("pushButton_3")
        self.pushButton_myMedicine = QtWidgets.QPushButton(self.frame)
        self.pushButton_myMedicine.setGeometry(QtCore.QRect(600, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_myMedicine.setFont(font)
        self.pushButton_myMedicine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_myMedicine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:4px;\n"
                                        "")
        self.pushButton_myMedicine.setObjectName("pushButton_4")
        self.pushButton_addMedicine = QtWidgets.QPushButton(self.frame)
        self.pushButton_addMedicine.setGeometry(QtCore.QRect(760, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_addMedicine.setFont(font)
        self.pushButton_addMedicine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_addMedicine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:4px;\n"
                                        "")
        self.pushButton_addMedicine.setObjectName("pushButton_5")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(9, 90, 881, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("color: rgb(0, 226, 166);\n"
                                      "border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 881, 751))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(70, -1, 70, 9)
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_widget.sizePolicy().hasHeightForWidth())
        self.search_widget.setSizePolicy(sizePolicy)
        self.search_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.search_widget.setObjectName("search_widget")
        self.search_button = QtWidgets.QLineEdit(self.search_widget)
        self.search_button.setGeometry(QtCore.QRect(150, 110, 351, 51))
        self.search_button.setMaximumSize(QtCore.QSize(16777215, 300))
        self.search_button.setStyleSheet("*{border-top-left-radius: 10px;\n"
                                         "border-bottom-left-radius: 10px;\n"
                                         "border: 1px solid rgb(104, 110, 171);\n"
                                         "color: rgb(41, 41, 41);\n"
                                         "padding: 5px;\n"
                                         "padding-left: 15px;\n"
                                         "font-size: 15px;}\n"
                                         "*::placeholder{\n"
                                         "color: rgb(126, 126, 126);\n"
                                         "}")
        self.search_button.setObjectName("search_button")
        self.findIt = QtWidgets.QPushButton(self.search_widget)
        self.findIt.setGeometry(QtCore.QRect(500, 110, 71, 51))
        self.findIt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findIt.setStyleSheet("font-size: 25px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(104, 110, 171);\n"
                                  "background-color: rgb(0, 170, 127);\n"
                                  "border-top-right-radius: 10px;\n"
                                  "border-bottom-right-radius: 10px;\n"
                                  "border:none;")
        self.findIt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frames/../images/search.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.findIt.setIcon(icon)
        self.findIt.setIconSize(QtCore.QSize(20, 20))
        self.findIt.setObjectName("findIt")
        self.shop_name = QtWidgets.QLabel(self.search_widget)
        self.shop_name.setGeometry(QtCore.QRect(10, 30, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        self.shop_name.setFont(font)
        self.shop_name.setStyleSheet("color: rgb(0, 121, 89);")
        self.shop_name.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name.setObjectName("shop_name")
        self.verticalLayout.addWidget(self.search_widget)
        self.medicine_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.medicine_widget.sizePolicy().hasHeightForWidth())
        self.medicine_widget.setSizePolicy(sizePolicy)
        self.medicine_widget.setMinimumSize(QtCore.QSize(630, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.medicine_widget.setFont(font)
        self.medicine_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.medicine_widget.setStyleSheet("\n"
                                           "background-color: rgb(0, 94, 69);\n"
                                           "")
        self.medicine_widget.setObjectName("medicine_widget")
        self.medicine_name = QtWidgets.QLabel(self.medicine_widget)
        self.medicine_name.setGeometry(QtCore.QRect(30, 10, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.medicine_name.setFont(font)
        self.medicine_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font-weight: 700;\n"
                                         "font-size: 20px;")
        self.medicine_name.setObjectName("medicine_name")
        self.description = QtWidgets.QLabel(self.medicine_widget)
        self.description.setGeometry(QtCore.QRect(30, 70, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setStyleSheet("color: rgb(255, 255, 255);")
        self.description.setObjectName("description")
        self.view = QtWidgets.QPushButton(self.medicine_widget)
        self.view.setGeometry(QtCore.QRect(570, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.view.setFont(font)
        self.view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius:11px;\n"
                                "color: rgb(0, 94, 69);")
        self.view.setObjectName("view")
        self.status = QtWidgets.QLabel(self.medicine_widget)
        self.status.setGeometry(QtCore.QRect(520, 100, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.status.setFont(font)
        self.status.setStyleSheet("color: rgb(255, 255, 255);")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.medicine_widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.frame.raise_()

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "Home Page"))
        self.pushButton_home.setText(_translate("HomePage", "Home"))
        self.pushButton_profile.setText(_translate("HomePage", "Profile"))
        self.pushButton_myMedicine.setText(_translate("HomePage", "My Medicines"))
        self.pushButton_addMedicine.setText(_translate("HomePage", "Add Medicines"))
        self.search_button.setPlaceholderText(_translate("HomePage", "Search..."))
        self.shop_name.setText(_translate("HomePage", "MedAlthea"))
        self.medicine_name.setText(_translate("HomePage", "Medicine Name"))
        self.description.setText(_translate("HomePage", "Description"))
        self.view.setText(_translate("HomePage", "View"))
        self.status.setText(_translate("HomePage", "Available"))
