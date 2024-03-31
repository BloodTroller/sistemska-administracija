import cv2
import numpy as np


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj):
    x1, y1 = levo_zgoraj
    x2, y2 = desno_spodaj
    izbira = slika[y1:y2, x1:x2]
    b = np.mean(izbira[:, :, 0])
    g = np.mean(izbira[:, :, 1])
    r = np.mean(izbira[:, :, 2])
    return [b, g, r]
def zmanjsaj_sliko(slika,sirina,visina):
    pass

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle,barva_koze):
    pass

def prestej_piksle_z_barvo_koze(slika, barva_koze):
    pass