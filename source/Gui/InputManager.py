from tkinter import Canvas, Entry
from Gui.Input import Input
import GuessResult
from PIL import ImageTk
from typing import List
import globals
from Gui.message_label import MessageLabel
from Gui.end_pages import show_result_screen  # Import the new module

class InputManager:

	def __init__(self, main_image_idx: int, canvas: Canvas, message_label: MessageLabel):
		self._txtboxes: List[Input] = []
		self._current_idx = 0
		self._canvas = canvas
		self._main_image_idx = main_image_idx
		self._message_label = message_label  # Store the message label
		self.input_fied: Entry = None

	# Pass the input field to the InputManager
	def set_input_field(self, input_field: Entry):
		self.input_fied = input_field

	def add_input(self, input: Input):
		self._txtboxes.append(input)

	def start_game(self):
		for i in range(len(self._txtboxes)):
			self._txtboxes[i].clear()
		self._current_idx = 0
		self._canvas.itemconfig(self._main_image_idx, image="")
		if (self.input_fied is not None):
			self.input_fied.config(
				state="normal",
			)
			self.input_fied.delete(0, 'end')
		# self._message_label.config(text="")  # Clear any existing message

	def guess(self, guess: str):

			if (self._current_idx - 1 == globals.max_tries):
				return

			guess_result: GuessResult = globals.game.guess(guess)

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

				# Disable the input field and set custom colors
				if self.input_fied is not None:
					self.input_fied.config(
						state="disabled",
						disabledbackground=globals.background_color,  # Use the global background color
						disabledforeground=globals.input_color       # Use the global input color
					)

				if (guess_result.win):
					show_result_screen(self._canvas.master, "You Win!", self)
				else:
					show_result_screen(self._canvas.master, f"You Lose! The correct answer was: {globals.game.get_current_country()}", self)
				return

	def show_win_screen(self):
		"""Display the win screen."""

	def show_lose_screen(self):
		"""Display the lose screen."""
		correct_country = globals.game._FlagleGame__current_country.name

