import cv2
import numpy as np

img_1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/bl.jpg")
img_2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")

bit_And = cv2.bitwise_and(img_1, img_2)
bit_Or = cv2.bitwise_or(img_1, img_2)
bit_Xor = cv2.bitwise_xor(img_1, img_2)
bit_Not1 = cv2.bitwise_not(img_1)
bit_Not2 = cv2.bitwise_not(img_2)


cv2.imshow("img_1_original", img_1)
cv2.imshow("img_2_original", img_2)
cv2.imshow("Bitwise And", bit_And)
cv2.imshow("Bitwise Or", bit_Or)
cv2.imshow("Bitwise Xor", bit_Xor)
cv2.imshow("Bitwise Not", bit_Not1)
cv2.imshow("Bitwise Not", bit_Not2)

cv2.waitKey(0)
cv2.destroyAllWindows()
