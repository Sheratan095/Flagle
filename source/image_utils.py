from PIL import Image
import globals  # Ensure the globals module is imported

def generate_combined_image(target_country : Image, guess_country : Image, current_suggestion_image : Image) -> Image:


	result_image : Image
	if (current_suggestion_image != None):
		result_image = current_suggestion_image
	else :
		result_image = Image.new('RGBA', (globals.max_width, globals.max_height))

	print(f"{globals.max_width} {globals.max_height}")

	# Access pixel map
	pixels = result_image.load()

	pixels[1000, 1000] = (255, 255, 255, 0)  # Set a pixel to white
	if (is_index_valid(result_image, 1000, 1000)):
		print("added")
		print(pixels[1000, 1000])  # Print the pixel value

	return (result_image)

def is_index_valid(img : Image, x: int, y: int) -> bool:
	if (x < 0 or y < 0):
		return (False)
	if (x > img.width or y > img.height):
		return (False)
	return (True)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)
