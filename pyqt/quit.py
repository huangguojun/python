import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)
quit = QPushButton("Quit")
quit.resize(175,30)
quit.clicked.connect(QCoreApplication.instance().quit)

quit.show()

app.exec_()

