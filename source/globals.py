import json
import string
from Game import FlagleGame
from GameMode import GameMode

mode : GameMode = GameMode.World

number_of_tries : int = 5

testing : bool = True
testing_nation : str = "Nepal"
trasparent : tuple = (0, 0, 0, 0)

color_tollerance : int = 40

max_width : int = 0
max_height : int = 0


background_color : string =  "#1D2951"
# border_color : string = "#8A8A8A"
border_color : string = "#fc0303"








with open("../config.json", "r") as file:

	data = json.load(file)

	number_of_tries = data["number_of_tries"]

game : FlagleGame = FlagleGame(number_of_tries)