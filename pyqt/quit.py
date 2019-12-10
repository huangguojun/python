import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
quit = QPushButton("Quit")
quit.resize(175,30)
QObject.connect(quit,SIGNAL("clicked()"),app,SLOT("quit()"))

quit.show()

app.exec_()

