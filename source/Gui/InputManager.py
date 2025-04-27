from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Gui.Input import Input
import MergeResult
import GuessResult
from PIL import Image, ImageTk
from typing import List
import globals

class InputManager:

	def __init__(self, main_image_idx : int, canvas : Canvas):
		self._inputs : List[Input] = []
		self._current_idx = 0
		self._canvas = canvas
		self._main_image_idx = main_image_idx

	def add_input(self, input : Input):
		self._inputs.append(input)

	def start_game(self):
		for i in range(len(self._inputs)):
			self._inputs[i].clear()
		self._current_idx = 0

	def guess(self, guess : str):
		if (self._current_idx == globals.max_tries):
			return

		guess_result : GuessResult = globals.game.guess(guess)
		if (guess_result.game_end):
			return

		if (guess_result.unknown_country):
			return

		self._inputs[self._current_idx].set_values(guess_result.guessed_country)
		self._current_idx += 1

		image = guess_result.merge_result.result_image.resize((247, 165))  # Resize the image
		self._tk_image = ImageTk.PhotoImage(image)  # Store the reference
		self._canvas.itemconfig(self._main_image_idx, image=self._tk_image)  # Update the suggestion image

