from Country import Country
import json
import random

class CountriesManager:

	def __init__(self):
		# __ make it private
		self.__countries : list[Country] = []

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

				self.__countries.append(country)

	def get_random_country(self):
		return (random.choice(self.__countries))

	def print_countries(self):
		for country in self.__countries:
			print(country)
		