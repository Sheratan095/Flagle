from tkinter import Entry, Button
from Gui.InputManager import InputManager
import globals
from PIL import Image, ImageTk
from Gui.events import on_button_click

def render_input_field(input_manager: InputManager):
	# Placeholder text
	placeholder_text = "Enter your guess here"

	# Input field
	input_field = Entry(
		bd=0,
		bg=globals.background_color,
		fg=globals.input_color,
		highlightthickness=0,
		insertbackground=globals.input_color  # Set the cursor color
	)
	input_field.place(
		x=32.0,
		y=606.0,
		width=179.0,
		height=28.0
	)

	# Add placeholder functionality
	def add_placeholder(event=None):
		if (input_field.get() == ""):
			input_field.insert(0, placeholder_text)
			input_field.config(fg=globals.txtbox_placeholder_color)  # Set placeholder text color
			input_field.icursor(0)  # Set the cursor at position 0

	def on_focus_out(event):
		add_placeholder()  # Add placeholder when focused

	def on_key_press(event):
		if (input_field.get() == placeholder_text):
			input_field.delete(0, 'end')
			input_field.config(fg=globals.input_color)

	def on_key_relase(event):
		if (input_field.get() == ""):
			add_placeholder()
		if (input_field.get() != placeholder_text and input_field.get() != ""):
			for c in globals.game.get_matching_countries(input_field.get()):
				print(c.name)

	input_field.bind("<FocusOut>", on_focus_out)
	input_field.bind("<Key>", on_key_press)  # Change text color on key press
	input_field.bind("<KeyRelease>", on_key_relase)  # Change text color on key release

	# Initialize with placeholder
	add_placeholder()

	input_field.focus_set()  # Set focus to the input field

	# Button
	image = Image.open("assets/btn.png")
	button_image_1 = ImageTk.PhotoImage(image.resize((24, 24)))
	button_1 = Button(
		image=button_image_1,
		borderwidth=0,
		bg=globals.background_color,
		activebackground=globals.background_color,  # Remove highlight when focused
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
