from .. import functions as f
import cv2 as cv
def test_prestej_piksle_z_barvo_koze():
    pic = cv.imread("face.png")
    assert f.prestej_piksle_z_barvo_koze(pic, [(176, 228, 239),(176, 228, 239)]) == 8418

def test_zmanjsaj_sliko():
    pic = cv.imread("face.png")
    assert f.zmanjsaj_sliko(pic, 200, 100) == cv.resize(pic, (200, 100))

def test_doloci_barvo_koze():
    pic = cv.imread("face.png")
    assert f.doloci_barvo_koze(pic,[0, 0], [pic.shape[0]-1, pic.shape[1]-1]) == ((176, 228, 239), (87, 122, 185))