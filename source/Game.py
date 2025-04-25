from CountriesManager import CountriesManager
from GameMode import GameMode
import string

class FlagleGame:

	def __init__(self):
		self.__countriesManger : CountriesManager = CountriesManager()
		self.__game_mode : GameMode = GameMode.NotAssigned
		self.__last_country_name : string = None

	def start_game(self, game_mode: GameMode):
		self.__countriesManger.load_from_json(game_mode.value)
		self.__game_mode = game_mode
		self.__guess : int = 0

	def get_random_country(self):

		new_countrie = None

		while (self.__last_country_name == new_countrie.name):
			new_countrie = self.__countriesManger.get_random_country()

		self.__last_country_name = new_countrie.name

		return (new_countrie)