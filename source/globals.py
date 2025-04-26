import json
from Game import FlagleGame
from GameMode import GameMode

mode : GameMode = GameMode.World

number_of_tries : int = 5

testing : bool = True
testing_nation : str = "Germany"

max_width : int = 0
max_height : int = 0

with open("config.json", "r") as file:

	data = json.load(file)

	number_of_tries = data["number_of_tries"]

game : FlagleGame = FlagleGame(number_of_tries)