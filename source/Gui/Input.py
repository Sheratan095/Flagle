from PIL import ImageTk
import Country
import globals

class Input:
	def __init__(self, canvas, text_id: int, image_id: int):
		self._canvas = canvas
		self._text_id = text_id
		self._image_id = image_id
		self._tk_image = None  # Store a reference to the Tkinter image

	def set_values(self, guessed_country : Country):
			# Truncate the country name if it's too long
			max_length = globals.max_lenght_txtbox  # Set the maximum length for the text
			country_name = guessed_country.name
			if len(country_name) > max_length:
				country_name = country_name[:max_length - 3] + "..."  # Truncate and add ellipsis

			# Convert PIL image to Tkinter PhotoImage
			image = guessed_country.image.resize((38, 25))  # Resize the image
			self._tk_image = ImageTk.PhotoImage(image)  # Store the reference
			self._canvas.itemconfig(self._image_id, image=self._tk_image)  # Update the image
			self._canvas.itemconfig(self._text_id, text=country_name)  # Update the text

	def clear(self):
		self._canvas.itemconfig(self._text_id, text="")
		# TO DO add a placeholder image
		# self._canvas.itemconfig(self._image_id, image="")