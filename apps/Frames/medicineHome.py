from PyQt5 import QtCore, QtGui, QtWidgets

from .functions.getData import getMedicine, getMedicalDetails
from .editmedicine import Ui_editMedicine
from .functions.getData import deleteMedicine, updateMedicine
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QCompleter


class Ui_MedicineHome(object):
    def __init__(self, mainWidget, Dialog):
        self.mainWidget = mainWidget
        self.id = None
        self.medical = None
        self.medicines = None
        self.editMedicineScreen = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 854)
        self.myMedicalScreen = Dialog

    def storeDetails(self, _id):
        self.medicines = getMedicine(_id).json()
        self.medical = getMedicalDetails(_id)

    def setupUi(self, _id):
        self.id = _id
        try:
            self.storeDetails(_id)
            self.medicineList = []
            for medicine in self.medicines:
                self.medicineList.append(medicine.get("name"))
        except Exception as e:
            print("server Not Running")
            print(e)

        self.widget = QtWidgets.QWidget(self.myMedicalScreen)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 900, 70))
        self.widget_2.setStyleSheet("background-color: rgb(0, 156, 112);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 9, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.Home_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.Home_pushButton.setGeometry(QtCore.QRect(550, 20, 90, 35))
        self.Home_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 156, 112);\n"
                                           "border-radius:8px;")
        self.Home_pushButton.setObjectName("Home_pushButton")
        self.Addmedicine_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.Addmedicine_pushButton.setGeometry(QtCore.QRect(660, 20, 111, 35))
        self.Addmedicine_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "color: rgb(0, 156, 112);\n"
                                                  "border-radius:8px;")
        self.Addmedicine_pushButton.setObjectName("Addmedicine_pushButton")
        self.profile_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.profile_pushButton.setGeometry(QtCore.QRect(790, 20, 90, 35))
        self.profile_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "color: rgb(0, 156, 112);\n"
                                              "border-radius:8px;")
        self.profile_pushButton.setObjectName("profile_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 911, 771))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 911, 771))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(250, 250))
        self.widget_9.setObjectName("widget_9")
        self.search_input = QtWidgets.QLineEdit(self.widget_9)
        self.search_input.setGeometry(QtCore.QRect(280, 80, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_input.sizePolicy().hasHeightForWidth())
        self.search_input.setSizePolicy(sizePolicy)
        self.search_input.setStyleSheet("border: 2px solid rgb(45, 22, 90);\n"
                                        "border-top-left-radius: 10px;\n"
                                        "border-bottom-left-radius: 10px;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "font-size:18px;\n"
                                        "padding:2px 8px;\n"
                                        "")
        self.search_input.setObjectName("search_input")
        self.model = QStandardItemModel()
        completer = QCompleter(self.model, self.widget)
        self.search_input.setCompleter(completer)
        for i in self.medicineList:
            self.model.appendRow(QStandardItem(i))
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.search_button = QtWidgets.QPushButton(self.widget_9)
        self.search_button.setGeometry(QtCore.QRect(570, 80, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setStyleSheet("font-size: 25px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 156, 112);\n"
                                         "border-top-right-radius: 10px;\n"
                                         "border-bottom-right-radius: 10px;\n"
                                         "border:none;")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("apps/Frames/ui/../../images/search.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(18, 18))
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.sortList)
        self.verticalLayout.addWidget(self.widget_9)
        length = len(self.medicines)
        col = 3
        for i in range(0, length, col):
            if i > length - 1:
                break
            self.row = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.row.sizePolicy().hasHeightForWidth())
            self.row.setSizePolicy(sizePolicy)
            self.row.setMinimumSize(QtCore.QSize(250, 250))
            self.row.setObjectName("row")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.row)
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.verticalLayout.addWidget(self.row)
            for j in range(i, i + col):
                if j > length - 1:
                    break
                self.col = QtWidgets.QWidget(self.row)
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(200)
                sizePolicy.setVerticalStretch(200)
                sizePolicy.setHeightForWidth(
                    self.col.sizePolicy().hasHeightForWidth())
                self.col.setSizePolicy(sizePolicy)
                self.col.setMinimumSize(QtCore.QSize(250, 230))
                self.col.setStyleSheet("background-color: rgb(0, 156, 112);\n"
                                       "border-radius:15px;")
                self.col.setObjectName("col{}".format(
                    self.medicines[j].get('medicineId')))
                self.medicine_name = QtWidgets.QLabel(self.col)
                self.medicine_name.setGeometry(QtCore.QRect(20, 16, 231, 50))
                font.setPointSize(24)
                font.setBold(True)
                self.medicine_name.setFont(font)
                self.medicine_name.setStyleSheet("color: rgb(255, 255, 255);")
                self.medicine_name.setText(self.medicines[j].get('name'))
                self.medicine_name.setWordWrap(False)
                self.medicine_name.setObjectName("medicine_name")
                self.Description = QtWidgets.QLabel(self.col)
                self.Description.setGeometry(QtCore.QRect(20, 80, 231, 41))
                self.Description.setStyleSheet("color: rgb(255, 255, 255);")
                self.Description.setText(self.medicines[j].get('description'))
                self.Description.setObjectName("Description")
                self.Description.setWordWrap(True)
                self.quantity = QtWidgets.QLabel(self.col)
                self.quantity.setGeometry(QtCore.QRect(20, 140, 91, 21))
                self.quantity.setStyleSheet("color: rgb(255, 255, 255);")
                self.quantity.setText(str(self.medicines[j].get('quantity')))
                self.quantity.setObjectName("quantity")
                self.view_button = QtWidgets.QPushButton(self.col)
                self.view_button.setGeometry(QtCore.QRect(20, 180, 81, 31))
                self.view_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "color: rgb(0, 156, 112);\n"
                                               "border-radius:10px;")
                self.view_button.setObjectName(
                    str(self.medicines[j].get('medicineId')))
                self.view_button.setText("View")
                self.view_button.clicked.connect(self.openEditMedicine)
                self.horizontalLayout_3.addWidget(self.col)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(self.myMedicalScreen)
        QtCore.QMetaObject.connectSlotsByName(self.myMedicalScreen)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "MedAlthea"))
        self.Home_pushButton.setText(_translate("Dialog", "Home"))
        self.Addmedicine_pushButton.setText(
            _translate("Dialog", "Add Medicines"))
        self.profile_pushButton.setText(_translate("Dialog", "Profile"))
        self.search_input.setPlaceholderText(_translate("Dialog", "Search"))

    def openEditMedicine(self):
        sender = self.widget.sender()
        ID = sender.objectName()
        self.editMedicine = Ui_editMedicine(ID)
        self.editMedicine.setupUi(self.editMedicineScreen)
        self.mainWidget.addWidget(self.editMedicineScreen)
        self.mainWidget.removeWidget(self.myMedicalScreen)
        self.editMedicine.Back_pushButton.clicked.connect(
            self.backToMedicalPage)
        self.editMedicine.delete_button.clicked.connect(self.delete)
        self.editMedicine.add_button.clicked.connect(self.submit)

    def submit(self):
        medicineName_text = self.editMedicine.medicine_name.text()
        medicinePrice_text = self.editMedicine.medicine_price.text()
        medicineDescription_text = self.editMedicine.description.toPlainText()
        medicineQuantity_text = self.editMedicine.medicine_quantity.text()
        medicineDetails = {
            'medicalId': self.id,
            'name': medicineName_text,
            'description': medicineDescription_text,
            'price': medicinePrice_text,
            'quantity': medicineQuantity_text
        }
        if medicineName_text == self.editMedicine.medicine.get(
                'name') and medicinePrice_text == self.editMedicine.medicine.get(
            'price') and medicineQuantity_text == self.editMedicine.medicine.get(
            'quantity') and medicineDescription_text == self.editMedicine.medicine.get('description'):
            self.backToMedicalPage()
        else:
            response = updateMedicine(medicineDetails, self.editMedicine.ID)
            self.storeDetails(self.id)
            self.backToMedicalPage()
            showMessage(True if not response.status_code == 400 else False, 'Medicine Updated')

    def backToMedicalPage(self):
        self.mainWidget.addWidget(self.myMedicalScreen)
        self.mainWidget.removeWidget(self.editMedicineScreen)

    def delete(self):
        response = deleteMedicine(self.editMedicine.ID)
        self.storeDetails(self.id)
        self.backToMedicalPage()
        showMessage(True if response.status_code == 202 else False, 'Medicine Deleted')

    def sortList(self):
        text = self.search_input.text()
        if not text == "":
            length = len(self.medicines)
            length = length / 3
            length = int(length + 1) if type(length) is float else length
            for i in range(1, length + 1):
                row = self.verticalLayout.itemAt(i).widget()
                content = row.findChildren(
                    QtWidgets.QLabel, "medicine_name")
                count = 0
                for j in range(len(content)):
                    if not content[j].text() == text:
                        count += 1
                        content[j].parent().hide()
                if count == 3:
                    row.hide()


def showMessage(status, messages):
    message = QtWidgets.QMessageBox()
    message.setWindowTitle(messages if status else "Error")
    message.setText(messages if status else "Sorry something went wrong")
    message.setIcon(
        QtWidgets.QMessageBox.Information if status else QtWidgets.QMessageBox.Critical)
    message.exec_()
