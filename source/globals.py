import json
import os
from Game import FlagleGame
from GameMode import GameMode

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config.json using an absolute path
config_path = os.path.join(BASE_DIR, "config.json")
with open(config_path, "r") as file:
	data = json.load(file)

# BACKEND
mode: GameMode = GameMode.World
max_tries: int = data["number_of_tries"]
color_tollerance: int = data["backend"]["color_tollerance"]
testing: bool = data["backend"]["testing"]
testing_nation: str = data["backend"]["testing_nation"]
trasparent: tuple = tuple(data["backend"]["trasparent"])

# FRONTEND
main_screen_idx: int = data["frontend"]["main_screen_idx"]
background_color: str = data["frontend"]["background_color"]
border_color: str = data["frontend"]["border_color"]
input_color: str = data["frontend"]["input_color"]
img_width_GUI: int = data["frontend"]["img_width_GUI"]
img_height_GUI: int = data["frontend"]["img_height_GUI"]
max_lenght_txtbox: int = data["frontend"]["max_lenght_txtbox"]
txtbox_placeholder: str = data["frontend"]["txtbox_placeholder"]
txtbox_placeholder_color: str = data["frontend"]["txtbox_placeholder_color"]
txtbox_img_width: int = data["frontend"]["txtbox_img_width"]
txtbox_img_height: int = data["frontend"]["txtbox_img_height"]
main_img_width: int = data["frontend"]["main_img_width"]
main_img_height: int = data["frontend"]["main_img_height"]
main_img_background: str = data["frontend"]["main_img_background"]

#red
test_color: str = "#FF0000"

# Initialize the game
game: FlagleGame = FlagleGame(max_tries)


def get_fixed_country_name(country_name: str, max_length: int) -> str:

	fixed_name = country_name

	if (len(country_name) > max_length):
		fixed_name = country_name[:max_length - 3] + "..."
	return (fixed_name)