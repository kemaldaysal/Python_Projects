import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/color_triangle.jpg")
snippet = img[50:150, 300:400]

print("Shape of the original image: ",img.shape)
print("Shape of the snippet: ", snippet.shape)

img[0:100, 0:100] = snippet
img[400:450, 300:350] = (0, 150, 255)

cv2.imshow("snippet", snippet)
cv2.imshow("new_img", img)

cv2.waitKey(0)
cv2.destroyAllWindows
