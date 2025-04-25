class Country:
	def __init__(self, flag, latitude, longitude, name):
		self.flag = flag
		self.latitude = latitude
		self.longitude = longitude
		self.name = name

	def __repr__(self):
		# This provides a nice string representation of the object
		return f"Country(name={self.name}, latitude={self.latitude}, longitude={self.longitude}, flag={self.flag})"

	def __eq__(self, other):

		if (not isinstance(other, Country)):
			return (NotImplemented)

		return (self.name == other.name)