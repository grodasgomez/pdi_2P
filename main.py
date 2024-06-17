import cv2
from item1 import item1

image = cv2.imread('5ab3_0Artificial.jpg', cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

a_image = item1(binary_image)
cv2.imshow("A image", a_image)
cv2.waitKey(0)
