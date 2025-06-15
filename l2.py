import cv2 as cv
import numpy as np

class Main:
  def __init__(self, path: str) -> None:
    self.path: str = path

  def run(self) -> None:
    img: cv.Mat = self.file_to_mat("pikachu.png")

    img = self.process_mat(img, [
      cv.erode(img, np.ones((3, 3), np.uint8)),
      cv.GaussianBlur(img, (7, 15), 0),
      cv.resize(img, (500, 100)),
      cv.copyMakeBorder(img, 5, 5, 5, 5, cv.BORDER_WRAP, img)
    ])

    cv.imshow("img", img)

    cv.waitKey(1000)
    cv.destroyAllWindows()
  
  def file_to_mat(self, path: str) -> cv.Mat:
    return cv.imread(self.path + path, 1)
  
  def process_mat(self, img: cv.Mat, functions: list) -> cv.Mat:
    for function in functions: img = function
    return img

if __name__ == "__main__":
  Main("L2/").run()