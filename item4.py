import cv2
import numpy as np
from utils import reconstruction

def item4(a_image, c_image):
    # Imagen a representa todas las células e imagen c representa las células de tipo 2, 3 y 4
    # Con xor, obtenemos las células de tipo 1
    not_d_image = cv2.bitwise_xor(a_image, c_image)

    # La imagen que nos resulta va tener las células pintadas de blanco, por lo cuál la invertimos
    d_image = cv2.bitwise_not(not_d_image)

    return d_image