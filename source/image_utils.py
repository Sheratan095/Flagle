from PIL import Image
from Country import Country
import string

def generate_combined_image(target_country_path : string, guess_country_path : string) -> Image:

	result_image : Image


	target_image = Image.open(target_country_path)
	guess_image = Image.open(guess_country_path)


	return (guess_image)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)