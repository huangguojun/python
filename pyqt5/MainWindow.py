import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
