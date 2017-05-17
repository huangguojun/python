import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)
quit = QPushButton("Quit")
quit.resize(175,30)
QObject.connect(quit,SIGNAL("clicked()"),app,SLOT("quit()"))

quit.show()

app.exec_()

