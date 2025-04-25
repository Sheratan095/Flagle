from CountriesManager import CountriesManager

class FlagleGame:

	def __init__(self):
		self.__countriesManger : CountriesManager = CountriesManager()
		self.__game_mode = None

	def set_mode(self, new_mode):
		self.__game_mode = new_mode

		self.__countriesManger.load_from_json(self.__game_mode.value)

	def get_random_country(self):
		return (CountriesManager.get_random_country())