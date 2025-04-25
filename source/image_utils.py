from PIL import Image
import string

# Define the standard aspect ratio here to avoid circular import
standard_aspect_ratio = 16 / 9

def generate_combined_image(target_country : Image, guess_country : Image) -> Image:

	result_image : Image


	return (target_country)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)


def get_standardized_image(path: string, width: int = 1920, height: int = 1080) -> Image:

	image: Image = Image.open(path)

	return (image.resize((width, height), Image.Resampling.LANCZOS))