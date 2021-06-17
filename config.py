
class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Battleship War"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base = 100
		ratio = 5
		self.side = base * ratio
		self.screen = f"{self.side}x{self.side}+500+500"

		#IMG PATH
		self.logo = "img/logo.png"
		self.init_img = "img/init_img.png"
		self.final_img = "img/final_img.png"
		self.win_img = "img/win_img.png"