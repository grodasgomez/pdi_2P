import cv2
import numpy as np
def item2(image, a_image):
    inverted_a_image = cv2.bitwise_not(a_image)
    cv2.imshow("inverted_a_image", inverted_a_image)