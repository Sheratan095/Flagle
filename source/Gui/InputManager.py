from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Gui.Input import Input
import MergeResult
import GuessResult
from typing import List
import globals

class InputManager:

	def __init__(self):
		self._inputs : List[Input] = []
		self._current_idx = 0

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
