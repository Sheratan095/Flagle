from tkinter import Toplevel, Label, Button, CENTER
import globals

def show_result_screen(canvas_master, message: str, input_manager):
	"""Display the win/lose screen."""
	result_window = Toplevel(canvas_master)
	result_window.title("Game Over")
	result_window.geometry("300x200")
	result_window.configure(bg=globals.background_color)
	result_window.resizable(False, False)

	# Center the window on the screen
	result_window.update_idletasks()
	screen_width = result_window.winfo_screenwidth()
	screen_height = result_window.winfo_screenheight()
	window_width = 300
	window_height = 200
	x_cordinate = (screen_width // 2) - (window_width // 2)
	y_cordinate = (screen_height // 2) - (window_height // 2)
	result_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

	# Make the window non-movable
	result_window.overrideredirect(True)

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