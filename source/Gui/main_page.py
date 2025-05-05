from tkinter import Tk, Canvas
from screeninfo import get_monitors
import Gui.render_geometry as geometry
import globals
from Gui.InputManager import InputManager
from Gui.render_txtboxes import render_inputs
from Gui.render_input_field import render_input_field
from Gui.events import handle_esc, handle_enter
from Gui.message_label import MessageLabel  # Import the MessageLabel class
from screeninfo import get_monitors
from tkinter import PhotoImage

window = Tk()

icon = PhotoImage(file="assets/icon.png")  # Use a .png
window.wm_iconphoto(True, icon)

# Set window dimensions
window_width = 300
window_height = 700

# Choose the monitor where you want the window (e.g., primary monitor)
monitor = get_monitors()[globals.main_screen_idx]  # You can change the index to target a different monitor

# Get monitor position and size
monitor_x = monitor.x
monitor_y = monitor.y
monitor_width = monitor.width
monitor_height = monitor.height

# Calculate centered window position
x = monitor_x + (monitor_width - window_width) // 2
y = monitor_y + (monitor_height - window_height) // 2

# Apply window geometry with position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# window.geometry(f"{window_width}x{window_height}")
window.configure(bg=globals.background_color)
window.title("Flagle")
window.resizable(False, False)

canvas = Canvas(
	window,
	bg=globals.background_color,
	height=window_height,
	width=window_width,
	bd=0,
	highlightthickness=0,
	relief="ridge"
)

canvas.place(x=0, y=0)

geometry.render_geometry(canvas)

# main image
main_image_idx: int = canvas.create_image(
	149.0,  # x
	109.0,  # y
	image=None
)

# Create a MessageLabel instance
message_label = MessageLabel(window)

input_manager = InputManager(main_image_idx, canvas, message_label)  # Pass the MessageLabel instance to InputManager
# Render input fields dynamically
render_inputs(canvas, input_manager)

# Render input field
input_field = render_input_field(input_manager)

# Bind the Esc key to the window
window.bind("<Escape>", lambda event: handle_esc(event, window))

# Bind the Enter key to the window
window.bind("<Return>", lambda event: handle_enter(event, input_field, input_manager))

canvas.create_text(
	90.0,
	666.0,
	anchor="nw",
	text="FLAGLE ",
	fill="#FFFFFF",
	font=("Inter Bold", 30 * -1)
)
