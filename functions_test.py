import cv2 as cv
import numpy as np
import functions as f


def test_prestej_piksle_z_barvo_koze():
    pic = cv.imread("Sources/face.png")
    assert f.prestej_piksle_z_barvo_koze(pic, [(176, 228, 239), (176, 228, 239)]) == 8418


def test_zmanjsaj_sliko():
    pic = cv.imread("Sources/face.png")
    assert np.array_equal(f.zmanjsaj_sliko(pic, 200, 100), cv.resize(pic, (200, 100)))


def test_doloci_barvo_koze():
    pic = cv.imread("Sources/face.png")
    assert np.array_equal(f.doloci_barvo_koze(pic, [0, 0], [pic.shape[0] - 1, pic.shape[1] - 1]),
                          ([87, 122, 185], [176, 228, 239]))
