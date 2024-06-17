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

    # Calculamos la inversa de los agujeros
    not_b_image = cv2.bitwise_not(b_image)

    # Calculamos la inversa de las células, rellenadas
    not_a_background = cv2.bitwise_xor(a_image, b_image)

    # Usamos los agujeros, para reconstruir las células rellenadas.
    # Como las células de tipo 1 no tienen agujeros, vamos a quedarnos solo con tipo 2, 3 y 4.
    c_background = reconstruction(not_a_background, not_b_image, debug=False)

    # Volvemos a agregar los agujeros a las células rellenadas
    not_c_image = cv2.bitwise_and(c_background, b_image)

    # Invertimos la imagen para obtener el resultado final, ya que hasta ahora trabajamos con la inversa.
    c_image = cv2.bitwise_not(not_c_image)

    return c_image