import cv2 as cv


def draw(src: cv.Mat, func, args: list) -> None:
  return func(src, *args)

def batch_draw(src: cv.Mat, func_args: list) -> None:
  mat: cv.Mat = src
  for func_arg in func_args: mat = func_arg[0](mat, *func_arg[1:])

  return mat


class Main:
  def __init__(self, **args) -> None: self.path: str = args["path"]

  def run(self) -> None:
    image: cv.Mat = cv.imread(f"{self.path}pikachu.png")

    image = batch_draw(image, [
      [
        cv.rectangle,
        (0, 0),
        (i * 2, i * 2),
        (i, 255 - i, i // 2),
        1
      ] for i in range(50)
    ] + [
      [
        cv.putText,
        "Hello World!",
        (20, 50),
        cv.FONT_ITALIC,
        1,
        (0, 0, 0),
        3
      ]
    ])

    cv.imshow("Pikachu", image)
    cv.waitKey(5000)
    
    cv.destroyAllWindows()


if __name__ == "__main__": Main(path="L3/").run()