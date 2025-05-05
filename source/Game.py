from CountriesManager import CountriesManager
from GameMode import GameMode
from Country import Country
from GuessResult import GuessResult
from image_utils import *
import string

class FlagleGame:

	def __init__(self, max_tries: int):
		self.__countriesManger : CountriesManager = CountriesManager()
		self.__current_country : Country = None
		self.__max_tries : int = max_tries
		self.__current_suggestion_image : Image = None


	def start_game(self, game_mode: GameMode):

		self.__countriesManger.load_from_json(game_mode.value)
		self.__tries : int = 0
		self.__current_suggestion_image = None  # Reset the suggestion image
		self._get_random_country()

		print("Game started \nTarget country is: " + str(self.__current_country.name))


	def get_current_country(self) -> Country:
		if (self.__tries == self.__max_tries):
			return (self.__current_country)

	def guess(self, guess: string) -> GuessResult:

		guess_name = guess.lower()

		if (self.__current_country.name.lower() == guess_name):
			return (self._generate_guess_result(True, True, guess_country=self.__current_country))

		guess_country : Country = self.__countriesManger.get_country_by_name(guess_name)

		# if the country is not found, return a special result
		if (guess_country == None):
			return (GuessResult(
				tries=self.__tries,
				unknown_country=True
			))

		self.__tries += 1

		return (self._generate_guess_result(False, self.__tries == self.__max_tries, guess_country))

	def get_matching_countries(self, name: str) -> list[Country]:
		return (self.__countriesManger.get_matching_countries(name))


	def _generate_guess_result(self, win : bool, game_end : bool, guess_country : Country) -> GuessResult:
		# if the game is over, generate the result image
		if (game_end == True):
			return (GuessResult(
				guessed_country=guess_country,
				game_end=game_end,
				win=win,
				tries=self.__tries,
				merge_result=MergeResult(result_image=self.__current_country.image, percentage=100.0)
			))

		marge_resutlt : MergeResult = merge_images(self.__current_country.image, guess_country.image, self.__current_suggestion_image)
		self.__current_suggestion_image = marge_resutlt.result_image

		# if the game is not over, generate the resulting image
		return (GuessResult(
			guessed_country=guess_country,
			game_end=game_end,
			win=win,
			tries=self.__tries,
			merge_result=marge_resutlt
		))


	def _get_random_country(self) -> Country:

		new_countrie : Country = None

		while (self.__current_country == new_countrie or new_countrie == None):
			new_countrie = self.__countriesManger.get_random_country()

		self.__current_country = new_countrie

		return (new_countrie)