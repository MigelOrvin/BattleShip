#loginPage.py
import tkinter as tk
from PIL import Image, ImageTk



class LoginPage(tk.Frame):
	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.config.row, width=self.config.column, bg="white")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.logo)
		image_w, image_h = image.size
		ratio = image_w/self.config.column
		image = image.resize((int(image_w*ratio//80),int(image_h*ratio//100)))

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(fill="both" ,expand=True)

		self.btn_login = tk.Button(self.main_frame, text="START GAME", font=("Arial", 22, "bold"),bg="white",bd="8", command=lambda:self.game.change_page("board"))
		self.btn_login.pack(pady=5, expand=True)

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 22, "bold"),fg="red",bg="white", bd="8", command=lambda:self.game.destroy())
		self.btn_exit.pack(pady=5,expand=True)
