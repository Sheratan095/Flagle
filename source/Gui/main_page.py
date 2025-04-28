from tkinter import Tk, Canvas
from screeninfo import get_monitors
import Gui.render_geometry as geometry
import globals
from Gui.InputManager import InputManager
from Gui.render_txtboxes import render_inputs
from Gui.render_input_field import render_input_field
from Gui.events import handle_esc, handle_enter
from Gui.message_label import MessageLabel  # Import the MessageLabel class

window = Tk()

# Set window dimensions
window_width = 300
window_height = 700

# Get the dimensions of the primary monitor
primary_monitor = get_monitors()[0]
screen_width = primary_monitor.width
screen_height = primary_monitor.height

# Calculate position to center the window on the primary monitor
x_position = max(0, (screen_width // 2) - (window_width // 2))
y_position = max(0, (screen_height // 2) - (window_height // 2))

# Set the geometry of the window
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
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
