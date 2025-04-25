from PIL import Image
import string

# Define the standard aspect ratio here to avoid circular import
standard_aspect_ratio = 16 / 9

def generate_combined_image(target_country : Image, guess_country : Image) -> Image:

	result_image : Image


	return (target_country)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)


def get_standardized_image(path: string) -> Image:

	image : Image = Image.open(path)

	width, height = image.size
	image_aspect_ratio = width / height

	if image_aspect_ratio > standard_aspect_ratio:
		new_width = int(standard_aspect_ratio * height)
		new_height = height
	else:
		new_width = width
		new_height = int(width / standard_aspect_ratio)

	return (image.resize((new_width, new_height), Image.Resampling.LANCZOS))