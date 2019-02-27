import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QLabel
from PyQt5.uic import loadUi


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
        print(type(self.checkBoxR))
        # print(ui.findChild(QCheckBox, 'checkBoxR').checked())
        self.show()

    # checkBox function
    def checkBoxChanged(self, state):
        if self.sender() == self.checkBoxR:
            self.autoRead = True if(state == 2) else False
        elif self.sender() == self.checkBoxW:
            self.autoWrite = True if (state == 2) else False
        print('[auto read]', self.autoRead)
        print('[suto write]', self.autoWrite)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = ui()
    sys.exit(app.exec_())
