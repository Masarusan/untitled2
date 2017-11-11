# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QSlider, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication
import sys


class App(QMainWindow):

    def main(self):
        self.w = QWidget()
        self.w.resize(250, 150)
        self.w.setWindowTitle('SliderSample')

        slider_label = QLabel('Slider (%):')
        self.slider = QSlider(Qt.Horizontal, self)  # スライダの向き
        self.slider.setRange(0, 100)  # スライダの範囲
        self.slider.setValue(20)  # 初期値
        #スライダの目盛りを両方に出す
        self.slider.setTickPosition(QSlider.TicksBothSides)
        #self.connect(self.slider, SIGNAL('valueChanged(int)'), self.on_draw)
        self.slider.valueChanged.connect(self.slider)

        hbox = QHBoxLayout()
        hbox.addWidget(slider_label)
        hbox.setAlignment(slider_label, Qt.AlignVCenter)
        hbox.addWidget(self.slider)
        hbox.setAlignment(self.slider, Qt.AlignVCenter)

        self.textbox = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addLayout(hbox)
        self.w.setLayout(vbox)
        self.w.show()

    def on_draw(self):
        self.textbox.setText(str(self.slider.value()))


def main_2():
    app = QApplication(sys.argv)
    ex = App()
    #ex.main()
    sys.exit(app.exec())

if __name__ == '__main__':
    main_2()