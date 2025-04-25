from globals import *
from GuessResult import GuessResult
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QImage
import sys
import io

# Start the game
game.start_game(mode)

# Make a guess
result: GuessResult = game.guess("Germany")
result: GuessResult = game.guess("Italy")

# Convert PIL image to QPixmap
def pil_to_qpixmap(pil_image):
	buffer = io.BytesIO()
	pil_image.save(buffer, format="PNG")
	qimage = QImage.fromData(buffer.getvalue())
	return (QPixmap.fromImage(qimage))

# Create Qt Application
app = QApplication(sys.argv)
label = QLabel()
pixmap = pil_to_qpixmap(result.result_image)
label.setPixmap(pixmap)
label.show()

sys.exit(app.exec_())
