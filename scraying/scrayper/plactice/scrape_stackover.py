# -*- coding: utf-8 -*-


import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QLabel
import urllib.request

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        url = 'http://www.google.com/images/srpr/logo1w.png'
        data = urllib.request.urlopen(url).read()


        lbl = QLabel(self)
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        #self.setLayout(hbox)
        self.resize(400, 400)
        self.show()

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()