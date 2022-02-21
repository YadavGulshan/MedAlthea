from PyQt5 import QtCore, QtGui, QtWidgets
from .functions.localdb import LocalDB
from .functions.getData import allMedicalShop
import DateTime


class Ui_Form(object):
    def __init__(self):
        self.db = LocalDB()
        tokens = self.db.getTokens()
        refreshLastUsed = DateTime.DateTime(tokens[0][1])
        today = DateTime.DateTime()
        self.day = today - refreshLastUsed
        self.medialShops = allMedicalShop()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 850)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 851, 134))
        self.label.setStyleSheet("color: rgb(41, 47, 127);\n"
                                 "font: 600 13pt \"Source Serif Pro\";\n"
                                 "font-size: 48px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 270, 281, 51))
        self.lineEdit.setStyleSheet("*{border-top-left-radius: 10px;\n"
                                    "border-bottom-left-radius: 10px;\n"
                                    "border: 1px solid rgb(104, 110, 171);\n"
                                    "color: rgb(41, 41, 41);\n"
                                    "padding: 5px;\n"
                                    "padding-left: 15px;\n"
                                    "font-size: 15px;}\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 270, 71, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font-size: 25px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(104, 110, 171);\n"
                                      "border-top-right-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px;\n"
                                      "border:none;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Frames/../images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 430, 901, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setToolTip("")
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 901, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 9)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # shop container

        for i in self.medialShops.json():
            address = "address_"
            container = "shop_"
            shopname = "shopName_"
            self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
            self.widget.setSizePolicy(sizePolicy)
            self.widget.setMinimumSize(QtCore.QSize(300, 250))
            self.widget.setStyleSheet("background-color: rgb(142, 154, 247);\n"
                                      "border-radius: 20px;")
            self.widget.setObjectName(container + str(i))
            self.Address = QtWidgets.QLabel(self.widget)
            self.Address.setGeometry(QtCore.QRect(0, 130, 301, 51))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.Address.setFont(font)
            self.Address.setStyleSheet("color: rgb(255, 255, 255);")
            self.Address.setAlignment(QtCore.Qt.AlignCenter)
            self.Address.setObjectName(address + str(i))
            self.pushButton_2 = QtWidgets.QPushButton(self.widget)
            self.pushButton_2.setGeometry(QtCore.QRect(90, 190, 121, 41))
            self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_2.setStyleSheet("background-color: rgb(104, 110, 171);\n"
                                            "color: rgb(254, 255, 255);")
            medicalID = i.get('medicalId')
            self.pushButton_2.setObjectName(str(medicalID))
            self.shopName = QtWidgets.QLabel(self.widget)
            self.shopName.setGeometry(QtCore.QRect(0, 0, 301, 121))
            font.setPointSize(32)
            self.shopName.setFont(font)
            self.shopName.setAlignment(QtCore.Qt.AlignCenter)
            self.shopName.setObjectName("{0}{1}".format(shopname, i))
            self.horizontalLayout.addWidget(self.widget)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.Address.setText(i.get("address"))
            self.pushButton_2.setText("Know More..")
            self.shopName.setText(i.get("name").capitalize())
            self.pushButton_2.clicked.connect(self.getShopInfo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PharmaServices"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Search on click </p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "search......"))

    def getShopInfo(self):
        sender = self.widget.sender()
