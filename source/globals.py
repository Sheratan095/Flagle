import json
from Countries import Countries
from GameMode import GameMode

mode = GameMode.World
countries: Countries = Countries()

with open("config.json", "r") as file:

	data = json.load(file)

	countries.load_from_json(mode.value)