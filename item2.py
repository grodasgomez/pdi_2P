import cv2
import numpy as np
from utils import reconstruction

def item2(a_image):
    # Crear una máscara que contenga los bordes de la imagen
    border_mask = np.zeros_like(a_image, dtype=np.uint8)
    border_mask[0, :] = a_image[0, :]
    border_mask[-1, :] = a_image[-1, :]
    border_mask[:, 0] = a_image[:, 0]
    border_mask[:, -1] = a_image[:, -1]

    # Realizar la reconstrucción
    reconstructed_image = reconstruction(a_image, border_mask, debug=False)

    not_b_image = cv2.bitwise_xor(a_image, reconstructed_image)
    b_image = cv2.bitwise_not(not_b_image)
    
    return b_image