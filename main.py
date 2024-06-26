import time

import cv2 as cv
import numpy as np
import functions as f


def tocke_slike(event, x, y, flags, params):
    global pframe
    if event == cv.EVENT_LBUTTONUP:
        pframe = frame.copy()
        if len(cord) == 2:
            cord.clear()
            displaystring = "Camera (press ENTER to confirm selection - 2 corners)"
            cv.setWindowTitle("cam_frame", "Camera (press ENTER to confirm selection - 2 corners)")
            print(displaystring)
        else:
            if len(cord) == 0:
                cord.append([x, y])
                displaystring = "Camera (press ENTER to confirm selection - 2 corners [(" + str(cord[0][0]) + "," + str(
                    cord[0][1]) + "), Y ])"
                cv.setWindowTitle("cam_frame", displaystring)
                print(displaystring)
            if cord[0] != [x, y] and len(cord) == 1:
                cord.append([x, y])
                polepsaj_tocke()

            if len(cord) == 2:
                a1, b1 = cord[0]
                a2, b2 = cord[1]
                for index in range(a1, a2):
                    pframe[b1, index] = [255 - frame[b1, index, 0], 255 - frame[b1, index, 1],
                                         255 - frame[b1, index, 2]]
                    pframe[b2, index] = [255 - frame[b2, index, 0], 255 - frame[b2, index, 1],
                                         255 - frame[b2, index, 2]]

                for ind in range(b1, b2):
                    pframe[ind, a1] = [255 - frame[ind, a1, 0], 255 - frame[ind, a1, 1], 255 - frame[ind, a1, 2]]
                    pframe[ind, a2] = [255 - frame[ind, a2, 0], 255 - frame[ind, a2, 1], 255 - frame[ind, a2, 2]]

                displaystring = "Camera (press ENTER to confirm selection - 2 corners [(" + str(cord[0][0]) + "," + str(
                    cord[0][1]) + "), (" + str(cord[1][0]) + "," + str(cord[1][1]) + ")])"
                cv.setWindowTitle("cam_frame", displaystring)
                print(displaystring)

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
vid = cv.VideoCapture(0)
cv.namedWindow("cam_frame")
cv.setMouseCallback("cam_frame", tocke_slike)
# ms between frames info; https://fpstoms.com
waitForSelection = True
play = True
cord = []
cv.setWindowTitle("cam_frame", "Camera (press Q to close)")
print("Camera (press Q to close)")
abc = True
displayFont = cv.FONT_HERSHEY_DUPLEX
prev_frame_time = 0
new_frame_time = 0

while play and cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) >= 1:
    check, fr = vid.read()
    frame = fr
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = str(int(fps))
    frame = cv.flip(frame, 1)
    cv.putText(frame, fps, (7, 70), displayFont, 2, (0, 0, 255), 5, cv.LINE_AA)

    if not check:
        print("Video ended")
        play = False
        break
    elif check and waitForSelection:
        # VELIKOST SLIKE
        # frame = f.zmanjsaj_sliko(frame, 340, 220)
        # frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if abc:
            # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow("cam_frame", frame)
            abc = False
    else:
        # print(f.prestej_piksle_z_barvo_koze(frame, barva_koze))
        squares = f.obdelaj_sliko_s_skatlami(frame, 5, 5, barva_koze)
        # print(squares)
        for i in range(len(squares)):
            cv.rectangle(frame, (squares[i][0], squares[i][1]), (squares[i][2], squares[i][3]), (100, 100, 100), 1)
        cv.imshow("cam_frame", frame)

    if cv.waitKey(1) == ord('q') or cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) < 1:
        play = False
        break

    while waitForSelection:
        pframe = frame.copy()
        cv.setWindowTitle("cam_frame", "Camera (press ENTER to confirm selection - 2 corners)")
        print("Camera (press ENTER to confirm selection - 2 corners)")
        k = cv.waitKey(-1)
        if k == ord(chr(13)) and len(cord) == 2:
            waitForSelection = False
            cv.setMouseCallback("cam_frame", lambda *args: None)
            barva_koze_min, barva_koze_max = f.doloci_barvo_koze(frame, cord[0], cord[1])
            print("Min: " + str(barva_koze_min) + " Max: " + str(barva_koze_max))
            barva_koze = np.array([barva_koze_min, barva_koze_max])
            cv.setWindowTitle("cam_frame", "Camera")
        if k == ord('q') or cv.getWindowProperty("cam_frame", cv.WND_PROP_VISIBLE) < 1:
            play = False
            waitForSelection = False
            cv.setWindowTitle("cam_frame", "Camera (press Q to close)")
            print("Camera (press Q to close)")
            break

# release camera
vid.release()

# end cv2
cv.destroyAllWindows()
