import pytesseract
from PIL.Image import Image
import screen_grabber

class TextScanner:
    def get_text_from_image(self, image: Image):
        print(pytesseract.image_to_string(image))

if __name__ == "__main__":
    scanner = TextScanner()
    scanner.get_text_from_image()
    screenGrabber = ScreenGrabber()