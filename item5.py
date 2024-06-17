import cv2
import numpy as np
from utils import reconstruction
from item2 import item2

def item5(c_image):
    # Generamos otra vez los agujeros de las células
    cytoplasm_without_nuclei = item2(c_image)

    # Los "nuevos agujeros" en los agujeros son los núcleos
    e_image = item2(cytoplasm_without_nuclei)

    return e_image