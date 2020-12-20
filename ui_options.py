# -*- coding: utf-8 -*-

# Form generated from reading UI file 'optionsKPfkLn.ui'

# Created by: Qt User Interface Compiler version 5.15.2

# WARNING! All changes made in this file will be lost when recompiling UI file!

#PyQT5 GUI imports
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Inner Window Design
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(677, 385)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color:rgb(220, 220, 220);\n"
"	border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 310, 121, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(5, 7, 31, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/Icons/back.png);\n"
"background-color: rgba(56, 58, 8,0);")
        self.lineEdit_next = QLineEdit(self.frame)
        self.lineEdit_next.setObjectName(u"lineEdit_next")
        self.lineEdit_next.setGeometry(QRect(20, 70, 261, 71))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.lineEdit_next.setFont(font2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 221, 16))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 160, 261, 16))
        self.label_3.setFont(font2)
        self.lineEdit_back = QLineEdit(self.frame)
        self.lineEdit_back.setObjectName(u"lineEdit_back")
        self.lineEdit_back.setGeometry(QRect(20, 180, 261, 71))
        self.lineEdit_back.setFont(font2)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(330, 20, 1, 301))
        self.line.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.478, y1:0.487591, x2:0.477, y2:0, stop:0.806818 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 0));")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 280, 291, 16))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 110, 121, 31))
        self.label_5.setFont(font)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(22, 8, 71, 20))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(56, 58, 8,0);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 130, 221, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 150, 221, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 200, 261, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # Function to render UI in Python 

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Developed: <span style=\" font-weight:600;\">MNM</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Keywords/phrases for forward transition:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Keywords/phrases for backward transition:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Note: Please seperate keywords/phrases using comma", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Version:</span> 1.0.0</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Released date:</span> 20 December, 2020</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Website:</span> www.slidetalk.tech</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Developed with love at </span>HACKUMASS2020</p></body></html>", None))

