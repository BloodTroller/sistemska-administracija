import cv2
import cv2 as cv
import numpy as np
import functions as f

def tocke_slike(event, x, y, flags, params):
    global pframe
    if event == cv.EVENT_LBUTTONUP:
        if len(cord) == 0:
            cord.append([x, y])
            cv.setWindowTitle("cam_frame",
                              "Camera (press S to confirm selection - 2 corners [(" + str(cord[0][0]) + "," + str(
                                  cord[0][1]) + "), Y ])")
        elif cord[0] != [x, y]:
            cord.append([x, y])
            cv.setWindowTitle("cam_frame",
                              "Camera (press S to confirm selection - 2 corners [(" + str(cord[0][0]) + "," + str(
                                  cord[0][1]) + "), (" + str(cord[1][0]) + "," + str(cord[1][1]) + ")])")
            polepsaj_tocke()
            a1, b1 = cord[0]
            a2, b2 = cord[1]
            for index in range(a1, a2):
                pframe[b1, index] = [255 - frame[b1, index, 0], 255 - frame[b1, index, 1], 255 - frame[b1, index, 2]]
                pframe[b2, index] = [255 - frame[b2, index, 0], 255 - frame[b2, index, 1], 255 - frame[b2, index, 2]]

            for ind in range(b1, b2):
                pframe[ind, a1] = [255 - frame[ind, a1, 0], 255 - frame[ind, a1, 1], 255 - frame[ind, a1, 2]]
                pframe[ind, a2] = [255 - frame[ind, a2, 0], 255 - frame[ind, a2, 1], 255 - frame[ind, a2, 2]]

        if len(cord) > 2:
            cord.clear()
            pframe = frame.copy()
            cv.setWindowTitle("cam_frame", "Camera (press S to confirm selection - 2 corners)")

        for i in cord:
            xx, yy = i
            if yy > 1 and xx > 1:
                pframe[yy, xx] = [255 - frame[yy, xx, 0], 255 - frame[yy, xx, 1], 255 - frame[yy, xx, 2]]
                pframe[yy + 1, xx] = [0, 0, 0]
                pframe[yy + 1, xx + 1] = [0, 0, 0]
                pframe[yy, xx + 1] = [0, 0, 0]
                pframe[yy - 1, xx] = [0, 0, 0]
                pframe[yy - 1, xx - 1] = [0, 0, 0]
                pframe[yy, xx - 1] = [0, 0, 0]
                pframe[yy - 1, xx + 1] = [0, 0, 0]
                pframe[yy + 1, xx - 1] = [0, 0, 0]
            else:
                pframe[yy, xx] = [255 - frame[yy, xx, 0], 255 - frame[yy, xx, 1], 255 - frame[yy, xx, 2]]
        cv.imshow("cam_frame", pframe)


def polepsaj_tocke():
    x1, y1 = cord[0]
    x2, y2 = cord[1]
    temp_c0 = cord[0]
    temp_c1 = cord[1]
    if x2 > x1 and y2 > y1:
        # all good
        pass
    elif x2 > x1 and y2 < y1:
        cord[0][1] = y2
        cord[1][1] = y1
    elif x2 < x1 and y2 > y1:
        cord[0][0] = x2
        cord[1][0] = x1
    elif x2 < x1 and y2 < y1:
        cord[0] = temp_c1
        cord[1] = temp_c0


## SHOW VIDEO
vid = cv.VideoCapture("Sources/little_movement.mp4")
cv.namedWindow("cam_frame")
cv.setMouseCallback("cam_frame", tocke_slike)
# ms between frames info; https://fpstoms.com
frameTime = 40
waitForSelection = True
play = True
cord = []
barva_koze = -1
global frame, pframe

while play and cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) >= 1:
    check, frame = vid.read()
    if check:
        cv.imshow("cam_frame", frame)
        cv.setWindowTitle("cam_frame", "Camera (press Q to close)")
    else:
        print("Video ended")
        play = False
        break

    if cv.waitKey(frameTime) == ord('q'):
        play = False
        break

    while waitForSelection:
        pframe = frame.copy()
        cv.setWindowTitle("cam_frame", "Camera (press ENTER to confirm selection - 2 corners)")
        k = cv.waitKey(-1)
        if k == ord(chr(13)) and len(cord) == 2:
            waitForSelection = False
            cv.setMouseCallback("cam_frame", lambda *args: None)
            barva_koze = f.doloci_barvo_koze(frame, tuple(cord[0]), tuple(cord[1]))
            print(barva_koze)
        if k == ord('q') or cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) < 1:
            play = False
            waitForSelection = False
            break

# release camera
vid.release()

# end cv2
cv.destroyAllWindows()