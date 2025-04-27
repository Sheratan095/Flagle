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

	if (target_country.size > guess_country.size):
		biggest_img = target_country
		smallest_img = guess_country
	else :
		biggest_img = guess_country
		smallest_img = target_country

	# Access pixel map
	dest_pixels = result_image.load()
	biggest_pixels = biggest_img.load()
	smallest_pixels = smallest_img.load()

	starting_y : int = (biggest_img.height - smallest_img.height) // 2

	# Draw a square around the point (100, 100)
	square_size = 10  # Size of the square (half-length of each side)
	center_x, center_y = 1000, 410

	for y in range(center_y - square_size, center_y + square_size + 1):
		for x in range(center_x - square_size, center_x + square_size + 1):
			if is_index_valid(result_image, x, y):
				dest_pixels[x, y] = (255, 0, 0, 255)  # Red color with full opacity

	# print(f"Starting y: {starting_y}")
	# print(f"Smallest img height: {smallest_img.height}")
	# print(f"Biggest img height: {biggest_img.height}")
	# print(f"difference: {biggest_img.height - smallest_img.height}")

	# for y in range(smallest_img.height):
	# 	for x in range(smallest_img.width):
	# 		if (is_index_valid(biggest_img, x, y + starting_y) and is_index_valid(smallest_img, x, y)):
	# 			if (pixels_are_close(biggest_pixels[x, y + starting_y], smallest_pixels[x, y])):
	# 				dest_pixels[x, y + starting_y] = biggest_pixels[x, y + starting_y]

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
