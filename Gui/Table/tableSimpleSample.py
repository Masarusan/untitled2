# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidgetItem, QVBoxLayout, QTableWidget
from PyQt5.QtCore import pyqtSlot


class App2(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 table -pythonspot-"
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_table()

        #layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        #show widget
        self.show()

    def create_table(self):
        #Create table
        self.tableWidget = QTableWidget()
        #行
        self.tableWidget.setRowCount(4)
        #列
        self.tableWidget.setColumnCount(2)
        #set data                  行、列                  データ
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1, 1"))
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        # self.tableWidget.setItem()
        self.tableWidget.move(0, 0)

        #table selection change
       # self.tableWidget


def main():
    app = QApplication(sys.argv)
    ex = App2()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
