import cv2 as cv
import numpy as np

## SHOW VIDEO
vid = cv.VideoCapture("Sources/little_movement.mp4")
cv.namedWindow("cam_frame")
# ms between frames info; https://fpstoms.com
frameTime = 40

while True and cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) >= 1:
    check, frame = vid.read()

    if check:
        cv.imshow("cam_frame", frame)
        cv.setWindowTitle("cam_frame", "Camera (press Q to close)")
    else:
        print("Video ended")
        play = False
        break

    if cv.waitKey(frameTime) == ord('q') or cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) < 1:
        break

#release camera
vid.release()

#end cv2
cv.destroyAllWindows()