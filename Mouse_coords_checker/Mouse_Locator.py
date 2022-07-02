from win32api import GetCursorPos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from screeninfo import get_monitors

WIDTH = int((get_monitors()[0].width-600)/2)
HEIGHT = int(get_monitors()[0].height/2)-150
  
class Window(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowIcon(QIcon('kursor.png'))
        self.setWindowTitle("Mouse Locator")
        self.setGeometry(WIDTH,HEIGHT,600,150)
        self.setFixedSize(self.size())
        self.UIComponents()

    def UIComponents(self):
        self.startButton = QPushButton("Set position",self)
        self.startButton.setGeometry(100,45,200,50)
        self.startButton.clicked.connect(self.Start_When_Click)
        self.QuitButton = QPushButton("Quit",self)
        self.QuitButton.setGeometry(300,45,200,50)
        self.QuitButton.clicked.connect(self.Quit_When_Click)
        self.transparent = TransparentWindow(self)

    def Start_When_Click(self):
        self.close()
        self.transparent.showFullScreen()

    def Quit_When_Click(self):
        self.close()

    def mouseMoveEvent(self,event):
        self.cursorloc_info.setText("("+str(event.globalX())+", "+str(event.globalY())+")")

class TransparentWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowOpacity(0.5)
        self.UiComponents()
        self.setMouseTracking(True)

    def mousePressEvent(self,QMouseEvent):
        self.x = QMouseEvent.globalX()
        self.y = QMouseEvent.globalY()
        self.close()
        self.result_win = ResultWindow(self)
        self.result_win.cursorloc_info.setText("("+str(self.x)+", "+str(self.y)+")")
    
    def mouseMoveEvent(self, event):
        self.cursorloc_info.setGeometry(event.globalX()+12,event.globalY(),100,20)
        self.cursorloc_info.setText("("+str(event.globalX())+", "+str(event.globalY())+")")

    def UiComponents(self):
        self.cursorloc_info = QLabel(self)
        font = QFont("Arial", 10)
        self.cursorloc_info.setFont(font)

class ResultWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowIcon(QIcon('kursor.png'))
        self.setWindowTitle("Mouse Locator")
        self.setGeometry(WIDTH,HEIGHT,600,150)
        self.setFixedSize(self.size())
        self.UiComponents()

    def UiComponents(self):
        self.label = QLabel("Coordinates: ",self)
        self.label.setGeometry(120,0,600,150)
        self.label.setAlignment(Qt.AlignLeft)
        font = QFont("Arial", 20)
        self.label.setFont(font)
        self.cursorloc_info = QLabel(self)
        self.cursorloc_info.setGeometry(95,0,600,150)
        self.cursorloc_info.setAlignment(Qt.AlignHCenter)
        self.cursorloc_info.setFont(font)
        self.startButton = QPushButton("Set position",self)
        self.startButton.setGeometry(100,55,200,50)
        self.startButton.clicked.connect(self.Start_When_Click)
        self.transparent = TransparentWindow(self)
        self.QuitButton = QPushButton("Quit",self)
        self.QuitButton.setGeometry(300,55,200,50)
        self.QuitButton.clicked.connect(self.Quit_When_Click)
        self.show()

    def Start_When_Click(self):
        self.close()
        self.transparent.showFullScreen()

    def Quit_When_Click(self):
        self.close()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
