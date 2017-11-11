import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #Dockアイコン表示
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'door.png')
    app.setWindowIcon(QIcon(path))
    ex = Example()
    sys.exit(app.exec_())