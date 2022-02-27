from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(44, 44, 44);\n"
                                  "font-weight: 400;\n"
                                  "font-size: 20px;")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 900, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color: rgb(0, 161, 118);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(350, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.widget_2)
        self.back.setGeometry(QtCore.QRect(770, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.back.setFont(font)
        self.back.setStyleSheet("color: rgb(0, 170, 127);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "border-radius:10px;")
        self.back.setObjectName("back")
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setGeometry(QtCore.QRect(260, 190, 381, 51))
        self.name.setStyleSheet("border-radius: 10px;\n"
                                "border: 2px solid rgb(0, 170, 127);\n"
                                "padding : 2px 10px;")
        self.name.setText("")
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:4px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(90, 400, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:4px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(90, 290, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:4px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setGeometry(QtCore.QRect(520, 630, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius:12px;")
        self.save.setObjectName("save")
        self.delete_2 = QtWidgets.QPushButton(self.widget)
        self.delete_2.setGeometry(QtCore.QRect(670, 630, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius:12px;\n"
                                    "background-color: rgb(255, 89, 90);")
        self.delete_2.setObjectName("delete_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 290, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:4px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QLineEdit(self.widget)
        self.price.setGeometry(QtCore.QRect(550, 290, 91, 51))
        self.price.setStyleSheet("border-radius: 10px;\n"
                                 "border: 2px solid rgb(0, 170, 127);padding : 2px 10px;")
        self.price.setText("")
        self.price.setObjectName("price")
        self.quatity = QtWidgets.QLineEdit(self.widget)
        self.quatity.setGeometry(QtCore.QRect(260, 290, 91, 51))
        self.quatity.setStyleSheet("border-radius: 10px;\n"
                                   "border: 2px solid rgb(0, 170, 127);padding : 2px 10px;")
        self.quatity.setText("")
        self.quatity.setObjectName("quatity")
        self.description = QtWidgets.QPlainTextEdit(self.widget)
        self.description.setGeometry(QtCore.QRect(250, 400, 381, 81))
        self.description.setStyleSheet("border-radius: 10px;\n"
                                       "border: 2px solid rgb(0, 170, 127);padding : 2px 10px;")
        self.description.setPlainText("")
        self.description.setObjectName("description")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Medicines!"))
        self.back.setText(_translate("Dialog", "Back"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Description:"))
        self.label_4.setText(_translate("Dialog", "Quatity"))
        self.save.setText(_translate("Dialog", "Save"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.label_5.setText(_translate("Dialog", "Price"))
