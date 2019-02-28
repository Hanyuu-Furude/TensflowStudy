import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QLabel, QPlainTextEdit, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication

class ui(QMainWindow):
    def __init__(self):
        super().__init__()

        # code to get and draw ui
        self.autoRead = True
        self.autoWrite = True
        # self=QMainWindow()
        loadUi('mainwindow.ui', self)
        self.checkBoxR = self.findChild(QCheckBox, 'checkBoxR')
        self.checkBoxR.stateChanged.connect(self.checkBoxChanged)
        self.checkBoxW = self.findChild(QCheckBox, 'checkBoxW')
        self.checkBoxW.stateChanged.connect(self.checkBoxChanged)
        self.textRead = self.findChild(QPlainTextEdit,'textOrigin')
        self.textWrite = self.findChild(QPlainTextEdit,'textTranslate')
        self.buttonExit = self.findChild(QPushButton,'buttonExit')
        self.buttonExit.clicked.connect(QCoreApplication.exit)  # button on exit
        self.show()

    # checkBox function
    def checkBoxChanged(self, state):
        if self.sender() == self.checkBoxR:
            self.autoRead = True if(state == 2) else False
        elif self.sender() == self.checkBoxW:
            self.autoWrite = True if (state == 2) else False
        # print('[auto read]', self.autoRead)
        # print('[suto write]', self.autoWrite)
        # print(self.textRead.toPlainText())
        # self.textWrite.clear()
        # self.textWrite.appendPlainText(self.textRead.toPlainText())
        # print(a.text())
        # a.text('a')
    # get the input box

    # fetch the text from textOrigin
    def fetchPlainText(self):
        return self.textRead.toPlainText()

    # set the text to textTranslate
    def setPlainText(self,text):
        self.textWrite.clear()
        self.textWrite.appendPlainText(text)
        return text



if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = ui()
    sys.exit(app.exec_())
