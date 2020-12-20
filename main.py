import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import random
import start
import pptcontrol

from ui_splash_screen import Ui_SpalshScreen
from ui_main import Ui_MainWindow
from ui_options import Ui_MainWindow as Ui_options
counter = 0
counter2 = 0
res = ""
file = ""

class MainWindow(QMainWindow):
    def __init__(self): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.shadowframe.setGraphicsEffect(self.shadow)
        self.ui.label_3.setVisible(False)
        self.ui.start_button.setVisible(False)
        self.ui.start_tag.setVisible(True)
        self.ui.loadingBar.setVisible(False)
        self.ui.selectfile.clicked.connect(self.pickFile)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.start_button.clicked.connect(self.startPresenting)
        self.ui.pushButton.clicked.connect(self.goOptions)

    def goOptions(self):
            self.main = OptionScreen()
            self.main.show()
            self.close()

    def startPresenting(self):
        if(self.ui.start_button.text()=="Start Presenting"):
            global file
            self.ui.start_button.setText("Stop Presenting")
            self.ui.start_tag.setVisible(False)
            start.startf(file)
        else:
            self.ui.start_button.setText("Start Presenting")
            self.ui.start_tag.setVisible(True)

    def exit(self):
        self.close()

    def pickFile(self):
        global res
        global file
        filePath = QFileDialog.getOpenFileName()[0]
        file = filePath
        self.ui.selectfile.setVisible(False)
        self.ui.loadingBar.setVisible(True)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.prog)
        self.timer.start(30)
        self.ui.label_3.setVisible(True)
        res = start.predata(filePath)
        
    def prog(self):
        global res
        global counter2
        self.ui.loadingBar.setValue(counter2)
        if counter2 > 100:
            self.ui.loadingBar.setVisible(False)
            if(res!="Done"):
                self.ui.selectfile.setVisible(True)
                self.ui.start_tag.setVisible(True)
                self.ui.label_3.setVisible(False)
            else:
                self.ui.start_tag.setVisible(True)
                self.ui.start_button.setVisible(True)
            self.timer.stop()
        counter2 += 2.0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SpalshScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.shadow.setGraphicsEffect(self.shadow)
        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(30)
        self.ui.label_loading.setText("checking for updates")
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText(""))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("loading user interface"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += random.uniform(0.8,1.0)

class OptionScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_options()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.ui.pushButton.clicked.connect(self.goMain)
        self.ui.pushButton_2.clicked.connect(self.goMain)
        self.ui.lineEdit_next.setText(start.next_extra)
        self.ui.lineEdit_back.setText(start.back_extra)
        self.show()
    
    def goMain(self):
        start.next_extra = self.ui.lineEdit_next.text()
        start.back_extra = self.ui.lineEdit_back.text()
        self.main = MainWindow()
        self.main.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())