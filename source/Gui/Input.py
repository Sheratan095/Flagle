from PIL import Image
from Gui.main_page import canvas

class Input:
	def __init__(self, text_id : int, image_id : int):
		self._text_id = text_id
		self._image_id = image_id

	def set_values(self, country_name: str, image: Image):
		canvas.itemconfig(self._text_id, text=country_name)
		canvas.itemconfig(self._image_id, image=image)

	def clear(self):
		canvas.itemconfig(self._text_id, text="")
		# TO DO add a placeholder image
		# canvas.itemconfig(self._image_id, image="")