# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        buttons = [[0, 0], [0, 1], [0, 2],
                   [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]]

        i = 0

        for i in buttons:
            button = QPushButton(str(i))
            layout.addWidget(button,i[0], i[1])


        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())