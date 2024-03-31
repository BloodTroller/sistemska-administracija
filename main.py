import cv2 as cv
import numpy as np
import functions as f

## SHOW VIDEO
vid = cv.VideoCapture("Sources/little_movement.mp4")
# ms between frames info; https://fpstoms.com
frameTime = 40

while True:
    check, frame = vid.read()

    if check & cv.waitKey(frameTime):
        cv.imshow("cam_frame", frame)
        cv.setWindowTitle("cam_frame", "Camera (press Q to close)")

    if cv.waitKey(1) == ord('q'):
        break



#release camera
vid.release()

#end cv2
cv.destroyAllWindows()