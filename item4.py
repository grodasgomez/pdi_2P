import cv2
import numpy as np
from utils import reconstruction

def item4(a_image, c_image):
    not_d_image = cv2.bitwise_xor(a_image, c_image)
    d_image = cv2.bitwise_not(not_d_image)

    cv2.imwrite('D.png', d_image)

    return d_image