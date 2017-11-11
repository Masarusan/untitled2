#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 水平方向のスライダー作成
        sld = QSlider(Qt.Horizontal, self)
        # スライダーがフォーカスされないようにする
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        # スライダーが動くとchangeValue関数が呼び出される
        sld.valueChanged[int].connect(self.changeValue)

        # ラベル作成
        self.label = QLabel(self)
        # ラベルに初期画像設定
        self.label.setPixmap(QPixmap('penki.png'))
        self.label.setGeometry(100, 100, 256, 256)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        # スライダーの位置によって画像を変化させる
        if value == 0:
            # オレンジ色の画像
            self.label.setPixmap(QPixmap('penki.png'))
        elif value > 0 and value <= 30:
            # 黄色の画像
            self.label.setPixmap(QPixmap('hasami.png'))
        elif value > 30 and value < 80:
            # 緑色の画像
            self.label.setPixmap(QPixmap('renti.png'))
        else:
            # 青色の画像
            self.label.setPixmap(QPixmap('door.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())