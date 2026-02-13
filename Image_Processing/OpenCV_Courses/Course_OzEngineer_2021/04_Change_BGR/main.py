import cv2
import numpy as np

c1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")
c2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")
c3 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")
c4 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")
c5 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/cb.jpg")

cv2.imshow("c original", c1)


c1[:, :, 0] = 255  # 255 to 0. color dimension (blue)
c2[:, :, 1] = 255  # 255 to 1. color dimension (green)
c3[:, :, 2] = 255  # 255 to 2. color dimension (red)

c4[:, :, 1] = 255  # 255 to 1. color dimension (green)
c4[:, :, 2] = 255  # 255 to 2. color dimension (red) => green + red = yellow

c5[300:450, 150:240, 0] = (
    255  # 1st parameter is selected area on y axis, 2nd parameter is selected area on x axis, 3rd parameter is chosen BGR parameter (color).
)
print(c1.shape)

cv2.imshow("c1", c1)
cv2.imshow("c2", c2)
cv2.imshow("c3", c3)
cv2.imshow("c4", c4)
cv2.imshow("c5", c5)

cv2.waitKey(0)
cv2.destroyAllWindows
