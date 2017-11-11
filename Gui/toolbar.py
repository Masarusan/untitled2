# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):


        exitAction = QAction(QIcon('door.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        pythonAction = QAction(QIcon('hasami.png'), 'Python', self)
        pythonAction.setShortcut('Ctrl+P')
        pythonAction.triggered.connect(qApp.quit)

        qtInfoAction = QAction(QIcon('renti.png'), 'qtinfo', self)
        qtInfoAction.setShortcut('Ctrl+I')
        qtInfoAction.setStatusTip('Show Qt info')
        qtInfoAction.triggered.connect(qApp.aboutQt)
    #ツールバー作成
        self.setWindowIcon(QIcon("door.png"))
        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(pythonAction)
        self.toolbar.addAction(qtInfoAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(250,250)
    win.setWindowTitle("toolbar")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    #main()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())