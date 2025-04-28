from Gui.Input import Input
from Gui.InputManager import InputManager
from tkinter import Canvas
import globals

def render_inputs(canvas: Canvas, input_manager: InputManager):

	positions = [
		(31.0, 229.0, 245.0, 237.0),  # First try
		(32.0, 290.0, 245.0, 298.0),  # Second try
		(32.0, 351.0, 245.0, 359.0),  # Third try
		(32.0, 412.0, 245.0, 420.0),  # Fourth try
		(32.0, 473.0, 245.0, 481.0),  # Fifth try
		(32.0, 534.0, 245.0, 542.0),  # Sixth try
	]

	for idx, (text_x, text_y, image_x, image_y) in enumerate(positions):
		text_id = canvas.create_text(
			text_x,
			text_y,
			anchor="nw",
			text=f"{['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth'][idx]} try",
			fill=globals.border_color,
			font=("Inter Bold", 15 * -1)
		)

		image_id = canvas.create_image(
			image_x,
			image_y,
			image=None
		)

		input_field = Input(canvas, text_id, image_id)
		input_manager.add_input(input_field)