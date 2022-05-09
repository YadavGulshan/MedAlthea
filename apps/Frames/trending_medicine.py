from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Trending_Medicine(object):
    def setup(self, Dialog,TrendingMed):
        self.Dialog = Dialog
        sorted_TrendingMed = sorted(TrendingMed, key=lambda d: d["count"], reverse=True)
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        Dialog.setWindowTitle("Trendingmedicic")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("Medicines in Demand")
        self.label.setGeometry(QtCore.QRect(260, 40, 320, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(16, 76, 42);\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 110, 811, 721))
        self.scrollArea.setAccessibleDescription("")
        self.scrollArea.setStyleSheet("border-color: rgb(16, 76, 42);border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 809, 719))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in sorted_TrendingMed:
            self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.widget.sizePolicy().hasHeightForWidth())
            self.widget.setSizePolicy(sizePolicy)
            self.widget.setMinimumSize(QtCore.QSize(0, 100))
            self.widget.setStyleSheet("background-color: rgb(16, 76, 42);\n"
                                    "border-radius:25px;\n"
                                    "")
            self.widget.setObjectName("widget")
            self.label_2 = QtWidgets.QLabel(self.widget)
            self.label_2.setText(i.get("name"))
            self.label_2.setGeometry(QtCore.QRect(10, 30, 681, 41))
            font.setPointSize(16)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_2.setObjectName("label_2")
            self.verticalLayout.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

