from Country import Country
import json

class Countries:
	def __init__(self):
		self.countries : list[Country] = []

	def load_from_json(self, filename: str):
		with open(filename, "r") as file:

			data = json.load(file)

			for entry in data:
				country = Country(
					flag=entry["flag"],
					latitude=entry["latitude"],
					longitude=entry["longitude"],
					name=entry["name"]
				)

				self.countries.append(country)

	def print_countries(self):
		for country in self.countries:
			print(country)
		