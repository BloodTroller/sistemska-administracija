import cv2 as cv
import numpy as np

img = cv.imread("Sources/still_image.jpg")
#default cvtcolor = bgr

img = cv.resize(img, (220, 340))
#resize to desired

cv.imshow("frame", img)

cv.waitKey(0)

cv.destroyAllWindows()
