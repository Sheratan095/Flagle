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
		insertbackground=globals.input_color,  # Set the cursor color
		font=("Arial", 10, "bold")  # Set font to bold
	)
	input_manager.set_input_field(input_field) # Pass the input field to the InputManager

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

	input_field.bind("<FocusOut>", on_focus_out)
	input_field.bind("<Key>", on_key_press)  # Change text color on key press

	# Initialize with placeholder
	add_placeholder()

	input_field.focus_set()  # Set focus to the input field

	# Frame to display matching countries (placed completely above the input field)
	matching_frame = Frame(bg=globals.background_color)

	def update_matching_countries():
		# Clear the frame
		for widget in matching_frame.winfo_children():
			widget.destroy()
		
		matching_countries: list[Country] = globals.game.get_matching_countries(input_field.get())

		# Adjust the height dynamically based on the number of matching countries
		if len(matching_countries) > 0:
			# Start the frame slightly higher than the textbox and grow upward
			frame_height = len(matching_countries) * 30  # 30 because it works somehow
			matching_frame.place(x=input_x, y=input_y - frame_height, width=240, height=frame_height)
		else:
			# Hide the frame if no matching countries
			matching_frame.place_forget()

		# Add each country to the frame
		for index, country in enumerate(matching_countries):
			country_frame = Frame(matching_frame, bg=globals.background_color, height=24)
			country_frame.pack(fill="x", pady=2)  # Add padding except for the last entry

				# Define a click handler for the country
			def on_country_click(event, selected_country=country):
				input_field.delete(0, 'end')  # Clear the input field
				input_field.insert(0, selected_country.name)  # Set the selected country's name
				matching_frame.place_forget()  # Hide the matching frame

			# Display country name (aligned to the left)
			name_label = Label(
				country_frame,
				text=globals.get_fixed_country_name(country.name, 30),
				fg=globals.input_color,
				bg=globals.background_color,
				anchor="w",
				font=("Arial", 10),
			)
			name_label.pack(side="left")

			# Bind the click event to the country frame
			country_frame.bind("<Button-1>", on_country_click)
			name_label.bind("<Button-1>", on_country_click)  # Also bind to the label for better click detection

			# Load and display flag image (aligned to the right)
			flag_image = Image.open(country.get_flag()).resize((32, 24))  # Adjusted flag size
			flag_photo = ImageTk.PhotoImage(flag_image)
			flag_label = Label(country_frame, image=flag_photo, bg=globals.background_color)
			flag_label.image = flag_photo  # Keep reference to avoid garbage collection
			flag_label.pack(side="right", padx=2)

			flag_label.bind("<Button-1>", on_country_click)  # Also bind to the label for better click detection


	def on_key_release(event):
		# Check if the input field is disabled
		if (input_field.cget("state") == "disabled"):
			return  # Do nothing if the input field is disabled

		if input_field.get() == "":
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
		command=lambda: [
			matching_frame.place_forget(),
			# Check if the input field is not disabled before calling on_button_click
			# This prevents the button from being clickable when the game is over
			on_button_click(input_field, input_manager) if (input_field.cget("state") != "disabled") else None
		],
		relief="flat"
	)

	button_1.image = button_image_1  # Store reference to prevent garbage collection
	button_1.place(
		x=235.0,
		y=606.0,
		width=29.0,
		height=29.0
	)

	# Bind Enter key to hide matching frame and trigger button click
	input_field.bind("<Return>", lambda event: [matching_frame.place_forget(), on_button_click(input_field, input_manager)])

	return (input_field)
