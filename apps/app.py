import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore

# initializing GUI application
app = QApplication(sys.argv)

# window and settings
window = QWidget()
# set the title to the window!
window.setWindowTitle("Get Your Medicine!!")
# set height and width
window.setFixedWidth(800)
# window.setFixedHeight(650)
# Set the location of window at desktop
window.move(400, 100)
window.setStyleSheet("background: #EEE6CE;")
# initialize the grid layout
grid = QGridLayout()


def welcomeFrame():
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
            margin: 0;
            
        }

    '''
    )

    # set the alignment
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    # adding a TextBox
    text_box = QLineEdit()
    text_box.setPlaceholderText("Search Your Medicine")
    text_box.setGeometry(100, 100, 200, 50)
    text_box.setFocus()
    text_box.setMaximumWidth(500)
    text_box.setStyleSheet('''
        *{
            color: #313552;
            margin:0px;
            
        }
        *::placeholder{
            color: #313540
        }
    ''')

    # added to grid

    grid.addWidget(icon, 0, 0)
    grid.addWidget(logo, 1, 0)
    grid.addWidget(text_box, 2, 0)


welcomeFrame()

window.setLayout(grid)

window.show()
sys.exit(app.exec_())
