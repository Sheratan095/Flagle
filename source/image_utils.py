from PIL import Image
import globals  # Ensure the globals module is imported

def generate_combined_image(target_country : Image, guess_country : Image, current_suggestion_image : Image) -> Image:


	result_image : Image
	if (current_suggestion_image != None):
		result_image = current_suggestion_image.copy()
	else :
		result_image = Image.new('RGBA', (globals.max_width, globals.max_height))

	print(f"{globals.max_width} {globals.max_height}")
	print(f"{result_image.width} {result_image.height}")

	# Access pixel map
	dest_pixels = result_image.load()
	guess_pixels = guess_country.load()
	target_pixels = target_country.load()

	for y in range(globals.max_height):
		for x in range(globals.max_width):
			if (is_index_valid(guess_country, x, y) and is_index_valid(target_country, x, y)):
				if (pixels_are_close(guess_pixels[x, y], target_pixels[x, y])):
					dest_pixels[x, y] = target_pixels[x, y]

	result_image.save("result.png")

	return (result_image)

def pixels_are_close(p1, p2) -> bool:
	# Compare only R, G, B (ignore alpha for now)
	return all(abs(a - b) <= globals.color_tollerance for a, b in zip(p1[:3], p2[:3]))

def is_index_valid(img : Image, x: int, y: int) -> bool:
	if (x < 0 or y < 0):
		return (False)
	if (x >= img.width or y >= img.height):
		return (False)
	return (True)

def get_image_aspect_ratio(image: Image) -> float:

	return (image.width / image.height)
