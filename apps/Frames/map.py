import sys
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shops are here')
        self.window_width, self.window_height = 900, 850
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (19.24582202982605, 73.01528706912977)
        m = folium.Map(
            zoom_start=13,
            location=coordinate
        )

        html = f"""
               <h1> {"kalher"}</h1>
               """
        iframe = folium.IFrame(html=html, width=200, height=200)
        popup = folium.Popup(iframe, max_width=560)
        folium.Marker(
            location=coordinate,
            popup=popup,
            icon=folium.DivIcon(html=f""" <div><svg width="30" height="30" viewBox="0 0 30 30" fill="none" 
            xmlns="http://www.w3.org/2000/svg"> <path d="M3.125 11.875H26.875V23.75H3.125V11.875Z" fill="#CFD8DC"/> 
            <path d="M3.125 23.75H26.875V26.25H3.125V23.75Z" fill="#B0BEC5"/> <path d="M16.875 
            15H24.375V26.25H16.875V15Z" fill="#455A64"/> <path d="M5.625 15H14.375V21.875H5.625V15Z" fill="#E3F2FD"/> 
            <path d="M6.25 15.625H13.75V21.25H6.25V15.625Z" fill="#1E88E5"/> <path d="M22.8125 20.9375C22.625 20.9375 
            22.5 21.0625 22.5 21.25V22.5C22.5 22.6875 22.625 22.8125 22.8125 22.8125C23 22.8125 23.125 22.6875 23.125 
            22.5V21.25C23.125 21.0625 23 20.9375 22.8125 20.9375Z" fill="#90A4AE"/> <path d="M15 13.75C16.0355 13.75 
            16.875 12.9105 16.875 11.875C16.875 10.8395 16.0355 10 15 10C13.9645 10 13.125 10.8395 13.125 
            11.875C13.125 12.9105 13.9645 13.75 15 13.75Z" fill="#558B2F"/> <path d="M22.5 13.75C23.5355 13.75 24.375 
            12.9105 24.375 11.875C24.375 10.8395 23.5355 10 22.5 10C21.4645 10 20.625 10.8395 20.625 11.875C20.625 
            12.9105 21.4645 13.75 22.5 13.75Z" fill="#558B2F"/> <path d="M7.5 13.75C8.53553 13.75 9.375 12.9105 9.375 
            11.875C9.375 10.8395 8.53553 10 7.5 10C6.46447 10 5.625 10.8395 5.625 11.875C5.625 12.9105 6.46447 13.75 
            7.5 13.75Z" fill="#558B2F"/> <path d="M25 3.75H5C4.3125 3.75 3.75 4.3125 3.75 5V6.875H26.25V5C26.25 
            4.3125 25.6875 3.75 25 3.75ZM13.125 6.875H16.875V11.875H13.125V6.875ZM23.125 6.875H20L20.625 
            11.875H24.375L23.125 6.875ZM6.875 6.875H10L9.375 11.875H5.625L6.875 6.875Z" fill="#7CB342"/> <path 
            d="M18.75 13.75C19.7855 13.75 20.625 12.9105 20.625 11.875C20.625 10.8395 19.7855 10 18.75 10C17.7145 10 
            16.875 10.8395 16.875 11.875C16.875 12.9105 17.7145 13.75 18.75 13.75Z" fill="#FFA000"/> <path d="M28.125 
            11.875C28.125 12.9375 27.3125 13.75 26.25 13.75C25.1875 13.75 24.375 12.9375 24.375 11.875C24.375 10.8125 
            25.1875 10 26.25 10L28.125 11.875Z" fill="#FFA000"/> <path d="M11.25 13.75C12.2855 13.75 13.125 12.9105 
            13.125 11.875C13.125 10.8395 12.2855 10 11.25 10C10.2145 10 9.375 10.8395 9.375 11.875C9.375 12.9105 
            10.2145 13.75 11.25 13.75Z" fill="#FFA000"/> <path d="M1.875 11.875C1.875 12.9375 2.6875 13.75 3.75 
            13.75C4.8125 13.75 5.625 12.9375 5.625 11.875C5.625 10.8125 4.8125 10 3.75 10L1.875 11.875Z" 
            fill="#FFA000"/> <path d="M20 6.875H16.875V11.875H20.625L20 6.875ZM26.25 6.875H23.125L24.375 
            11.875H28.125L26.25 6.875ZM10 6.875H13.125V11.875H9.375L10 6.875ZM3.75 6.875H6.875L5.625 
            11.875H1.875L3.75 6.875Z" fill="#FFC107"/> </svg> </div>""")
        ).add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        webView.resize(900, 850)
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            background-color:white;
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
