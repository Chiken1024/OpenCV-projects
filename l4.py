import cv2 as cv
import numpy as np


def highlight_circles(src: cv.Mat, duration: int) -> None:
  mat: cv.Mat = src
  
  detected_circles: cv.Mat = cv.HoughCircles(
    cv.blur(cv.cvtColor(mat, cv.COLOR_BGR2GRAY), (3, 3)),
    cv.HOUGH_GRADIENT, 1, 20,
    param1=50, param2=30, minRadius=1, maxRadius=40
  )

  if detected_circles is not None:
    for pt in np.uint16(np.around(detected_circles))[0, :]:
      cv.circle(mat, (pt[0], pt[1]), pt[2], (0, 0, 255), 2)
    cv.imshow("Highlighted Circles", mat)
    cv.waitKey(duration)
    cv.destroyAllWindows()


image: cv.Mat = cv.imread("../L4/eyes.jpg")

highlight_circles(image, 0)