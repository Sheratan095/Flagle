from tkinter import Entry, Button, Frame, Label
from Gui.InputManager import InputManager
import globals
from PIL import Image, ImageTk
from Gui.events import on_button_click
from Country import Country

input_x = 32.0
input_y = 606.0
input_width = 179.0
input_height = 28.0

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
		x=input_x,
		y=input_y,
		width=input_width,
		height=input_height
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

	# Frame to display matching countries (placed completely above the input field)
	matching_frame = Frame(bg=globals.input_color)

	def update_matching_countries():
		# Clear the frame
		for widget in matching_frame.winfo_children():
			widget.destroy()
		matching_frame.place_forget()

		matching_countries: list[Country] = globals.game.get_matching_countries(input_field.get())

		# Adjust the height dynamically based on the number of matching countries
		if matching_countries:
			# Start the frame slightly higher than the textbox and grow upward
			frame_height = len(matching_countries) * 20  # Increased height for better spacing
			matching_frame.place(x=input_x, y=input_y - frame_height - 10, width=237, height=frame_height)

		for country in matching_countries:
			# Create a container frame for each country
			country_frame = Frame(matching_frame, bg=globals.background_color, height=12)  # Adjusted height for each entry
			country_frame.pack(fill="x")

			# Display country name (aligned to the left)
			name_label = Label(
				country_frame, 
				text=country.name, 
				fg=globals.input_color, 
				bg=globals.background_color, 
				anchor="w", 
				font=("Arial", 12)  # Adjusted font size
			)
			name_label.pack(side="left")

			# Load and display flag image (aligned to the right)
			flag_image = Image.open(country.get_flag()).resize((32, 24))  # Adjusted flag size
			flag_photo = ImageTk.PhotoImage(flag_image)
			flag_label = Label(country_frame, image=flag_photo, bg=globals.background_color)
			flag_label.image = flag_photo  # Keep reference to avoid garbage collection
			flag_label.pack(side="right")

	def on_key_release(event):
		if (input_field.get() == ""):
			add_placeholder()
		update_matching_countries()

	# Bind key release to update matching countries
	input_field.bind("<KeyRelease>", on_key_release)

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
