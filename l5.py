import os
import cv2 as cv
from PIL import Image
from PIL.ImageFile import ImageFile


IMAGES_PATH: str = "../OpenCV/L5/Images"


avg_width, avg_height = 0, 0
files: list[str] = os.listdir(IMAGES_PATH)


for file in files:
  image: ImageFile = Image.open(os.path.join(IMAGES_PATH, file))
  avg_width += image.width
  avg_height += image.height


avg_width, avg_height = avg_width // len(files), avg_height // len(files)


for file in files:
  if file.endswith(".jpg") or file.endswith(".png"):
    image = Image.open(os.path.join(IMAGES_PATH, file)).resize((avg_width, avg_height))
    image.save(file, "PNG", quality=95)
    print(file, " is resized!")


def generate_video() -> cv.VideoCapture: ...