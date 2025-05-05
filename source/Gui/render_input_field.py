from tkinter import Entry, Button, Frame, Label, Canvas, Scrollbar
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
		insertbackground=globals.input_color,
		font=("Arial", 10, "bold")
	)
	input_manager.set_input_field(input_field)

	input_field.place(
		x=input_x,
		y=input_y,
		width=input_width,
		height=input_height
	)

	# Placeholder functionality
	def add_placeholder(event=None):
		if input_field.get() == "":
			input_field.insert(0, placeholder_text)
			input_field.config(fg=globals.txtbox_placeholder_color)
			input_field.icursor(0)

	def on_focus_out(event):
		add_placeholder()

	def on_key_press(event):
		if input_field.get() == placeholder_text:
			input_field.delete(0, 'end')
			input_field.config(fg=globals.input_color)

	input_field.bind("<FocusOut>", on_focus_out)
	input_field.bind("<Key>", on_key_press)
	add_placeholder()
	input_field.focus_set()

	# Create a canvas + scrollbar + frame for matching countries
	matching_canvas = Canvas(bg=globals.background_color, highlightthickness=0)
	scrollbar = Scrollbar(orient="vertical", command=matching_canvas.yview, bg=globals.background_color)
	matching_frame = Frame(matching_canvas, bg=globals.background_color)

	# Configure scrolling
	matching_frame.bind("<Configure>", lambda e: matching_canvas.configure(scrollregion=matching_canvas.bbox("all")))
	matching_canvas.create_window((0, 0), window=matching_frame, anchor="nw")
	matching_canvas.configure(yscrollcommand=scrollbar.set)

	# Mouse wheel support
	def _on_mousewheel(event):
		matching_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

	matching_canvas.bind_all("<MouseWheel>", _on_mousewheel)

	def update_matching_countries():
		# Clear previous content
		for widget in matching_frame.winfo_children():
			widget.destroy()

		matching_countries: list[Country] = globals.game.get_matching_countries(input_field.get())

		if matching_countries:
			max_visible = 10  # Maximum number of countries to display
			visible_count = min(len(matching_countries), max_visible)
			frame_height = visible_count * 30  # Each country row is 30px high

			matching_canvas.place(x=input_x, y=input_y - frame_height, width=220, height=frame_height)
			scrollbar.place(x=input_x + 220, y=input_y - frame_height, width=20, height=frame_height)
		else:
			matching_canvas.place_forget()
			scrollbar.place_forget()

		for index, country in enumerate(matching_countries):
			country_frame = Frame(matching_frame, bg=globals.background_color, height=24)
			country_frame.pack(fill="x", pady=1)

			def on_country_click(event, selected_country=country):
				input_field.delete(0, 'end')
				input_field.insert(0, selected_country.name)
				matching_canvas.place_forget()
				scrollbar.place_forget()

			name_label = Label(
				country_frame,
				text=globals.get_fixed_country_name(country.name, 30),
				fg=globals.input_color,
				bg=globals.background_color,
				anchor="w",
				font=("Arial", 10),
				width=22  # Set a fixed width for the label
			)
			name_label.pack(side="left")

			flag_image = Image.open(country.get_flag()).resize((32, 24))
			flag_photo = ImageTk.PhotoImage(flag_image)
			flag_label = Label(country_frame, image=flag_photo, bg=globals.background_color)
			flag_label.image = flag_photo
			flag_label.pack(side="right", padx=2)

			# Bind clicks
			country_frame.bind("<Button-1>", on_country_click)
			name_label.bind("<Button-1>", on_country_click)
			flag_label.bind("<Button-1>", on_country_click)

	def on_key_release(event):
		if input_field.cget("state") == "disabled":
			return
		if input_field.get() == "":
			add_placeholder()
		update_matching_countries()

	input_field.bind("<KeyRelease>", on_key_release)

	# Submit Button
	image = Image.open("assets/btn.png")
	button_image_1 = ImageTk.PhotoImage(image.resize((24, 24)))
	button_1 = Button(
		image=button_image_1,
		borderwidth=0,
		bg=globals.background_color,
		activebackground=globals.background_color,
		highlightthickness=0,
		command=lambda: [
			matching_canvas.place_forget(),
			scrollbar.place_forget(),
			on_button_click(input_field, input_manager) if input_field.cget("state") != "disabled" else None
		],
		relief="flat"
	)

	button_1.image = button_image_1
	button_1.place(
		x=235.0,
		y=606.0,
		width=29.0,
		height=29.0
	)

	# Enter key triggers submission
	input_field.bind("<Return>", lambda event: [matching_canvas.place_forget(), scrollbar.place_forget(), on_button_click(input_field, input_manager)])

	return input_field
