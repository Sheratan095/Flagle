from PIL import Image, ImageTk
import Country

class Input:
	def __init__(self, canvas, text_id: int, image_id: int):
		self._canvas = canvas
		self._text_id = text_id
		self._image_id = image_id
		self._tk_image = None  # Store a reference to the Tkinter image

	def set_values(self, guessed_country : Country):
		# Convert PIL image to Tkinter PhotoImage
		image = guessed_country.image.resize((38, 25))  # Resize the image
		self._tk_image = ImageTk.PhotoImage(image)  # Store the reference
		self._canvas.itemconfig(self._text_id, text=guessed_country.name)
		self._canvas.itemconfig(self._image_id, image=self._tk_image)  # Update the text item with the image
		# self._canvas.delete(self._image_id)  # Use the stored reference
		# self._image_id = self._canvas.create_image(245.0, 237.0, image=self._tk_image, tags="image")

	def clear(self):
		self._canvas.itemconfig(self._text_id, text="")
		# TO DO add a placeholder image
		# self._canvas.itemconfig(self._image_id, image="")