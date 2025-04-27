from dataclasses import dataclass
import MergeResult
import Country

@dataclass
class GuessResult:
	game_end : bool = False
	guessed_country : Country = ""
	win : bool = False
	tries : int = 0
	merge_result :MergeResult = None
	unknown_country : bool = False