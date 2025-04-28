from tkinter import Tk, Canvas, Entry, Button
import Gui.render_geometry as geometry # Adjusted to use a relative import
import globals
from Gui.InputManager import InputManager
from Gui.render_txtboxes import render_inputs
from Gui.render_input_field import render_input_field

window = Tk()

window.geometry("300x700")
window.configure(bg = globals.background_color)
window.title("Flagle")
window.resizable(False, False)

canvas = Canvas(
	window,
	bg = globals.background_color,
	height = 700,
	width = 300,
	bd = 0,
	highlightthickness = 0,
	relief = "ridge"
)

canvas.place(x = 0, y = 0)

geometry.render_geometry(canvas)

# main image
main_image_idx : int = canvas.create_image(
	149.0,
	109.0,
	image=None
)

input_manager = InputManager(main_image_idx, canvas)
# Render input fields dynamically
render_inputs(canvas, input_manager)

render_input_field(input_manager)

canvas.create_text(
	90.0,
	666.0,
	anchor="nw",
	text="FLAGLE ",
	fill="#FFFFFF",
	font=("Inter Bold", 30 * -1)
)



