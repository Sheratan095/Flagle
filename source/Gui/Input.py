from PIL import Image

class Input:
	def __init__(self, canvas, text_id: int, image_id: int):
		self._canvas = canvas
		self._text_id = text_id
		self._image_id = image_id

	def set_values(self, country_name: str, image: Image):
		self._canvas.itemconfig(self._text_id, text=country_name)
		self._canvas.itemconfig(self._image_id, image=image)

	def clear(self):
		self._canvas.itemconfig(self._text_id, text="")
		# TO DO add a placeholder image
		# self._canvas.itemconfig(self._image_id, image="")