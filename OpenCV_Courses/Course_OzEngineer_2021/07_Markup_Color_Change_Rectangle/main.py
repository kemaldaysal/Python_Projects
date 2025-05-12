import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses\Course_OzEngineer\Sources\wolf_1.jpg")

img[50:100, 230:310, 0] = 255
cv2.rectangle(img, (50, 100), (150, 30), [0, 0, 255], 5)

cv2.imshow("o", img)

cv2.waitKey(0)
cv2.destroyAllWindows
