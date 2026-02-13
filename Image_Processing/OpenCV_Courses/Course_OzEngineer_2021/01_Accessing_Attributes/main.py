import cv2
import numpy as np

image_1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/OpenCV_Logo.png")
cv2.imshow("OCVLogo", image_1)
print(image_1.size)  # results as width x height x channel count
print(image_1.dtype)  # data type of the image
print(image_1.shape)  # width, height and channel count information
cv2.imwrite("OCV_V2.png", image_1)

image_2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/OpenCV_Logo.png", 0)
cv2.imshow("qwe", image_2)
print(image_2.size)
print(image_2.dtype)
print(image_2.shape)
cv2.waitKey(0)
cv2.destroyAllWindows
