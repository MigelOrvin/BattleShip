
class Player:

	def __init__(self, name="john"):
		self.name = name

	def current_location(self, x, y):
		self.location = (x,y)