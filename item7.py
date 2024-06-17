import cv2
import numpy as np
from utils import reconstruction

def item7(a_image, tipo1_image, tipo4_image):
    g_image = cv2.bitwise_xor(cv2.bitwise_xor(a_image, tipo1_image), tipo4_image)

    return g_image