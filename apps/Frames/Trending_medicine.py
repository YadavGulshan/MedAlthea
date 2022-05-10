from PyQt5 import QtCore, QtGui, QtWidgets


class Trending_Medicine(object):
    def setupUi(self, Dialog, TrendingMed):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 800)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 90, 891, 711))
        self.scrollArea.setAccessibleDescription("")
        self.scrollArea.setStyleSheet("border-color: rgb(16, 76, 42);\n"
                                      "border:none;\n"
                                      "border-radius:30px;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 891, 711))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(16, 76, 42);\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        no_of_med = len(TrendingMed)
        col = 2
        for i in range(0, no_of_med, col):

            if i > no_of_med - 1:
                break
            self.medicine_container = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.medicine_container.sizePolicy().hasHeightForWidth())
            self.medicine_container.setSizePolicy(sizePolicy)
            self.medicine_container.setMinimumSize(QtCore.QSize(0, 200))
            self.medicine_container.setObjectName("medicine_container")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.medicine_container)
            self.horizontalLayout.setObjectName("horizontalLayout")
            for j in range(i, i + col):
                if j > no_of_med - 1:
                    break
                self.medicne_widget = QtWidgets.QWidget(self.medicine_container)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.medicne_widget.sizePolicy().hasHeightForWidth())
                self.medicne_widget.setSizePolicy(sizePolicy)
                self.medicne_widget.setMinimumSize(QtCore.QSize(400, 0))
                self.medicne_widget.setStyleSheet("background-color: rgb(0, 153, 112);")
                self.medicne_widget.setObjectName("medicne_widget")
                self.medicine_name = QtWidgets.QLabel(self.medicne_widget)
                self.medicine_name.setGeometry(QtCore.QRect(4, 5, 391, 171))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                self.medicine_name.setFont(font)
                self.medicine_name.setStyleSheet("color: rgb(255, 255, 255);")
                self.medicine_name.setText((TrendingMed[j].get("name")).upper())
                self.medicine_name.setAlignment(QtCore.Qt.AlignCenter)
                self.medicine_name.setObjectName("medicine_name")
                self.horizontalLayout.addWidget(self.medicne_widget)
            self.verticalLayout.addWidget(self.medicine_container)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(770, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:12px;\n"
                                      "background-color: rgb(0, 153, 112);\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Medicines in Demand"))
        self.pushButton.setText(_translate("Dialog", "Back"))
