from tkinter import Label
import globals

class MessageLabel:
	def __init__(self, window):
		self._label = Label(
			window,
			text="Unknown country!",
			bg=globals.background_color,
			fg="#FF0000",  # Red text for error messages
			font=("Inter Bold", 12),
		)
		self._x = 32
		self._y = 580
		self._label.place(x=self._x, y=self._y)
		self._label.place_forget()
		self._is_shown = False

	def show_message(self, delay: int = 100):

		if (self._is_shown == True):
			self._label.place_forget()
			# Schedule the label to hide after the specified delay
			self._label.after(delay, lambda: self._label.place(x=self._x, y=self._y))
		else:
			self._label.place(x=self._x, y=self._y)

		self._is_shown = True


	def hide_message(self):
		"""Hide the message label."""
		self._label.place_forget()
		self._is_shown = False
