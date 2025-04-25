from dataclasses import dataclass
from PIL import Image

@dataclass
class GuessResult:
	game_end : bool
	win : bool
	tries : int
	result_image :Image