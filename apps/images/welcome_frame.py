from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit


def searchMedicine(text_box):
    print(text_box.text())


def welcomeFrame(grid):
    # inserting image
    image = QPixmap("images/capsule.png")
    icon = QLabel()
    icon.setPixmap(image)
    icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    icon.setStyleSheet(
        """
        *{
            margin: 0;
            padding: 0;
            margin-top: 50px;
        }
        """
    )

    # Welcome Quotes
    logo = QLabel()
    logo.setText("Get your Medicine !!")
    logo.setStyleSheet(  # style is given by using normal css
        """
        *{
            color: #313552;
            font-family: "JetBrains Mono";
            font-size: 30px;
            font-weight: bold;
            padding:0;
            margin: 0;
            margin-bottom: 50px;
        }

    """
    )

    # set the alignment
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
    # adding a TextBox
    text_box = QLineEdit()
    text_box.setPlaceholderText("Search Your Medicine")
    # text_box.setMaximumWidth(500)
    text_box.resize(80, 40)
    text_box.setStyleSheet(
        """
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
    """
    )
    # add search button
    button = QPushButton("Search")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.resize(10, 40)
    button.clicked.connect(lambda: searchMedicine(text_box))
    button.setStyleSheet(
        """
        *{
            color
            padding: 10px 10px;
            border: 3px solid #B8405E;
            border-radius: 24px;
            color: #B8405E;
            spacing: 20px;
        }
        *:hover{
            color: #EEE6CE;
            background-color: #B8405E ;

        }

        """
    )

    # added to grid

    grid.addWidget(icon, 0, 2, 1, 2)
    grid.addWidget(logo, 1, 2, 1, 2)
    grid.addWidget(text_box, 2, 2, 10, 1)
    grid.addWidget(button, 2, 3, 10, 1)
