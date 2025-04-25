from Country import Country
from GameMode import GameMode
import json
import random
import os

class CountriesManager:

	def __init__(self):
		# __ make it private
		self.__countries : list[Country] = []
		self.__current_game_mode : GameMode = GameMode.NotAssigned

	def load_from_json(self, game_mode: GameMode):

		# if the game mode is the same, do nothing
		#	because the json file is already loaded
		if (self.__current_game_mode == game_mode):
			return

		# if the game mode is not the same, load the new json file
		self.__current_game_mode = game_mode

		# clear the list of countries , usefull when the game mode is changed in run time
		self.__countries.clear()

		with open(self.__current_game_mode, "r") as file:

			data = json.load(file)

			# for each entry in the json file, create a new country object and add it to the list
			for entry in data:
				country = Country(
					flag= os.path.splitext(self.__current_game_mode)[0] + "/" + entry["flag"],
					latitude=entry["latitude"],
					longitude=entry["longitude"],
					name=entry["name"]
				)

				self.__countries.append(country)

		self.print_countries()


	def get_random_country(self):
		return (random.choice(self.__countries))

	def print_countries(self):
		for country in self.__countries:
			print(country)
	
	def get_country_by_name(self, name: str) -> Country:

		for country in self.__countries:
			if (country.name == name):
				return (country)

		return (None)
		