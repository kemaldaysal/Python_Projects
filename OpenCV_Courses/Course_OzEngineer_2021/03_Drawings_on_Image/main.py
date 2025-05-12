import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_1.jpg")

img[50,30]=[255,255,255]

for i in range(100):
    img[70,i]=[255,255,255]

cv2.imshow("Wolf",img)

cv2.waitKey(0)
cv2.destroyAllWindows
