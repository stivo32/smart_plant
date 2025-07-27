from picamera2 import Picamera2
from time import sleep
import datetime
import pathlib

from app.config import PHOTO_STORAGE_PATH
from app.storage.action_logger import log_action


class CameraService:
    def __init__(self):
        self.picam2 = Picamera2()
        self.config = self.picam2.create_still_configuration(main={"size": (4056, 3040)})
        self.picam2.configure(self.config)

    @log_action
    def capture_image(self) -> None:
        now = datetime.datetime.now()
        filename = f"photo_{now.strftime('%Y%m%d_%H%M%S')}.jpg"
        self.picam2.start()
        sleep(2)  # Дать камере время для настройки
        output = pathlib.Path(PHOTO_STORAGE_PATH) / filename
        self.picam2.capture_file(output)

    def __del__(self):
        self.picam2.close()


def capture_image():
    camera_service = CameraService()
    print("Capturing image...")
    camera_service.capture_image()
    print("Image captured successfully.")


if __name__ == "__main__":
    camera_service = CameraService()
    try:
        camera_service.capture_image()  # Capture an image
    except Exception as e:
        print(f"An error occurred: {e}")
