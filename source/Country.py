from PIL import Image
from image_utils import *

class Country:

	def __init__(self, flag, latitude, longitude, name):

		self.__flag = flag
		self.latitude = latitude
		self.longitude = longitude
		self.name = name

		# preload the image
		self.image = get_standardized_image(flag)

	def __repr__(self):
		# This provides a nice string representation of the object
		return f"Country(name={self.name}, latitude={self.latitude}, longitude={self.longitude}, flag={self.__flag})"

	def __eq__(self, other):

		if (not isinstance(other, Country)):
			return (NotImplemented)

		return (self.name == other.name)