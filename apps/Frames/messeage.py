from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Message(object):
    def setupUi(self, Dialog, text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(144, 112, 255);\n"
                                  "font: 36pt \"Times New Roman\";\n"
                                  "font-weight: 600;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 130, 900, 521))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
