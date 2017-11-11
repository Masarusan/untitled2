# -*- coding: utf-8 -*-

import sys, datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.time_watch)
        self.testTimeDisplay = QLCDNumber(self)
        self.TimeDisplay = QLCDNumber(self)
        self.testTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.testTimeDisplay.setDigitCount(14)
        self.testTimeDisplay.resize(500, 150)
        self.time_watch()
        timer.start(1000)

        vbox = QVBoxLayout()
        vbox.addWidget(self.testTimeDisplay)
        self.setGeometry(300, 300, 500, 300)

    def time_watch(self):
        d = QDateTime.currentDateTime().toString("yyyy/MM/dd")

        currenttime = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.testTimeDisplay.display(d)
        self.testTimeDisplay.display(currenttime)
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())