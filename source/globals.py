import json
from FlagleGame import FlagleGame
from GameMode import GameMode

mode : GameMode = GameMode.World

game : FlagleGame = FlagleGame()

with open("config.json", "r") as file:

	data = json.load(file)

	game.set_mode(mode)