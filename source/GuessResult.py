from dataclasses import dataclass
from PIL import Image

@dataclass
class GuessResult:
	game_end : bool = False
	win : bool = False
	tries : int = 0
	result_image :Image = None
	unknown_country : bool = False