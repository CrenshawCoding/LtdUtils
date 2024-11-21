import mss
from mss.screenshot import ScreenShot
from PIL import Image

class ScreenGrabber:

    def screenshot(self) -> ScreenShot:
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {"top": 487, "left": 626, "width": 270, "height": 274}
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            print(f"Screenshot taken: {output}")
            return sct.grab(monitor)

            # Save to the picture file
            # mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def get_image_from_screenshot(self, screenshot: ScreenShot) -> Image.Image:
        return Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")


if __name__ == "__main__":
    screenGrabber = ScreenGrabber()
    screenGrabber.screenshot()
