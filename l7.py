import os
import cv2 as cv


PATH: str = "L7/"

MAX_SAMPLES: int = 10


images_path: str = PATH + "images"
if os.path.exists(images_path): os.makedirs(images_path)

user_id: str = input("Enter user ID: ")

face_cascade: cv.CascadeClassifier = cv.CascadeClassifier(
  cv.data.haarcascades + (PATH + "haarcascade_frontalface_default.xml")
)


capture: cv.VideoCapture = cv.VideoCapture(0, cv.CAP_DSHOW)

samples: int = 0

print("Starting face detection. Look into the camera.")

while True:
  value, frame = capture.read()
  if not value: break

  gray: cv.Mat = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  for (x, y, w, h) in face_cascade.detectMultiScale(gray, 1.3, 5):
    samples += 1

    image: cv.Mat = gray[y:y + h, x:x + w]
    file_name: str = os.path.join(images_path, f"{user_id}_{samples}.jpg")
    cv.imwrite(file_name, image)

    cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
    cv.putText(
      frame, f"Samples: {samples}/{MAX_SAMPLES}", (10, 30),
      cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 3
    )
    cv.imshow("Face Data Collection", frame)
  
  if samples >= MAX_SAMPLES:
    print("Data collection completed!")
    break

  if cv.waitKey(1) & 0xFF == ord('q'): break


capture.release()
cv.destroyAllWindows()