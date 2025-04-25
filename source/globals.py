import json
from Game import FlagleGame
from GameMode import GameMode

mode : GameMode = GameMode.World

number_of_tries = 5

with open("config.json", "r") as file:

	data = json.load(file)

	number_of_tries = data["number_of_tries"]

game : FlagleGame = FlagleGame(number_of_tries)