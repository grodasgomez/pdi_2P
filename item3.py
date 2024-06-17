import cv2
import numpy as np
from utils import reconstruction

def item3(a_image, b_image):
    # Crear una máscara que contenga los bordes de la imagen
    border_mask = np.zeros_like(a_image, dtype=np.uint8)
    border_mask[0, :] = a_image[0, :]
    border_mask[-1, :] = a_image[-1, :]
    border_mask[:, 0] = a_image[:, 0]
    border_mask[:, -1] = a_image[:, -1]

    # Realizar la reconstrucción
    a_background = reconstruction(a_image, border_mask, debug=False)
    b_background = reconstruction(b_image, border_mask, debug=False)

    cv2.imshow('a_background', a_background)
    cv2.imshow('b_background', b_background)

    not_c_image = cv2.bitwise_xor(a_background, b_background)
    c_image = cv2.bitwise_not(not_c_image)

    cv2.imwrite('C.png', c_image)

    return c_image