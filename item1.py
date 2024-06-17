import cv2
import numpy as np
from utils import reconstruction


def item1(image):

    # Asegurarse de que la imagen sea binaria
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    inverted_image = cv2.bitwise_not(binary_image)

    # Crear una máscara que contenga los bordes de la imagen
    border_mask = np.zeros_like(binary_image, dtype=np.uint8)
    border_mask[0, :] = binary_image[0, :]
    border_mask[-1, :] = binary_image[-1, :]
    border_mask[:, 0] = binary_image[:, 0]
    border_mask[:, -1] = binary_image[:, -1]

    # Inicializar el marcador para la reconstrucción
    marker = border_mask.copy()

    # Realizar la reconstrucción
    reconstructed_image = reconstruction(inverted_image, marker)


    result = cv2.bitwise_xor(binary_image, reconstructed_image)

    return result