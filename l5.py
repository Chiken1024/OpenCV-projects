import os
import cv2 as cv
from PIL import Image
from PIL.ImageFile import ImageFile


IMAGES: list[str] = os.listdir("./L5/Images")
edited_images: list[str] = os.listdir("./L5/Edited Images")


def generate_video(avg_width: int, avg_height: int) -> cv.VideoCapture:
  video: cv.VideoWriter = cv.VideoWriter(
    "./L5/video.avi", 0, 1, (avg_width, avg_height)
  )
  for image in edited_images:
    video.write(cv.imread(f"./L5/Edited Images/{image}"))
  return video


if len(edited_images) != len(IMAGES):
  for image in edited_images:
    os.remove(os.path.join("./L5/Edited Images", image))
  
  IMAGES_PATH: str = "./L5/Images"
  
  avg_width, avg_height = 0, 0

  for path in IMAGES:
    image: ImageFile = Image.open(os.path.join(IMAGES_PATH, path))
    avg_width += image.width
    avg_height += image.height

  avg_width, avg_height = avg_width // len(IMAGES), avg_height // len(IMAGES)

  for path in IMAGES:
    if path.endswith(".jpg") or path.endswith(".png"):
      image = Image.open(os.path.join(IMAGES_PATH, path)).resize(
        (avg_width, avg_height)
      )
      image.save(os.path.join("./L5/Edited Images", path), "PNG", quality=95)
  
  edited_images = os.listdir("./L5/Edited Images")
else:
  avg_width, avg_height = cv.imread(
    os.path.join("./L5/Edited Images", edited_images[0])
  ).shape[:2][::-1]


generate_video(avg_width, avg_height).release()