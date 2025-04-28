import json
import string
from Game import FlagleGame
from GameMode import GameMode

# BACKEND
mode : GameMode = GameMode.World

max_tries: int = 6

testing : bool = False
testing_nation : str = "Nepal"
trasparent : tuple = (0, 0, 0, 0)

color_tollerance : int = 40

max_width : int = 0
max_height : int = 0


#FRONTEND
background_color : string =  "#1D2951"
border_color : string = "#8A8A8A"
input_color : string = "#FFFFFF"
img_width_GUI: int = 300
img_height_GUI: int = 200
max_lenght_txtbox: int = 27

txtbox_img_width: int = 38
txtbox_img_height: int = 25
main_img_width: int = 247
main_img_height: int = 165
main_img_background: string = "#243364"





with open("../config.json", "r") as file:

	data = json.load(file)

	max_tries = data["number_of_tries"]

game : FlagleGame = FlagleGame(max_tries)