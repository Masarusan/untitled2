import sys
from PyQt5.QtWidgets import (QLineEdit, QApplication,QWidget
                            ,QGridLayout)
from PyQt5.QtGui import QWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.line_edit()

    def line_edit(self):
        lineedit = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(lineedit, 1, 1)
        self.setLayout(grid)
        self.setWindowTitle("TestQLineEdit")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())