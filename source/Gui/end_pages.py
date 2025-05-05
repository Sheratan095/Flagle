from tkinter import Toplevel, Label, Button
import globals
from screeninfo import get_monitors

def show_result_screen(canvas_master, message: str, input_manager):
	"""Display the win/lose screen."""
	result_window = Toplevel(canvas_master)

	window_width = 300
	window_height = 200

	result_window.title("Game Over")
	result_window.configure(bg=globals.background_color)
	result_window.resizable(False, False)

	# Disable the red cross (close button)
	result_window.protocol("WM_DELETE_WINDOW", lambda: None)

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
	result_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

	# Display the result message
	Label(
		result_window,
		text=message,
		font=("Arial", 16, "bold"),
		fg=globals.input_color,
		bg=globals.background_color
	).pack(pady=20)

	# Add a restart button
	Button(
		result_window,
		text="Restart",
		font=("Arial", 12),
		command=lambda: [_restart_game()],
		bg=globals.input_color,
		fg=globals.background_color
	).pack(pady=10)

	# Add a quit button
	Button(
		result_window,
		text="Quit",
		font=("Arial", 12),
		command=result_window.quit,
		bg=globals.input_color,
		fg=globals.background_color
	).pack(pady=10)

	def _restart_game():
		result_window.withdraw()  # Hide the end window
		globals.game.start_game(globals.mode)
		input_manager.start_game()