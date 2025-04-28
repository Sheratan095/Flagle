from tkinter import Entry, Button
from Gui.InputManager import InputManager
import globals
from PIL import Image, ImageTk
from Gui.events import on_button_click

def render_input_field(input_manager: InputManager) -> Entry :

	# Input field
	input_field = Entry(
		bd=0,
		bg=globals.background_color,
		fg=globals.input_color,
		highlightthickness=0
	)
	input_field.place(
		x=32.0,
		y=606.0,
		width=179.0,
		height=28.0
	)

	# Set focus on the input field
	input_field.focus_set()

	# Button
	image = Image.open("assets/btn.png")
	button_image_1 = ImageTk.PhotoImage(image.resize((24, 24)))
	button_1 = Button(
		image=button_image_1,
		borderwidth=0,
		bg=globals.background_color,
		activebackground=globals.background_color,  # Remove highlight when focuessed
		highlightthickness=0,
		command=lambda: on_button_click(input_field, input_manager),  # Pass input_field
		relief="flat"
	)

	button_1.image = button_image_1  # Store reference to prevent garbage collection
	button_1.place(
		x=235.0,
		y=606.0,
		width=29.0,
		height=29.0
	)

	return (input_field)
