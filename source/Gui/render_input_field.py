from tkinter import Entry, Button
from Gui.InputManager import InputManager
import globals
from PIL import Image, ImageTk

def render_input_field(input_manager: InputManager):

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

def on_button_click(input_field: Entry, input_manager: InputManager):

	if (input_field.get() == ""):
		return

	input_manager.guess(input_field.get())