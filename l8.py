import cv2 as cv
import os


PATH: str = "L8/"

VIDEO_SOURCE: str = PATH + "cars.mp4"
CASCADE_PATH: str = PATH + "cars.xml"


try:
  capture: cv.VideoCapture = cv.VideoCapture(VIDEO_SOURCE)
except:
  raise FileNotFoundError("Failed to load video")
  exit()


car_cascade: cv.CascadeClassifier = cv.CascadeClassifier(CASCADE_PATH)
if car_cascade.empty():
  raise ValueError("Failed to load cascade classifier")
  exit()


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
    cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
  
  cv.putText(
    frame, f"Cars detected: {len(cars)}", (10, 30),
    cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
  )

  cv.imshow("Car Detection", frame)

  if cv.waitKey(33) == 27: break


capture.release()
cv.destroyAllWindows()