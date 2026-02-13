import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_1.jpg")

img_double_size = cv2.pyrUp(img)  # Doubles both the height and width, ex: 480*520 becomes 960*1040
img_half_size = cv2.pyrDown(img)  # 2X smaller
img_square_size = (cv2.pyrUp(img)) ** 2 # square times bigger

print("Shape img_original: ", img.shape)
print("Shape img_double_size: ", img_double_size.shape)
print("Shape img_half_size: ", img_half_size.shape)
print("Shape img_square_size :", img_square_size.shape)

cv2.imshow("img_original", img)
cv2.imshow("img_double_size", img_double_size)
cv2.imshow("img_half_size", img_half_size)
cv2.imshow("img_square_size (anomaly)", img_square_size)

cv2.waitKey(0)
cv2.destroyAllWindows
