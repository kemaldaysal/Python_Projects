import cv2
import numpy as np

img_1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_2.jpg")
img_2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_3.jpg")

total = cv2.add(img_1, img_2)
total_weighted = cv2.addWeighted(
    img_1, 0.7, img_2, 0.3, 0
)  # %70 of img1, %30 of img2

cv2.imshow("Added images", total)
cv2.imshow("Weighted total", total_weighted)

cv2.waitKey(0)
cv2.destroyAllWindows
