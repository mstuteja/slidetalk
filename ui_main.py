# -*- coding: utf-8 -*-

# Form generated from reading UI file 'main_screenbvIFAW.ui'

# Created by: Qt User Interface Compiler version 5.15.2

# WARNING! All changes made in this file will be lost when recompiling UI file!

# PyQT GUI imports
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Main GUI Design

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.shadowframe = QFrame(self.centralwidget)
        self.shadowframe.setObjectName(u"shadowframe")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.shadowframe.setFont(font)
        self.shadowframe.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color:rgb(220, 220, 220);\n"
"	border-radius:20px;\n"
"}")
        self.shadowframe.setFrameShape(QFrame.StyledPanel)
        self.shadowframe.setFrameShadow(QFrame.Raised)
        self.selectfile = QPushButton(self.shadowframe)
        self.selectfile.setObjectName(u"selectfile")
        self.selectfile.setGeometry(QRect(150, 150, 401, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.selectfile.setFont(font1)
        self.selectfile.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(56, 58, 89);\n"
"border-radius:5px;")
        self.loadingBar = QProgressBar(self.shadowframe)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setGeometry(QRect(150, 150, 401, 21))
        self.loadingBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(195, 195, 195);\n"
"	\n"
"	color: rgba(255, 255, 255, 0);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"}")
        self.loadingBar.setValue(24)
        self.label_3 = QLabel(self.shadowframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 150, 251, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: rgba(56, 58, 89, 0);\n"
"color: rgb(56, 58, 89);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.shadowframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 0, 81, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgba(56, 58, 89,0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/Icons/settings.png);")
        self.pushButton_2 = QPushButton(self.shadowframe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(10, 0, 51, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setWeight(50)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"background-color: rgba(56, 58, 89,0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton_2.setIconSize(QSize(10, 10))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)
        self.start_button = QPushButton(self.shadowframe)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(200, 140, 291, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(25)
        font5.setBold(True)
        font5.setWeight(75)
        self.start_button.setFont(font5)
        self.start_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.start_tag = QLabel(self.shadowframe)
        self.start_tag.setObjectName(u"start_tag")
        self.start_tag.setGeometry(QRect(160, 190, 371, 21))
        self.start_tag.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.start_tag.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.shadowframe, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # Function to render UI in Python program

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectfile.setText(QCoreApplication.translate("MainWindow", u"Select file (.pptx)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Processing file...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start Presenting", None))
        self.start_tag.setText(QCoreApplication.translate("MainWindow", u"<strong>Note:</strong> Please open the powerpoint app before start presenting", None))

