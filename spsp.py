from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QScrollArea, QGroupBox, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap, QCursor
from sp import search_sp
import sys


class MyWindow(QMainWindow):

    def geo(self):
        # Set the initial width and height
        width = 1200
        height = 600
        return width, height

    def __init__(self, app):
        super(MyWindow, self).__init__()
        # Get the screen dimensions
        screen = app.primaryScreen()
        screen_geometry = screen.geometry()

        width, height= self.geo()
        # Calculate the x and y positions to center the window
        xpos = (screen_geometry.width() - width) // 2
        ypos = (screen_geometry.height() - height) // 2

        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("Spotify API GUI by Skeeter")
        #self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));")

        self.initUI()

    def initUI(self):

        width, height= self.geo()

        self.label=QtWidgets.QLabel(self)
        self.label.setText('It\'s Spotify API GUI by Skeeter')
        self.label.setGeometry((width - 300) // 2,0,200, 25)


        # Add a QLineEdit widget for user input
        self.q = QtWidgets.QLineEdit(self)
        self.q.setGeometry((width - 300) // 2, 50, 300, 25)
        self.q.setPlaceholderText('Search something in Spotify')
        self.client_id = QtWidgets.QLineEdit(self)
        self.client_id.setGeometry((width - 300) // 2, 100, 300, 25)
        self.client_id.setPlaceholderText('Enter your Spotify client_id')
        self.client_secret = QtWidgets.QLineEdit(self)
        self.client_secret.setGeometry((width - 300) // 2, 150, 300, 25)
        self.client_secret.setPlaceholderText('Enter your Spotify client_secret')

        # add a button 
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText('confirm')

        #styling button
        self.b1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.move((width - 300) // 2, 200)
        self.b1.setStyleSheet(
            "*{border: 2px solid '#BC006C';" +
            "border-radius: 15px;" +
            "font-size: 20px;}" +
            "*:hover {background: '#BC006C';}" 
        )
        
        # add a textarea to display console info
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setFixedSize(300, 100)  # Set a fixed size
        self.text_area.setPlaceholderText('console info will be displayed here.')
        self.text_area.move((width - 300) // 2, 250)
        self.text_area.setReadOnly(True)

        # Set the vertical scrollbar policy to AsNeeded
        self.text_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)


        self.b1.clicked.connect(self.b1clicked)

    def b1clicked(self):
        
        q=self.q.text()
        client_id=self.client_id.text()
        client_secret=self.client_secret.text()
        result=search_sp(q,client_id,client_secret)
        self.text_area.setText(str(result))
        

    # rescale geo
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow(app)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
