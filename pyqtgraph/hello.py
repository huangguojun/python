from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg

## Always start by initializing Qt (only once per application)
app = QApplication([])

## Define a top-level widget to hold everything
w = QWidget()

## Create some widgets to be placed inside
btn = QPushButton('press me')
text = QLineEdit('enter text')
listw = QListWidget()
plot = pg.PlotWidget()
imv = pg.ImageView()

## Create a grid layout to manage the widgets size and position
layout = QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)   # button goes in upper-left
layout.addWidget(text, 1, 0)   # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1) 

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()