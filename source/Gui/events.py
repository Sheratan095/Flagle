from Gui.InputManager import InputManager
from tkinter import Entry

# Define the function to handle the Esc key globally
def handle_esc(event, window):
	window.destroy()  # Close the application when Esc is pressed

# Define the function to handle the Enter key globally
def handle_enter(event, input_field: Entry, input_manager: InputManager):
	on_button_click(input_field, input_manager)  # Trigger the guess logic

def on_button_click(input_field: Entry, input_manager: InputManager):

	if (input_field.get() == ""):
		return

	input_manager.guess(input_field.get())
	input_field.delete(0, 'end')  # Clear the input field
	input_field.focus_set()  # Refocus the input field