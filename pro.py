
#encoding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtGui import QPalette,QBrush,QPixmap,QColor, QIcon,QPixmap
from PyQt5.QtWidgets import  QFileDialog,QWidget
from  baidutranslate import requests_for_dst 
import requests
import string
import time
import hashlib
import json
import sys
import os
import wave
import pyaudio
import voice
import recordvoice
import s 
import GenAudio
import xunfeitts
from log import Logger
from Baidutts import BaiduRest  
from  bdtranslate import translate1,translate2
from  baiduasr import  asr  


class Ui_MainWindow2(QWidget):


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


        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 100, 191, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 51, 27))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setStyleSheet('QPushButton{background-image:url(record.png)}')

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
        self.pushButton_7.setGeometry(QtCore.QRect(480, 220, 60, 27))
        self.pushButton_7.setObjectName("pushButton_7")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 70, 85, 27))

        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
       
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 70, 85, 27))

        self.comboBox_2.setObjectName("comboBox_2")
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
        MainWindow2.setWindowTitle(_translate("MainWindow2", "translate system"))
 
        self.pushButton.setText(_translate("MainWindow2", "录音"))
        self.pushButton.setToolTip("请说话")

        self.pushButton_2.setText(_translate("MainWindow2", "翻译"))
        self.pushButton_2.setToolTip("中英互译")

        self.pushButton_3.setText(_translate("MainWindow2", "播报"))
        self.pushButton_3.setToolTip("文字朗读")

        self.label.setText(_translate("MainWindow2", "多功能翻译系统"))

        self.pushButton_4.setText(_translate("MainWindow2", "打开"))
        self.pushButton_4.setToolTip("打开文本/音视频")

        self.pushButton_7.setText(_translate("MainWindow2", "合成视频"))
        self.pushButton_7.setToolTip("将音频和视频组合")

        self.comboBox.setItemText(0, _translate("MainWindow2", "源语言"))
      
        self.comboBox_2.setItemText(0, _translate("MainWindow2", "目标语言"))



    def setupFunction(self):   
        self.pushButton.pressed.connect(self.Record) 
        #self.pushButton.released.connect(self.record_stop)                                 #set function for the button
        self.pushButton_2.clicked.connect(self.translateapi)
        self.pushButton_4.clicked.connect(self.openfile)
        
        self.pushButton_3.clicked.connect(self.tts)
        self.pushButton_7.clicked.connect(self.mix)
        #self.pushButton.released.connect(self.stopRecord)
        #self.textEdit_2.setText(baidutranslate.requests_for_dst(self.textEdit.toPlainText()))
        #self.textEdit_2.setText(baidutranslate.requests_for_dst())




    def translateapi(self):               #baiduapi translate  mode

            low = 'abcdefghijklmnopqrstuvwxyz'
            up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            #yourAppId = '20170221000039563'
            yourAppId =  '20180430000151935'
            #yourSecret = 'nIyk6j2N4pOIc3PpE9tY'
            yourSecret ='fVWFdsmEiv74MwcQVnbO'
            word = self.textEdit.toPlainText()
            
            if (str(word)[0] in low)|(str(word)[0] in up):
               self.textEdit_2.setText(translate1(yourAppId, yourSecret, "en", "zh",word))
            else:
               word2 = str(word)
               self.textEdit_2.setText(translate2(yourAppId, yourSecret, "zh", "en",word2))
        #requests_for_dst(word)
            #str1 = (baidutranslate.requests_for_dst(word))
            #baidutranslate.requests_for_dst(word)
            #baidutranslate.requests_for_dst(word)
            #sys.stdout = Logger("1.txt")
             #self.textEdit_2.setText
            #self.textEdit_2.setText(baidutranslate.requests_for_dst(word))

    def openfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', './')
        file_path = os.path.split(filename[0]) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        #print lists[1]
        if  lists[1] == 'txt':                  #open the txt 
            if filename[0]:
                with open(filename[0], 'r') as f:
                   self.textEdit.setText(f.read())

        if  lists[1] == 'wav':                  #open the sound 
            voice.playvoice(filename[0])
            #os.system('play test2.mp3')
            self.textEdit.setText(s.recognize(filename[0]))
        
        if  lists[1] == 'mp3':                  #open the sound 
            #voice.playvoice(filename[0])
            cmd6 =  "ffmpeg  -i "+''+ file_path[1] +' '+" mp3out.wav "
            os.system(cmd6)
            os.system  ('play'+' '+filename[0])
            self.textEdit.setText(asr("mp3out.wav"))

        if  lists[1] == 'mp4':                  #open the video
            cmd = "mplayer"+ ' '+file_path[1]
            os.system(cmd)
            #dtVideoFile = "d:\\workroom\\testroom\\dt-program.mp4"
             
            cmd2 = "ffmpeg -i " + file_path[1] + " -vn -sn -dn -f wav output.wav " 
            os.system(cmd2)
            os.system('play test2.mp3')
            self.textEdit.setText(s.recognize("output.wav"))
            #dt_sr(pcmFile)
         #os.system('paly filename[0]')
         #os.system('mplayer L9.mp4')
         #if os.path.splitext(filename)[1] == '.txt':  
                #with open(filename[0], 'r') as f:
                    #self.textEdit.setText(f.read())  
         #elif os.path.splitext(filename)[1] == '.mp3':  
                  #os.system('play filename')       
         #else:              
         #a = filename[0]
               #os.system('mplayer a')
         #print filename[1] 
         #print type(filename) 
         #print type(filename[0]) 
        
    
         #print (filename) 
         #print (filename[0])
         
         
         #print file_path
         
         
         #print lists
        
       #if filename[0]:
                #with open(filename[0], 'r') as f:
                   #self.textEdit.setText(f.read())
    #def startRecord(self):
        #recordvoice.my_record()

    #def stopRecord(self):
        #recordvoice.paly()

    def mix(self):

        filename = QFileDialog.getOpenFileName(self, 'Open file', './')
        file_path = os.path.split(filename[0]) #分割出目录与文件
        #lists = file_path[1].split('.') #分割出文件与文件扩展名
        #if  lists[1] == 'mp4':                  #open the video
            #dtVideoFile = "d:\\workroom\\testroom\\dt-program.mp4" 
        cmd3 = "ffmpeg -i  "+' '+ file_path[1] + ' '+" -vcodec copy -an test.mp4"
        os.system(cmd3)
        time.sleep(3) 
        cmd4 = "ffmpeg -i test.mp4 -i test0.mp3 -vcodec copy -acodec copy output.avi " 
        os.system(cmd4)
        time.sleep(3) 
        cmd5 = "mplayer output.avi"
        os.system(cmd5)
  


    def Record(self):   
            os.system("play start.mp3")       
            os.system("python GenAudio.py")           
            os.system("play test.wav")
            result = asr("test.wav")
            self.textEdit.setText(result)

    
    def  tts(self):                
        word = str(self.textEdit_2.toPlainText())
        #xunfeitts.text_to_speech(str(word),'xx.wav')
        api_key = "SrhYKqzl3SE1URnAEuZ0FKdT" 
        api_secert = "hGqeCkaMPb0ELMqtRGc2VjWdmjo7T89d"
        bdr = BaiduRest("test_python", api_key, api_secert)
    # 将字符串语音合成并保存为out.mp3
        bdr.getVoice(word, "test0.mp3")
        os.system('play test0.mp3')


    def record_stop(self):
    # stop record the wave
          # stop stream (4)
          pass

   

if __name__ == '__main__':
    #baidutranslate.requests_for_dst('word')
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
   
    ui.setupUi(MainWindow)
    ui.setupFunction()

    #QtGui.QApplication.processEvents()
    MainWindow.show()
    sys.exit(app.exec_())

    