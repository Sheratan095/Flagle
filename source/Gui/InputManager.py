from tkinter import Canvas, Label, Toplevel, Button
from Gui.Input import Input
import GuessResult
from PIL import ImageTk
from typing import List
import globals
from Gui.message_label import MessageLabel
from Gui.end_page import show_result_screen  # Import the new module

class InputManager:

	def __init__(self, main_image_idx: int, canvas: Canvas, message_label: MessageLabel):
		self._txtboxes: List[Input] = []
		self._current_idx = 0
		self._canvas = canvas
		self._main_image_idx = main_image_idx
		self._message_label = message_label  # Store the message label

	def add_input(self, input: Input):
		self._txtboxes.append(input)

	def start_game(self):
		for i in range(len(self._txtboxes)):
			self._txtboxes[i].clear()
		self._current_idx = 0
		self._message_label.config(text="")  # Clear any existing message

	def guess(self, guess: str):
		if (self._current_idx - 1 == globals.max_tries):
			return

		guess_result: GuessResult = globals.game.guess(guess)
		print(guess_result.guessed_country)

		if (guess_result.unknown_country):
			self._message_label.show_message()
			return

		self._message_label.hide_message()

		self._txtboxes[self._current_idx].set_values(guess_result.guessed_country)  # Set the guessed country in the input box
		self._current_idx += 1

		image = guess_result.merge_result.result_image.resize((globals.main_img_width, globals.main_img_height))  # Resize the image
		self._tk_image = ImageTk.PhotoImage(image)  # Store the reference
		self._canvas.itemconfig(self._main_image_idx, image=self._tk_image)  # Update the suggestion image

		if (guess_result.game_end):
			if (guess_result.win):
				show_result_screen(self._canvas.master, "You Win!", self._restart_game)
			else:
				show_result_screen(self._canvas.master, f"You Lose! The correct answer was: {globals.game.get_current_country()}", self._restart_game)
			return

	def show_win_screen(self):
		"""Display the win screen."""

	def show_lose_screen(self):
		"""Display the lose screen."""
		correct_country = globals.game._FlagleGame__current_country.name

	def _restart_game(self):
		"""Restart the game."""
		globals.game.start_game(globals.current_game_mode)

