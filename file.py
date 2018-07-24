#-*- coding:utf-8 -*-
#######pyqt  文件载入对话框，文件保存对话框，打开文件夹对话框
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MyWindow(QDialog,QWidget):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.resize(400,150)
        self.mainlayout = QGridLayout(self)
        self.loadFileButton = QPushButton()
        self.loadFileButton.setText(u"载入文件")
        self.mainlayout.addWidget(self.loadFileButton,0,0,1,1)
        self.loadFileLineEdit = QLineEdit()
        self.mainlayout.addWidget(self.loadFileLineEdit,0,1,1,4)
        self.loadFileButton.clicked.connect(self.loadFile)

        self.saveFileButton = QPushButton()
        self.saveFileButton.setText(u"保存文件")
        self.saveFileLineEdit = QLineEdit()
        self.mainlayout.addWidget(self.saveFileButton,1,0,1,1)
        self.mainlayout.addWidget(self.saveFileLineEdit,1,1,1,4)
        self.saveFileButton.clicked.connect(self.saveFile)

        self.openFileDirButton = QPushButton()
        self.openFileDirButton.setText(u"打开文件目录")
        self.mainlayout.addWidget(self.openFileDirButton,2,0,1,1)
        self.openFileDirButton.clicked.connect(self.openFileDirectory)

    def loadFile(self):########载入file
        file_name = QFileDialog.getOpenFileName(self,"open file dialog","./home/fish","Txt files(*.txt)")
        ##"open file Dialog "文件对话框的标题，第二个是打开的默认路径，第三个是文件类型
        self.loadFileLineEdit.setText(file_name)

    def saveFile(self):
        file_path =  QFileDialog.getSaveFileName(self,'save file',"saveFile" ,"xj3dp files (*.xj3dp);;all files(*.*)") ####
        print file_path

    def openFileDirectory(self):
        import os
        os.popen("explorer.exe ./home/fish")


app=QApplication(sys.argv)
window=MyWindow()
window.show()
app.exec_()