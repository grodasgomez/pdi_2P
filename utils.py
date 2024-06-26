import cv2
import numpy as np

def reconstruction(mask, marker, debug=False):
    while True:
        if debug:
            cv2.imshow("Reconstruction", marker)
            cv2.waitKey(0)
        dilated_mark = cv2.dilate(marker, np.ones((3, 3), np.uint8))
        new_mark = cv2.bitwise_and(dilated_mark, mask)
        if np.array_equal(new_mark, marker):
            break
        marker = new_mark
    return marker