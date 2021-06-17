import tkinter as tk
from game_stat import Game_Stat
from config import Config
from board import Board
from ship import Ship
from player import Player
from login import LoginPage


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game # battleship
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_loginPage()
		

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_loginPage(self):
		self.pages['login'] = LoginPage(self.container, self)


class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.game_stat = Game_Stat()
		self.player = Player()
		self.window = Window(self)


	def check_location(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def window_button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)

		win = self.check_location()
		self.window.pages["board"].change_image_btn(pos_x, pos_y, win)
		if win:
			print("you win")
			self.window.destroy()

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()