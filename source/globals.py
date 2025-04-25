import json
from Game import FlagleGame
from GameMode import GameMode

mode : GameMode = GameMode.World

game : FlagleGame = FlagleGame(5)

with open("config.json", "r") as file:

	data = json.load(file)
