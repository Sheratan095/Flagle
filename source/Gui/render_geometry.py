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
		fill=globals.background_color,
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
		outline=globals.border_color)

	#Footer line
	canvas.create_rectangle(
		6.996467590332031,
		660.0,
		291.00354766845703,
		661.0,
		fill="#FFFFFF",
		outline=globals.border_color)



	# canvas.create_rectangle(
	# 	215.0,
	# 	524.0,
	# 	216.0,
	# 	560.0,
	# 	fill=globals.background_color,
	# 	outline=globals.border_color)

	# canvas.create_rectangle(
	# 	215.0,
	# 	463.0,
	# 	216.0,
	# 	499.0,
	# 	fill=globals.background_color,
	# 	outline=globals.border_color)

	# canvas.create_rectangle(
	# 	215.0,
	# 	402.0,
	# 	216.0,
	# 	438.0,
	# 	fill=globals.background_color,
	# 	outline=globals.border_color)

	# canvas.create_rectangle(
	# 	215.0,
	# 	341.0,
	# 	216.0,
	# 	377.0,
	# 	fill=globals.background_color,
	# 	outline=globals.border_color)

	# canvas.create_rectangle(
	# 	215.0,
	# 	280.0,
	# 	216.0,
	# 	316.0,
	# 	fill=globals.background_color,
	# 	outline=globals.border_color)
	

	# canvas.create_rectangle(
	# 	215.0,
	# 	219.0,
	# 	216.0,
	# 	255.0,
	# 	fill=globals.border_color,
	# 	outline=globals.border_color)