# -*- coding: utf-8 -*-

# Form generated from reading UI file 'splash_screenxhmXHd.ui'

# Created by: Qt User Interface Compiler version 5.15.2

# WARNING! All changes made in this file will be lost when recompiling UI file!

#PyQT5 GUI imports 
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Inner Window 2 GUI Design 
class Ui_SpalshScreen(object):
    def setupUi(self, SpalshScreen):
        if not SpalshScreen.objectName():
            SpalshScreen.setObjectName(u"SpalshScreen")
        SpalshScreen.setEnabled(True)
        SpalshScreen.resize(680, 400)
        SpalshScreen.setAutoFillBackground(False)
        SpalshScreen.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(SpalshScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.shadow = QFrame(self.centralwidget)
        self.shadow.setObjectName(u"shadow")
        self.shadow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color:rgb(220, 220, 220);\n"
"	border-radius:20px;\n"
"}")
        self.shadow.setFrameShape(QFrame.StyledPanel)
        self.shadow.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.shadow)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 81))
        font = QFont()
        font.setFamily(u"Baskerville Old Face")
        font.setPointSize(60)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_tagline = QLabel(self.shadow)
        self.label_tagline.setObjectName(u"label_tagline")
        self.label_tagline.setGeometry(QRect(0, 170, 661, 51))
        font1 = QFont()
        font1.setFamily(u"Lucida Calligraphy")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_tagline.setFont(font1)
        self.label_tagline.setStyleSheet(u"background-color: rgba(56, 58, 89, 0);\n"
"color: rgb(195, 195, 195);")
        self.label_tagline.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.progressBar = QProgressBar(self.shadow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 252, 461, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
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
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.shadow)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(10, 280, 651, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(195, 195, 195);")
        self.label_loading.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_credits = QLabel(self.shadow)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 330, 631, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(195, 195, 195);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_2 = QLabel(self.shadow)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setGeometry(QRect(20, 330, 191, 21))
        self.label_credits_2.setFont(font3)
        self.label_credits_2.setStyleSheet(u"color: rgb(195, 195, 195);")
        self.label_credits_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.shadow)

        SpalshScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SpalshScreen)
        self.statusbar.setObjectName(u"statusbar")
        SpalshScreen.setStatusBar(self.statusbar)

        self.retranslateUi(SpalshScreen)

        QMetaObject.connectSlotsByName(SpalshScreen)

    # Function to render UI in Python

    def retranslateUi(self, SpalshScreen):
        SpalshScreen.setWindowTitle(QCoreApplication.translate("SpalshScreen", u"XYZ", None))
        self.label_title.setText(QCoreApplication.translate("SpalshScreen", u"<html><head/><body><p>Slide<span style=\" font-weight:600;\">Talk</span></p></body></html>", None))
        self.label_tagline.setText(QCoreApplication.translate("SpalshScreen", u"<html><head/><body><p align=\"center\">Presenting in style</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SpalshScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SpalshScreen", u"<html><head/><body><p>Developed: <span style=\" font-weight:600;\">MNM</span></p></body></html>", None))
        self.label_credits_2.setText(QCoreApplication.translate("SpalshScreen", u"<html><head/><body><p>Version: <span style=\" font-weight:600;\">1.0.0</span></p></body></html>", None))

