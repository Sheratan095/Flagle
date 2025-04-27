from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import Gui.render_geometry as geometry # Adjusted to use a relative import
import globals
from Gui.Input import Input
from Gui.InputManager import InputManager

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



#main image
# image_image_7 = PhotoImage(file="assets/image_7.png")
image_7 = canvas.create_image(
	149.0,
	109.0,
	image=None
)

input_manager = InputManager(image_7, canvas)


#inptut field
# entry_image_1 = PhotoImage(
#     file="assets/entry_1.png")
# entry_bg_1 = canvas.create_image(
#     121.5,
#     621.0,
#     image=entry_image_1
# )
input = Entry(
	bd=0,
	bg=globals.background_color,
	fg=globals.input_color,
	highlightthickness=0
)
input.place(
	x=32.0,
	y=606.0,
	width=179.0,
	height=28.0
)

def on_button_click():
	print("Button clicked")
	if (input.get() == ""):
		return
	input_manager.guess(input.get())

#BUTTON
from PIL import Image, ImageTk

image = Image.open("assets/btn.png")

button_image_1 =  ImageTk.PhotoImage(image.resize((24, 24)))
button_1 = Button(
	image=button_image_1,
	borderwidth=0,
	bg=globals.background_color,
	highlightthickness=0,
	command=lambda: on_button_click(),
	relief="flat"
)
#y: same of input
button_1.place(
	x=235.0,
	y=606.0,
	width=29.0,
	height=29.0
)

canvas.create_text(
	90.0,
	666.0,
	anchor="nw",
	text="FLAGLE ",
	fill="#FFFFFF",
	font=("Inter Bold", 30 * -1)
)



sixth_try:int = canvas.create_text(
	32.0,
	534.0,
	anchor="nw",
	text="Sixth try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# sixth_img = PhotoImage(file="assets/image_1.png")
sixth_img_idx = canvas.create_image(
	245.0,
	542.0,
	image=None
)



fifth_idx : int = canvas.create_text(
	32.0,
	473.0,
	anchor="nw",
	text="Fifth try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# FIFTH TRY
# fifth_img = PhotoImage(file="assets/image_2.png")
fifth_img_idx = canvas.create_image(
	245.0,
	481.0,
	image=None
)



fourth_idx = canvas.create_text(
	32.0,
	412.0,
	anchor="nw",
	text="Fourth try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# fourth_img = PhotoImage(file="assets/image_3.png")
fourth_img_idx = canvas.create_image(
	245.0,
	420.0,
	image=None
)


third_idx = canvas.create_text(
	32.0,
	351.0,
	anchor="nw",
	text="Third try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# third_img = PhotoImage(file="assets/image_4.png")
third_img_idx = canvas.create_image(
	245.0,
	359.0,
	image=None
)



second_idx : int = canvas.create_text(
	32.0,
	290.0,
	anchor="nw",
	text="Second try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# second_img = PhotoImage(file="assets/image_5.png")
second_img_idx = canvas.create_image(
	245.0,
	298.0,
	image=None
)



first_idx: int = canvas.create_text(
	31.0,
	229.0,
	anchor="nw",
	text="First try",
	fill=globals.border_color,
	font=("Inter Bold", 15 * -1)
)

# first_img= PhotoImage(file="assets/image_6.png")
first_img_idx = canvas.create_image(
	245.0,
	237.0,
	image=None
)


# Create Input objects and add them to InputManager
first_input = Input(canvas, first_idx, first_img_idx)
input_manager.add_input(first_input)

second_input = Input(canvas, second_idx, second_img_idx)
input_manager.add_input(second_input)

third_input = Input(canvas, third_idx, third_img_idx)
input_manager.add_input(third_input)

fourth_input = Input(canvas, fourth_idx, fourth_img_idx)
input_manager.add_input(fourth_input)

fifth_input = Input(canvas, fifth_idx, fifth_img_idx)
input_manager.add_input(fifth_input)

sixth_input = Input(canvas, sixth_try, sixth_img_idx)
input_manager.add_input(sixth_input)


