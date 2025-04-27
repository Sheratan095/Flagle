from dataclasses import dataclass
import MergeResult

@dataclass
class GuessResult:
	game_end : bool = False
	win : bool = False
	tries : int = 0
	merge_result :MergeResult = None
	unknown_country : bool = False