import cv2
from item1 import item1
from item2 import item2
from item3 import item3
from item4 import item4
from item5 import item5
from item6 import item6
from item7 import item7
from item8 import item8

image = cv2.imread('5ab3_0Artificial.jpg', cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

a_image = item1(binary_image)
b_image = item2(a_image)
c_image = item3(a_image, b_image)
d_image = item4(a_image, c_image)
e_image = item5(c_image)
f_image = item6(a_image, e_image)
g_image = item7(a_image, d_image, item6(a_image, e_image))
type2, type3 = item8(g_image)
cv2.imshow("A image", a_image)
cv2.imwrite('A.png', a_image)
cv2.imshow("B image", b_image)
cv2.imwrite('B.png', b_image)
cv2.imshow("C image", c_image)
cv2.imwrite('C.png', c_image)
cv2.imshow("D image", d_image)
cv2.imwrite('D.png', d_image)
cv2.imshow("E image", e_image)
cv2.imwrite('E.png', e_image)
cv2.imshow("F image", f_image)
cv2.imwrite('F.png', f_image)
cv2.imshow("G image", g_image)
cv2.imwrite('G.png', g_image)
cv2.imshow("Type 2 image", type2)
cv2.imwrite('Type2.png', type2)
cv2.imshow("Type 3 image", type3)
cv2.imwrite('Type3.png', type3)

cv2.waitKey(0)
