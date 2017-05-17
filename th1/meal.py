class Meal:
	def __init__(self,food="omelet",drink="coffee"):
		self.name = "gemeric ,meal"
		self.food = food
		self.drink = drink
	def printIt(self,prefix=''):
		print("A fine " ,self.name ,"with ",self.food,"and ",self.drink)
	def setFood(self,food):
		self.food = food
	def setDrink(self,drink):
		self.drink = drink
	def setName(self,name):
		self.name = name


