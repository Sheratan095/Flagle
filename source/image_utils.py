from PIL import Image
from Country import Country

def generate_combined_image(target_country : Country, guess_country : Country) -> Image:

	result_image : Image


	return (target_country.image)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)