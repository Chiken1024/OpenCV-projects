import cv2 as cv


PATH: str = "L8/"

VIDEO_SOURCE: str = PATH + "cars.avi"
CASCADE_PATH: str = PATH + "cars.xml"

FPS: int = 30
SCALE_FACTOR: float = 1.5


try:
  open(VIDEO_SOURCE)
except:
  raise FileNotFoundError("Failed to locate video file")
  exit()
else:
  capture: cv.VideoCapture = cv.VideoCapture(VIDEO_SOURCE)

try:
  open(CASCADE_PATH)
except:
  raise FileNotFoundError("Failed to locate cascade file")
  exit()
else:
  car_cascade: cv.CascadeClassifier = cv.CascadeClassifier(CASCADE_PATH)
  if car_cascade.empty():
    raise ValueError("Failed to load cascade classifier")
    exit()


WAIT_DURATION: int = 1000 // FPS


while True:
  read, frame = capture.read()
  if not read:
    print("Failed to load next frame (end of video)")
    exit()

  frame_grayscale: cv.Mat = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  cars: list[list[int]] = car_cascade.detectMultiScale(
    frame_grayscale, scaleFactor=1.1, minNeighbors=1
  )

  for (x, y, w, h) in cars:
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

  if SCALE_FACTOR != 1.0:
    frame: cv.Mat = cv.resize(
      frame, [int(i * SCALE_FACTOR) for i in frame.shape[:2][::-1]], frame
    )

  cars_amount: int = len(cars)
  [
    cv.putText(
      frame, f"Cars detected: {cars_amount}", (10, 40 - i * 3),
      cv.FONT_HERSHEY_SIMPLEX, 1, (i * 255, i * 255, i * 255), 2
    ) for i in range(2)
  ]

  cv.imshow("Car Detection", frame)
  if cv.waitKey(WAIT_DURATION) == 27: break


capture.release()
cv.destroyAllWindows()