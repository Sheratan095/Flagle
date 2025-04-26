from globals import *
from GuessResult import GuessResult
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image

import sys
import io

# Start the game
game.start_game(mode)

# Convert PIL image to QPixmap
def pil_to_qpixmap(pil_image):
	buffer = io.BytesIO()
	pil_image.save(buffer, format="PNG")
	qimage = QImage.fromData(buffer.getvalue())
	return (QPixmap.fromImage(qimage))

# Create Qt Application
app = QApplication(sys.argv)
label = QLabel()

# Set the background color of the main window
label.setStyleSheet("background-color: black;")

while True:
    user_input = input("Enter your guess (type 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting the game.")
        break

    # Make a guess
    result: GuessResult = game.guess(user_input)

    # Update the image
    pixmap = pil_to_qpixmap(result.result_image)
    label.setPixmap(pixmap)
    label.show()
    app.processEvents()  # Process Qt events to update the GUI

