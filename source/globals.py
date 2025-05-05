import json
import string
import os  # Import os to work with absolute paths
from Game import FlagleGame
from GameMode import GameMode

# BACKEND
mode: GameMode = GameMode.World

max_tries: int = 6

testing: bool = False
testing_nation: str = "Nepal"
trasparent: tuple = (0, 0, 0, 0)

color_tollerance: int = 40

max_width: int = 0
max_height: int = 0


# FRONTEND
main_screen_idx: int = 1
background_color: string = "#1D2951"
border_color: string = "#8A8A8A"
input_color: string = "#FFFFFF"
img_width_GUI: int = 300
img_height_GUI: int = 200
max_lenght_txtbox: int = 25
txtbox_placeholder: string = "Guess the country"
txtbox_placeholder_color: string = "gray"

txtbox_img_width: int = 38
txtbox_img_height: int = 25
main_img_width: int = 247
main_img_height: int = 165
main_img_background: string = "#243364"

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config.json using an absolute path
config_path = os.path.join(BASE_DIR, "config.json")
with open(config_path, "r") as file:
	data = json.load(file)
	max_tries = data["number_of_tries"]

game: FlagleGame = FlagleGame(max_tries)


def get_fixed_country_name(country_name: str, max_length: int) -> str:
	
	fixed_name = country_name

	if (len(country_name) > max_length):
		fixed_name = country_name[:max_length - 3] + "..."
	return (fixed_name)