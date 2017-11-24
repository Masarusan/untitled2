#!/usr/bin/python
# -*- coding: utf-8 -*-

from Example import *


class TestGui(Example):

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec())