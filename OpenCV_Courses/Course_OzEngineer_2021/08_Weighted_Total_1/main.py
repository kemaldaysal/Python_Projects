import cv2
import numpy as np

img_1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_1.jpg")
img_2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/bear_1.jpg")

print(img_1[100, 200])
print(img_2[300, 430])

cv2.imshow("wolf", img_1)
cv2.imshow("bear", img_2)

print(img_1[100, 200] + img_2[300, 430])

cv2.waitKey(0)
cv2.destroyAllWindows()
