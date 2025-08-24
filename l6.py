import os
import numpy as np
import time
import cv2 as cv

PATH: str = "./L6/"

video: cv.VideoCapture = cv.VideoCapture(PATH + "video.mp4")

time.sleep(1)

background: cv.Mat
for i in range(60):
  value, background = video.read()
  if value: break
background = np.flip(background, axis=1)

image: cv.Mat

count: int = 0
while video.isOpened():
  value, image = video.read()
  if not value: break

  count += 1

  image: cv.Mat = np.flip(image, axis = 1)
  image_hsv: cv.Mat = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  mask1: cv.Mat = cv.dilate(
    cv.morphologyEx(
      cv.inRange(image_hsv, (255, 40, 40), (255, 255, 255)) +
      cv.inRange(image_hsv, (155, 40, 40), (180, 255, 255)),
      np.ones((3, 3), np.uint8), iterations=2
    ),
    np.ones((3, 3), np.uint8), iterations=1
  )
  mask2: cv.Mat = cv.bitwise_not(mask1)

  output: cv.Mat = cv.addWeighted(
    cv.bitwise_and(background, background, mask=mask1), 1,
    cv.bitwise_and(image, image, mask=mask2), 1, 0
  )

  cv.imshow("Invisibility Cloak", output)

  k: int = cv.waitKey(10)
  if k == 27: break