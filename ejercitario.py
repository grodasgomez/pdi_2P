import cv2
import numpy as np
from utils import reconstruction

def ej1(img):
    kernel = [[1,1,1],[1,1,1],[1,1,1]]
    kernel = np.array(kernel, dtype=np.uint8)
    n_iter = 3
    neg = cv2.bitwise_not(img)

    # Sacamos los circulos
    apertura = cv2.erode(cv2.dilate(img, kernel, iterations=n_iter), kernel, iterations=n_iter)

    # Agrandamos los circulos un poco para no dejar esquinas
    ero_apertura = cv2.erode(apertura, kernel, iterations=2)

    # Sacamos las lineas con los circulos borrados
    lines_with_holes = cv2.bitwise_and(neg, ero_apertura)

    kernel = [[0,0,0],[1,1,1],[0,0,0]]
    kernel = np.array(kernel, dtype=np.uint8)

    # Ahora vamos a agrandar las lineas, pero solo dejamos agrandar sobre los circulos o lineas
    lines = lines_with_holes
    for i in range(20):
        lines = cv2.dilate(lines, kernel, iterations=1)
        lines = cv2.bitwise_and(neg, lines)

    # Descomentar para debug
    # cv2.imshow('img', img)
    # cv2.imshow('apertura', apertura)
    # cv2.imshow('ero_apertura', ero_apertura)
    # cv2.imshow('lines', lines)
    # cv2.imshow('lines_with_holes', lines_with_holes)
    # cv2.waitKey(0)

    return cv2.bitwise_not(lines)


# main
image = cv2.imread('binbolin.jpg', cv2.IMREAD_GRAYSCALE)
neg = cv2.bitwise_not(image)

r1 = ej1(image)
cv2.imshow('image', image)
cv2.imshow('r1', r1)
cv2.waitKey(0)

