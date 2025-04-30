from tkinter import Toplevel, Label, Button
import globals

def show_result_screen(canvas_master, message: str, restart_callback):
    """Display the win/lose screen."""
    result_window = Toplevel(canvas_master)
    result_window.title("Game Over")
    result_window.geometry("300x200")
    result_window.configure(bg=globals.background_color)
    result_window.resizable(False, False)

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
        command=lambda: [restart_callback(), result_window.destroy()],
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
