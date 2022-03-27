from PyQt5 import QtCore, QtGui, QtWidgets
from .functions.getData import getMyMedical

# importing frame
from .MyMedical import Ui_MyMedical
from .medicalProfile import Ui_MedicalProfile
from .addMedicine import Ui_AddMedicine


class Ui_HomePage(object):
    def __init__(self, widget):
        self.MedicalProfileScreen = QtWidgets.QDialog()
        self.MyMedicalScreen = QtWidgets.QDialog()
        self.homePage = None
        self.mainWidget = widget
        try:
            self.medicals = getMyMedical()
        except Exception as e:
            print(e)

    def setupUi(self, Dialog):
        self.homePage = Dialog
        self.homePage.setObjectName("Dialog")
        self.homePage.resize(900, 850)
        self.widget = QtWidgets.QWidget(self.homePage)
        self.widget.setGeometry(QtCore.QRect(0, 0, 901, 900))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(-1, 0, 901, 71))
        self.widget_2.setStyleSheet("background-color: rgb(0, 153, 112);")
        self.widget_2.setObjectName("widget_2")
        self.profile_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.profile_pushButton.setGeometry(QtCore.QRect(760, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.profile_pushButton.setFont(font)
        self.profile_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "color: rgb(10, 89, 83);\n"
                                              "border-radius:10px;")
        self.profile_pushButton.setObjectName("back_pushButton")
        self.profile_pushButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 901, 791))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 901, 791))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(55, 9, 55, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Add_medical = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Add_medical.sizePolicy().hasHeightForWidth())
        self.Add_medical.setSizePolicy(sizePolicy)
        self.Add_medical.setMinimumSize(QtCore.QSize(0, 250))
        self.Add_medical.setObjectName("Add_medical")
        self.label = QtWidgets.QLabel(self.Add_medical)
        self.label.setGeometry(QtCore.QRect(130, 50, 531, 91))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 153, 112);\n"
                                 "font-weight: 600;\n"
                                 "font-size: 23px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_pushButton = QtWidgets.QPushButton(self.Add_medical)
        self.add_pushButton.setGeometry(QtCore.QRect(240, 160, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_pushButton.setStyleSheet("background-color: rgb(0, 153, 112);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius:10px;")
        self.add_pushButton.setObjectName("add_pushButton")
        self.verticalLayout.addWidget(self.Add_medical)

        for medical in self.medicals.json():
            self.medical_widget = QtWidgets.QWidget(
                self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.medical_widget.sizePolicy().hasHeightForWidth())
            self.medical_widget.setSizePolicy(sizePolicy)
            self.medical_widget.setMinimumSize(QtCore.QSize(0, 250))
            self.medical_widget.setStyleSheet("border-radius:10px;\n"
                                              "background-color: rgb(0, 153, 112);")
            self.medical_widget.setObjectName(
                "medical_widget" + str(medical.get("medicalId")))
            self.label_2 = QtWidgets.QLabel(self.medical_widget)
            self.label_2.setGeometry(QtCore.QRect(30, 30, 67, 17))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.medical_widget)
            self.label_3.setGeometry(QtCore.QRect(30, 80, 81, 17))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.medical_widget)
            self.label_4.setGeometry(QtCore.QRect(30, 120, 91, 17))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_4.setFont(font)
            self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_4.setObjectName("label_4")
            self.shopName_text = QtWidgets.QLabel(self.medical_widget)
            self.shopName_text.setGeometry(QtCore.QRect(130, 30, 281, 21))
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            self.shopName_text.setFont(font)
            self.shopName_text.setStyleSheet("color: rgb(255, 255, 255);")
            self.shopName_text.setText(str(medical.get("name")))
            self.shopName_text.setObjectName(
                "shopName_" + str(medical.get("name")))
            self.address_text = QtWidgets.QLabel(self.medical_widget)
            self.address_text.setGeometry(QtCore.QRect(130, 70, 361, 31))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.address_text.setFont(font)
            self.address_text.setStyleSheet("color: rgb(255, 255, 255);")
            self.address_text.setText(str(medical.get("address")))
            self.address_text.setObjectName(
                "address_" + str(medical.get("address")))
            self.phoneNumber_text = QtWidgets.QLabel(self.medical_widget)
            self.phoneNumber_text.setGeometry(QtCore.QRect(130, 120, 151, 21))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.phoneNumber_text.setFont(font)
            self.phoneNumber_text.setStyleSheet("color: rgb(255, 255, 255);")
            self.phoneNumber_text.setText(str(medical.get("phone")))
            self.phoneNumber_text.setObjectName("phoneNumber_text")
            self.label_14 = QtWidgets.QLabel(self.medical_widget)
            self.label_14.setGeometry(QtCore.QRect(30, 160, 61, 31))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_14.setFont(font)
            self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_14.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.label_14.setObjectName("label_14")
            self.email_text = QtWidgets.QLabel(self.medical_widget)
            self.email_text.setGeometry(QtCore.QRect(130, 160, 221, 21))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.email_text.setFont(font)
            self.email_text.setStyleSheet("color: rgb(255, 255, 255);")
            self.email_text.setText(str(medical.get("email")))
            self.email_text.setObjectName("email_text")
            self.label_16 = QtWidgets.QLabel(self.medical_widget)
            self.label_16.setGeometry(QtCore.QRect(30, 210, 91, 17))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_16.setFont(font)
            self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_16.setObjectName("label_16")

            self.pincode_text = QtWidgets.QLabel(self.medical_widget)
            self.pincode_text.setGeometry(QtCore.QRect(130, 210, 91, 17))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pincode_text.setFont(font)
            self.pincode_text.setStyleSheet("color: rgb(255, 255, 255);")
            self.pincode_text.setText(str(medical.get("pincode")))
            self.pincode_text.setObjectName("pincode_text")

            self.view_pushButton = QtWidgets.QPushButton(self.medical_widget)
            self.view_pushButton.setGeometry(QtCore.QRect(630, 100, 81, 51))
            self.view_pushButton.setStyleSheet("color: rgb(0, 153, 112);\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "font-size: 18px;")
            self.view_pushButton.setObjectName(str(medical.get("medicalId")))
            self.view_pushButton.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.view_pushButton.clicked.connect(self.getShopId)

            self.verticalLayout.addWidget(self.medical_widget)
            self.label_2.setText("Name:")
            self.label_3.setText("Address:")
            self.label_4.setText("Phone No:")
            self.label_14.setText("Email:")
            self.label_16.setText("Pincode:")
            self.view_pushButton.setText("View")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.widget_2.raise_()

        self.retranslateUi(self.homePage)
        QtCore.QMetaObject.connectSlotsByName(self.homePage)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.profile_pushButton.setText(_translate("Dialog", "Profile"))
        self.label.setText(_translate("Dialog", "Add New Medical Shop!"))
        self.add_pushButton.setText(_translate("Dialog", "Add"))

    def getShopId(self):
        sender = self.widget.sender()
        _id = sender.objectName()
        self.openMyMedical(_id)

    def openMyMedical(self, _id):
        self.MyMedical = Ui_MyMedical()
        self.MyMedical.setupUi(self.MyMedicalScreen, self.mainWidget, _id)
        self.mainWidget.addWidget(self.MyMedicalScreen)
        self.mainWidget.removeWidget(self.homePage)
        self.MyMedical.pushButton_home.clicked.connect(self.MedicalToHome)
        self.MyMedical.pushButton_profile.clicked.connect(self.openProfile)
        self.MyMedical.pushButton_addMedicine.clicked.connect(self.addMedicines)

    def MedicalToHome(self):
        self.mainWidget.removeWidget(self.MyMedicalScreen)
        self.mainWidget.addWidget(self.homePage)

    def addMedicines(self):
        self.addMedicineScreen = QtWidgets.QDialog()
        self.addMedicine = Ui_AddMedicine(self.MyMedical.id)
        self.addMedicine.setupUi(self.addMedicineScreen)
        self.mainWidget.addWidget(self.addMedicineScreen)
        self.mainWidget.removeWidget(self.MyMedicalScreen)

    def openProfile(self):
        self.medicalProfile = Ui_MedicalProfile(self.MyMedical.id)
        self.medicalProfile.setupUi(self.MedicalProfileScreen)
        self.mainWidget.addWidget(self.MedicalProfileScreen)
        self.mainWidget.removeWidget(self.MyMedicalScreen)
        self.medicalProfile.back_button.clicked.connect(self.profileToMedical)

    def profileToMedical(self):
        self.mainWidget.removeWidget(self.MedicalProfileScreen)
        self.openMyMedical(self.medicalProfile.id)
