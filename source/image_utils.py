from PIL import Image
import globals  # Ensure the globals module is imported

def generate_combined_image(target_country : Image, guess_country : Image, current_suggestion_image : Image) -> Image:


	result_image : Image
	if (current_suggestion_image != None):
		result_image = current_suggestion_image.copy()
	else :
		result_image = Image.new('RGBA', (globals.max_width, globals.max_height))

	print(f"{globals.max_width} {globals.max_height}")

	# Access pixel map
	dest_pixels = result_image.load()
	target_pixels = target_country.load()
	guess_pixels = guess_country.load()

	for x in range(globals.max_width):
		for y in range(globals.max_height):
			if (is_index_valid(target_country, x, y) and is_index_valid(guess_country, x, y)):
				if (target_pixels[x, y] == guess_pixels[x, y]):
					# If the pixels are the same, set the pixel to the target pixel
					dest_pixels[x, y] = target_pixels[x, y]

	result_image.save('output_with_transparency.png')


	return (result_image)

def is_index_valid(img : Image, x: int, y: int) -> bool:
	if (x < 0 or y < 0):
		return (False)
	if (x >= img.width or y >= img.height):
		return (False)
	return (True)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)
