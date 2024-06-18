import cv2
import numpy as np
from utils import reconstruction

def item6(a_image, e_image):
    # Crear una máscara que contenga los bordes de la imagen
    border_mask = np.zeros_like(a_image, dtype=np.uint8)
    border_mask[0, :] = a_image[0, :]
    border_mask[-1, :] = a_image[-1, :]
    border_mask[:, 0] = a_image[:, 0]
    border_mask[:, -1] = a_image[:, -1]

    # Calculamos la inversa de los agujeros
    not_e_image = cv2.bitwise_not(e_image)

    # Calculamos la inversa de las células, rellenadas
    a_background = reconstruction(a_image, border_mask, debug=False)
    not_a_background = cv2.bitwise_not(a_background)

    # Usamos los núcleos, para reconstruir las células rellenadas.
    # Como las células de tipo 1, 2 y3 no tienen núcleos, vamos a quedarnos solo con tipo 4.
    f_background = reconstruction(not_a_background, not_e_image, debug=False)

    # Volvemos a agregar los agujeros a las células rellenadas
    not_f_image = cv2.bitwise_and(f_background, cv2.bitwise_not(a_image))

    # Invertimos la imagen para obtener el resultado final, ya que hasta ahora trabajamos con la inversa.
    f_image = cv2.bitwise_not(not_f_image)

    return f_image