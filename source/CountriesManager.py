from Country import Country
from GameMode import GameMode
import globals  # Ensure the globals module is imported
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

		with open(self.__current_game_mode, "r", encoding="utf-8") as file:

			data = json.load(file)

			# for each entry in the json file, create a new country object and add it to the list
			for entry in data:
				country = Country(
					flag= os.path.splitext(self.__current_game_mode)[0] + "/" + entry["flag"],
					# latitude=entry["latitude"],
					# longitude=entry["longitude"],
					name=entry["name"]
				)
				self.__countries.append(country)
		
		self._get_max_dimensions()

	def _get_max_dimensions(self):
		max_w = 0
		max_h = 0

		# find the max width and height of the images
		for country in self.__countries:
			if (country.get_img_width() > max_w):
				max_w = country.get_img_width()
			if (country.get_img_height() > max_h):
				max_h = country.get_img_height()

		# Correctly reference the globals module
		globals.max_width = max_w
		globals.max_height = max_h


	def get_random_country(self):
		if (globals.testing == True):
			# if the game is in testing mode, return the first country
			return (self.get_country_by_name(globals.testing_nation))
		return (random.choice(self.__countries))


	def print_countries(self):
		for country in self.__countries:
			print(country)


	def get_country_by_name(self, name: str) -> Country:

		for country in self.__countries:
			if (country.name.lower() == name):
				return (country)

		return (None)

	# get the countries that match the name
	def get_matching_countries(self, name: str) -> list[Country]:

		matching_countries : list[Country] = []

		for country in self.__countries:
			if (country.name.lower().startswith(name.lower())):
				matching_countries.append(country)

		return (matching_countries)