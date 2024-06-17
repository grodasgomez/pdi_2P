import cv2
import numpy as np
from utils import reconstruction
from item5 import item5
from item6 import item6

def item8(g_image, n_iter=2):
    kernel = [[1,1,1],[1,1,1],[1,1,1]]
    kernel = np.array(kernel, dtype=np.uint8)
    not_g_image = cv2.bitwise_not(g_image)
    not_apertura = cv2.erode(cv2.dilate(not_g_image, kernel, iterations=n_iter), kernel, iterations=n_iter)
    not_cierre_apertura = cv2.dilate(cv2.erode(not_apertura, kernel, iterations=n_iter), kernel, iterations=n_iter)

    future_loose_nuclei = item5(not_cierre_apertura)
    type3 = item6(g_image, future_loose_nuclei)
    not_type2 = cv2.bitwise_xor(g_image, type3)
    type2 = cv2.bitwise_not(not_type2)

    return type2, type3