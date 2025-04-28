from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import globals

def render_geometry(canvas : Canvas):
	print("Rednering geometry")


	# Main image
	rect_x1 = 149.0 - 260 / 2  # Top-left x-coordinate
	rect_y1 = 109.0 - 180 / 2  # Top-left y-coordinate
	rect_x2 = 149.0 + 260 / 2  # Bottom-right x-coordinate
	rect_y2 = 109.0 + 180 / 2  # Bottom-right y-coordinate

	canvas.create_rectangle(
		rect_x1, rect_y1, rect_x2, rect_y2,
		fill=globals.main_img_background,
		outline=globals.border_color
	)


	#First try
	canvas.create_rectangle(
		26.0,
		216.0,
		273.0,
		260.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Second try
	canvas.create_rectangle(
		26.0,
		277.0,
		273.0,
		321.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Third try
	canvas.create_rectangle(
		26.0,
		338.0,
		273.0,
		382.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Fourth try
	canvas.create_rectangle(
		26.0,
		399.0,
		273.0,
		443.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Fifth try
	canvas.create_rectangle(
		26.0,
		460.0,
		273.0,
		504.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Sixth try
	canvas.create_rectangle(
		26.0,
		521.0,
		273.0,
		565.0,
		fill=globals.background_color,
		outline=globals.border_color)

	#Guess
	canvas.create_rectangle(
		26.0,
		599.0,
		273.0,
		643.0,
		fill=globals.background_color,
		outline=globals.input_color)

	#Footer line
	canvas.create_rectangle(
		6.996467590332031,
		660.0,
		291.00354766845703,
		661.0,
		fill="#FFFFFF",
		outline=globals.border_color)

	# Define positions for rectangles relative to the images
	positions = [
		(245.0, 237.0),  # First try
		(245.0, 298.0),  # Second try
		(245.0, 359.0),  # Third try
		(245.0, 420.0),  # Fourth try
		(245.0, 481.0),  # Fifth try
		(245.0, 542.0),  # Sixth try
	]

	# Rectangle dimensions (38x25 to match the image size)
	rect_width = globals.txtbox_img_width - 2
	rect_height = globals.txtbox_img_height - 1

	# Create rectangles for each position
	for x_center, y_center in positions:
		x1 = x_center - rect_width / 2  # Top-left x-coordinate
		y1 = y_center - rect_height / 2  # Top-left y-coordinate
		x2 = x_center + rect_width / 2  # Bottom-right x-coordinate
		y2 = y_center + rect_height / 2  # Bottom-right y-coordinate

		canvas.create_rectangle(
			x1, y1, x2, y2,
			fill=globals.background_color,  # Match the background color
			outline=globals.border_color    # Optional: Add a border color
		)