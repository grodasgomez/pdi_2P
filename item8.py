import cv2
import numpy as np
from utils import reconstruction
from item5 import item5
from item6 import item6

def item8(g_image, n_iter=2):
    kernel = [[1,1,1],[1,1,1],[1,1,1]]
    kernel = np.array(kernel, dtype=np.uint8)
    not_g_image = cv2.bitwise_not(g_image)
    apertura = cv2.erode(cv2.dilate(not_g_image, kernel, iterations=n_iter), kernel, iterations=n_iter)
    cierre = cv2.dilate(cv2.erode(not_g_image, kernel, iterations=n_iter), kernel, iterations=n_iter)
    cierre_apertura = cv2.dilate(cv2.erode(apertura, kernel, iterations=n_iter), kernel, iterations=n_iter)
    erode = cv2.dilate(not_g_image, kernel, iterations=n_iter)

    # future_loose_nuclei = item5(eroded)
    # future_type4 = item6(g_image, future_loose_nuclei)
    
    # tipo2 = cv2.bitwise_xor(g_image, future_type4)
    # cv2.imshow('Tipo2', tipo2)
    # cv2.imshow('Tipo4', future_type4)
    # cv2.imshow('Loose nuclei', future_loose_nuclei)
    cv2.imshow('g image', not_g_image)
    cv2.imshow('apertura', apertura)
    cv2.imshow('cierre', cierre)
    cv2.imshow('cierre_apertura', cierre_apertura)
    cv2.imshow('erode', erode)
    cv2.waitKey(0)

    return 