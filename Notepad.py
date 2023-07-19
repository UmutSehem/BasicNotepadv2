import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
        
    def init_ui(self):
        
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("Clear")
        
        h_box = QHBoxLayout()
        
        h_box.addWidget(self.temizle)
        
        v_box = QVBoxLayout()

        v_box.addWidget(self.yazialani)
        v_box.addLayout(h_box)


        self.setLayout(v_box)
        
        self.temizle.clicked.connect(self.temiz)

    def temiz(self):
        
        self.yazialani.clear()
class Menu(QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        self.pencere = Notepad()
        
        self.setCentralWidget(self.pencere)

        self.menuler()
    def menuler(self):
        menubar = self.menuBar()
        
        
        dosya = menubar.addMenu("File")
        yazitip = menubar.addMenu("Other")
        
        dosyaac = QAction("Open File",self)
        dosyaac.setShortcut("Ctrl+O")

        dosyakaydet = QAction("File Save",self)
        dosyakaydet.setShortcut("Ctrl+P")


        cikis = QAction("Quit",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosyaac)
        dosya.addAction(dosyakaydet)
        dosya.addAction(cikis)
        



        

        dosya.triggered.connect(self.response)


        
        

        

        
        self.setWindowTitle("Advanced Notepad")
        self.setGeometry(700,250,500,400)

        self.show()

    def ac(self):
            dosyaismi = QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))
            with open(dosyaismi[0],"r") as file:
                self.pencere.yazialani.setText(file.read())

    
    def kayit(self):
        dosyaismi = QFileDialog.getSaveFileName(self,"File Save",os.getenv("Desktop"))

        with open(dosyaismi[0],"w") as file:
            file.write(self.pencere.yazialani.toPlainText())                


    def response(self,action):
        if action.text() == "Open File":
            self.ac()
        elif action.text() == "File Save":
            self.kayit()
        elif action.text() == "Quit":
            qApp.quit()



app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())



