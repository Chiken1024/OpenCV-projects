import cv2 as cv
import numpy as np


SCALE_FACTOR: float = 5.0
IMAGE_PATH: str = ""


"""
image: cv.Mat = cv.imread(IMAGE_PATH)
print(f"Dimensions: {image.shape}")

image = cv.resize(
  image, [image.shape[:2][::-1][i] * SCALE_FACTOR for i in range(2)]
)
split_image: list[cv.Mat] = cv.split(image)
for i, color in enumerate("RGB"):
  win_name: str = f"Image ({color})"
  cv.imshow(win_name, split_image[i])
  cv.moveWindow(win_name, 100, 100)

  if cv.waitKey(1000) == 27: break
  cv.destroyAllWindows()


image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

win_name: str = "RGB2BGR"
cv.imshow(win_name, image)
cv.moveWindow(win_name, 100, 100)

cv.waitKey(1000)
cv.destroyAllWindows()
"""

"""
image: cv.Mat = cv.imread(IMAGE_PATH)
image = cv.resize(
  image, [image.shape[:2][::-1][i] * SCALE_FACTOR for i in range(2)]
)
for i in range(3):
  erosion: int = i * 2 + 3
  
  win_name: str = f"Kernel size: {erosion}x{erosion}"
  cv.imshow(
    win_name, cv.erode(image, np.ones([erosion, erosion], np.uint8))
  )
  cv.moveWindow(win_name, 100, 100)

  if cv.waitKey(1000) == 27: break
  cv.destroyAllWindows()
"""