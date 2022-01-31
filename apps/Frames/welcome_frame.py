from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore


def welcomeFrame(grid):
    # inserting image


    image = QPixmap("images/capsule.png")
    icon = QLabel()
    icon.setPixmap(image)
    icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    icon.setStyleSheet(
        '''
        *{
            margin: 0;
            padding: 0;
            margin-top: 50px;
        }
        '''
    )

    # Welcome Quotes
    logo = QLabel()
    logo.setText("Get your Medicine !!")
    logo.setStyleSheet(  # style is given by using normal css
        '''
        *{
            color: #313552;
            font-family: "JetBrains Mono";
            font-size: 30px;
            font-weight: bold;
            padding:0;
            margin: 0;
            margin-bottom: 50px;
        }

    '''
    )

    # set the alignment
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
    # adding a TextBox
    text_box = QLineEdit()
    text_box.setPlaceholderText("Search Your Medicine")
    text_box.setMaximumWidth(500)
    text_box.setStyleSheet('''
        *{
            color: #313552;
            margin:0px;
            padding: 10px;
            outline: none;
            font-size: 18px;
            border: 3px solid #313552;
        }
        *::placeholder{
            color: #313540
        }
    ''')

    # add search button
    button = QPushButton("Search")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

    # added to grid

    grid.addWidget(icon, 0, 0, 1, 1)
    grid.addWidget(logo, 1, 0, 1, 1)
    grid.addWidget(text_box, 2, 0, 1, 1)

