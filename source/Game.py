from CountriesManager import CountriesManager
from GameMode import GameMode
from Country import Country
from GuessResult import GuessResult
from PIL import Image
import string

class FlagleGame:

	def __init__(self, max_tries: int):
		self.__countriesManger : CountriesManager = CountriesManager()
		self.__current_country : Country = None
		self.__max_tries : int = max_tries


	def start_game(self, game_mode: GameMode):

		self.__countriesManger.load_from_json(game_mode.value)
		self.__tries : int = 0
		self._get_random_country()

		print("Game started \n" + str(self.__current_country.name))

	def guess(self, guess_name: string) -> GuessResult:

		if (self.__last_country_name.name == guess_name):
			return (self._generate_guess_result(True, True, guess_name))

		self.__tries += 1

		return (self._generate_guess_result(False, self.__tries == self.__max_tries, guess_name))


	def _generate_guess_result(self, win : bool, game_end : bool, guess_name : string) -> GuessResult:
		# if the game is over, generate the result image
		if (game_end == True):
			return (GuessResult(
				game_end=game_end,
				win=win,
				tries=self.__tries,
				result_image=Image.open(self.__current_country.flag)
			))

		# if the game is not over, generate the resulting image
		return (GuessResult(
			game_end=game_end,
			win=win,
			tries=self.__tries,
			result_image=self._generate_combined_image()
		))

	def _generate_combined_image(self, guess_name : string) -> Image:
		# generate a random country
		# self.__current_country = self._get_random_country()

		# open the image
		image = Image.open(self.__current_country.flag)

		# resize the image to 200x200
		# image = image.resize((200, 200))

		return (image)

	def _get_random_country(self) -> Country:

		new_countrie : Country = None

		while (self.__current_country == new_countrie):
			new_countrie = self.__countriesManger.get_random_country()

		self.__current_country = new_countrie

		return (new_countrie)