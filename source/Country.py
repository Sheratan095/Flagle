from PIL import Image
from image_utils import *

class Country:

	def __init__(self, flag, latitude, longitude, name):

		self.__flag = flag
		self.latitude = latitude
		self.longitude = longitude
		self.name = name

		# preload the image
		self.image = Image.open(flag)
		# self.image = self.image.resize((1280, 800))  # Correct usage of resize


	def __repr__(self):
		# This provides a nice string representation of the object
		return f"Country(name={self.name}, latitude={self.latitude}, longitude={self.longitude}, flag={self.__flag}, height={self.image.height}, width={self.image.width})"

	def get_img_width(self):
		return (self.image.width)

	def get_img_height(self):
		return (self.image.height)

	def __eq__(self, other):

		if (not isinstance(other, Country)):
			return (NotImplemented)

		return (self.name == other.name)