from dataclasses import dataclass
from PIL import Image

@dataclass
class MergeResult:
	percentage : float = 0.0
	result_image : Image = None