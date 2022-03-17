from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import folium
import io,sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 850)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 850))
        self.widget.setObjectName("widget")
        coorodinates = (19.26798680248383, 72.96750174465166)
        m = folium.Map(title="Map",location=coorodinates, zoom_start=12)
        data = io.BytesIO()
        m.save(data, close_file=False)
        webview = QWebEngineView(self.widget)
        webview.setHtml(data.getvalue().decode('utf-8'))
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


App = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(900)
widget.setFixedHeight(850)
widget.show()
mapSreen = QtWidgets.QDialog()

map = Ui_Dialog()
map.setupUi(mapSreen)
widget.addWidget(mapSreen)

sys.exit(App.exec_())