# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import sys
import urllib.request
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QGridLayout,QGroupBox,QVBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QUrl
from bs4 import *
import requests
from scrape_01 import Scrape
from PIL import Image

class Example(QWidget, Scrape):

    def __init__(self):
        super().__init__()
        super().__init__(self, list=[], url='')
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 600
        self.init_ui()
        #self.show()

    def init_ui(self):
        sc = Scrape()
        # QPixmapオブジェクト作成
        sc.set_url('http://xxeronetxx.info/img/20170906/v1-074.html')
        src = sc.scrape()

        for i in sc.get_list_img():
            self.data = io.BytesIO(urllib.request.urlopen(i).read())
            pixmap = QPixmap(self.resize_img(self.data))
            self.createGridLayout(pixmap.loadFromData(pixmap))
            print(i)

        # ラベルを作ってその中に画像を置く
            windowlayout = QVBoxLayout()
            windowlayout.addWidget(self.horizontalGroupBox)
            self.setLayout(windowlayout)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Imoyokan')
        self.show()

    def createGridLayout(self, pixmap):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        labels = [
            [0, 0], [0, 1], [0, 2],
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2]
        ]

        i = 0
        for i in labels:
            label = QLabel(self)
            label.setPixmap(pixmap)
            layout.addWidget(label)
        #, i[0], i[1]

        self.horizontalGroupBox.setLayout(layout)

    def resize_img(self, img):
        #既存ファイルを、readモードで読み込み
        image = Image.open(img, 'r')
        #リサイズ。サイズは幅と高さタプルで指定
        resize_img = self.resize((150, 150))
        #リサイズ後の画像を保存
        resize_img.save('resize_img', 'JPEG', quality=100, optimize=True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())