# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_MainTitle = QtWidgets.QLabel(self.centralwidget)
        self.label_MainTitle.setGeometry(QtCore.QRect(3, 10, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_MainTitle.setFont(font)
        self.label_MainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MainTitle.setObjectName("label_MainTitle")
        self.lineEdit_Adder1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adder1.setGeometry(QtCore.QRect(10, 40, 51, 20))
        self.lineEdit_Adder1.setObjectName("lineEdit_Adder1")
        self.lineEdit_Adder2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adder2.setGeometry(QtCore.QRect(90, 40, 51, 20))
        self.lineEdit_Adder2.setObjectName("lineEdit_Adder2")
        self.lineEdit_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sum.setGeometry(QtCore.QRect(170, 40, 51, 20))
        self.lineEdit_sum.setReadOnly(True)
        self.lineEdit_sum.setObjectName("lineEdit_sum")
        self.label_plus = QtWidgets.QLabel(self.centralwidget)
        self.label_plus.setGeometry(QtCore.QRect(60, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_plus.setFont(font)
        self.label_plus.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plus.setObjectName("label_plus")
        self.label_equals = QtWidgets.QLabel(self.centralwidget)
        self.label_equals.setGeometry(QtCore.QRect(140, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_equals.setFont(font)
        self.label_equals.setAlignment(QtCore.Qt.AlignCenter)
        self.label_equals.setObjectName("label_equals")
        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setGeometry(QtCore.QRect(230, 40, 75, 23))
        self.pushButton_calc.setObjectName("pushButton_calc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "加法器"))
        self.label_MainTitle.setText(_translate("MainWindow", "简易加法器"))
        self.label_plus.setText(_translate("MainWindow", "+"))
        self.label_equals.setText(_translate("MainWindow", "="))
        self.pushButton_calc.setText(_translate("MainWindow", "计算"))
 
    def setupFunction(self):
        self.pushButton_calc.clicked.connect(self.get_sum)
 
    def get_sum(self):
        adder1 = self.lineEdit_Adder1.text()    # 获取第一个文本框中的内容存入adder1
        adder2 = self.lineEdit_Adder2.text()    # 获取第二个文本框中的内容存入adder2
        sum = int(adder1) + int(adder2)         # 将adder1和adder2强制转换为整形，计算出两数之和存入sum
        self.lineEdit_sum.setText(str(sum))     # 将sum强制转换为字符串，填入lineEdit_sum
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    ui.setupFunction()                      # 执行类中的setupFunction方法
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication
 
