# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
#encoding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#import baidutranslate  
import requests
import string
import time
import hashlib
import json


api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = "20180430000151935"
cyber = "fVWFdsmEiv74MwcQVnbO"
lower_case = list(string.ascii_lowercase)


class Ui_MainWindow2(object):

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 181, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)     #The first textEdit  
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 100, 191, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)    #The second textEdit 
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 51, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 140, 81, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 220, 51, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 40, 211, 20))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 220, 51, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(480, 220, 51, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)

        self.comboBox.setGeometry(QtCore.QRect(100, 70, 85, 27))

        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 70, 85, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow2", "录音"))
        self.pushButton_2.setText(_translate("MainWindow2", "翻译"))
        self.pushButton_3.setText(_translate("MainWindow2", "播报"))
        self.label.setText(_translate("MainWindow2", "多功能翻译系统"))
        self.pushButton_4.setText(_translate("MainWindow2", "打开"))
        self.pushButton_7.setText(_translate("MainWindow2", "关闭"))

        self.comboBox.setItemText(0, _translate("MainWindow2", "文字"))
        self.comboBox.setItemText(1, _translate("MainWindow2", "文档"))
        self.comboBox.setItemText(2, _translate("MainWindow2", "语音"))
        self.comboBox.setItemText(3, _translate("MainWindow2", "视频"))
        self.comboBox_2.setItemText(0, _translate("MainWindow2", "文字"))
        self.comboBox_2.setItemText(1, _translate("MainWindow2", "文档"))
        self.comboBox_2.setItemText(2, _translate("MainWindow2", "语音"))
        self.comboBox_2.setItemText(3, _translate("MainWindow2", "视频"))
    
    def requests_for_dst(self,word):
        #init salt and final_sign
        salt = str(time.time())[:10]
        final_sign = str(my_appid)+word+salt+cyber
        final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
        #区别en,zh构造请求参数
        if str(word)[0] in lower_case:
            paramas = {
                'q':word,
                'from':'en',
                'to':'zh',
                'appid':'%s'%my_appid,
                'salt':'%s'%salt,
                'sign':'%s'%final_sign
                }
            my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'en'+'&to='+'zh'+'&salt='+salt+'&sign='+final_sign
        else:
            paramas = {
                'q':word,
                'from':'zh',
                'to':'en',
                'appid':'%s'%my_appid,
                'salt':'%s'%salt,
                'sign':'%s'%final_sign
                }
            my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'zh'+'&to='+'en'+'&salt='+salt+'&sign='+final_sign
        response = requests.get(api_url,params = paramas).content
        #content = str(response,encoding = "utf-8")
        content = str(response)
        json_reads = json.loads(content)
        print(json_reads['trans_result'][0]['dst'])    
        #return self.requests_for_dst(word)

    def translateapi(self,word):               #baiduapi translate  mode
       
        #word = input("输入你想翻译的内容: ")
           
        word = self.textEdit.toPlainText()
        #str1=str(baidutranslate.requests_for_dst(word))
        self.requests_for_dst(word)
        #baidutranslate.requests_for_dst(word)
        #print type(baidutranslate.requests_for_dst(word))
        #self.textEdit_2.setPlainText("%s"%(self.translateapi(self.textEdit.toPlainText())))

    def setupFunction(self):                                     #set function for the button
        self.pushButton_2.clicked.connect(self.translateapi)
        word = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText("%s"%(self.translateapi(word)))
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    ui.setupFunction() 
    MainWindow.show()
    sys.exit(app.exec_())
 

