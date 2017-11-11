#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from  scrape_01 import Scrape
import urllib.request


class Example(QWidget, Scrape):

    def __init__(self):
        super().__init__()
        super().__init__(self, list=[], url='',list_img=[[]])

        self.initUI()


    def initUI(self):
        url = 'http://xxeronetxx.info/img/20170906/m-83fd3fe45c96187853f19d960d61b0fbcec15dad.jpg'
        sc = Scrape()
        sc.set_url('http://xxeronetxx.info/img/20170906/v1-074.html')
        src = sc.scrape()
        #print(sc.get_list()[1])
        hbox = QHBoxLayout(self)
        # QPixmapオブジェクト作成
        #for a in sc.get_list():
        for link in sc.get_soup().find_all('img'):
            self.__list_img = [link.get('src')]
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        # ラベルを作ってその中に画像を置く
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)


        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(500, 200)
        self.setWindowTitle('Imoyokan')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())