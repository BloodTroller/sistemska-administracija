import cv2
import numpy as np

def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj):

    roi = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    min_loc = np.unravel_index(np.argmin(gray_roi), gray_roi.shape)
    max_loc = np.unravel_index(np.argmax(gray_roi), gray_roi.shape)

    min_value_color = np.array(roi[min_loc[0], min_loc[1]])
    max_value_color = np.array(roi[max_loc[0], max_loc[1]])

    return min_value_color, max_value_color
    pass

def zmanjsaj_sliko(slika, sirina, visina):
    slika = cv2.resize(slika, (sirina, visina))
    return slika


def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze):
    visina, sirina = slika.shape[:2]

    korak_x = sirina_skatle
    korak_y = visina_skatle

    boxes = []

    for y in range(0, visina - visina_skatle, korak_y):
        for x in range(0, sirina - sirina_skatle, korak_x):

            skatla = slika[y:y + visina_skatle, x:x + sirina_skatle]

            piksli_koze = prestej_piksle_z_barvo_koze(skatla, barva_koze)

            # če je 50%+ kože
            if piksli_koze / (sirina_skatle * visina_skatle) > 0.5:
                boxes.append((x, y, x + sirina_skatle, y + visina_skatle))
    return boxes

def prestej_piksle_z_barvo_koze(slika, barva_koze):
    brown_min = barva_koze[0]
    brown_max = barva_koze[1]
    rang = cv2.inRange(slika, brown_min, brown_max)
    return cv2.countNonZero(rang)