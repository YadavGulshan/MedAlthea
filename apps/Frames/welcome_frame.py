
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore


def welcomeFrame():
    logo = QLabel()
    logo.setText("Get your Medicine")
    # logo.setStyleSheet('''
    #     *{
    #         color: #D9534F;
    #         font-family: serif;
    #         font-weight: bold;
    #     }
    #     *:hover{
    #         color: #FFEEAD;
    #     }
    #
    # ''')
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
