from PIL import ImageTk
import Country
import globals

class Input:
	def __init__(self, canvas, text_id: int, image_id: int, text: str):
		self._canvas = canvas
		self._text_id = text_id
		self._image_id = image_id
		self._text = text
		self._tk_image = None  # Store a reference to the Tkinter image

	def set_values(self, guessed_country : Country):
			# Truncate the country name if it's too long
			max_length = globals.max_lenght_txtbox  # Set the maximum length for the text

			# Convert PIL image to Tkinter PhotoImage
			image = guessed_country.image.resize((globals.txtbox_img_width, globals.txtbox_img_height))  # Resize the image
			self._tk_image = ImageTk.PhotoImage(image)  # Store the reference
			self._canvas.itemconfig(self._image_id, image=self._tk_image)  # Update the image
			self._canvas.itemconfig(self._text_id, text=globals.get_fixed_country_name(guessed_country.name, max_length))  # Update the text

	def clear(self):

		if (self._canvas.itemcget(self._text_id, "text") == self._text):
			return

		self._canvas.itemconfig(self._text_id, text=self._text)
		self._canvas.itemconfig(self._image_id, image="")  # Clear the image