import cv2 as cv
import numpy as np

## SHOW IMAGE
# img = cv.imread("Sources/still_image.jpg")
## default cvtcolor = bgr
# img = cv.resize(img, (220, 340))
## resize to desired
#
# cv.imshow("frame", img)
#
# cv.waitKey(0)

## CAMERA CAPTURE
# cam = cv.VideoCapture(0)
#
# while True:
#     ret, frame = cam.read()
#     frame = cv.flip(frame, 1)
#
#     cv.imshow("Camera (press Q to close)", frame)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cam.release()

## SHOW VIDEO
vid = cv.VideoCapture("Sources/little_movement.mp4")
# ms between frames info; https://fpstoms.com
frameTime = 40

while True:
    check, frame = vid.read()

    if check:
        cv.imshow("cam_frame", frame)
        cv.setWindowTitle("cam_frame", "Camera (press Q to close)")

    if cv.waitKey(1) == ord('q') & cv.waitKey(frameTime):
        break

#release camera
vid.release()

#end cv2
cv.destroyAllWindows()