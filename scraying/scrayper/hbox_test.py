# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        pixa = QPixmap('renti.png')

        for i in range(5):
            lbl = QLabel()
            #lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            lbl.setPixmap(pixa)
            hbox.addWidget(lbl)
            vbox.addWidget(lbl)
            hbox.addLayout(vbox)
            self.setLayout(hbox)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())