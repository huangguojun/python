import sys
from PySide import QtGui

class Example(QtGui.QWidget):
	
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()
	
	def initUI(self):
		self.btn = QtGui.QPushButton('Dialog',self)
		self.btn.move(20,20)
		self.btn.clicked.connect(self.showDialog)
		self.show()


	def showDialog(self):
		pass


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()

