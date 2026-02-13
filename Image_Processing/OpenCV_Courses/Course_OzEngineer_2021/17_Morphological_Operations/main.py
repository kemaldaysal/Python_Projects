import cv2
import numpy as np

image = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/color_triangle.jpg")

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(image, kernel, iterations=1)
dilation2 = cv2.dilate(image, kernel, iterations=2)
erosion = cv2.erode(image, kernel, iterations=1)
erosion2 = cv2.erode(image, kernel, iterations=2)

dilationM = cv2.dilate(image, kernel, iterations=1)
erosionM = cv2.erode(dilationM, kernel, iterations=1)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

gradyan = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", image)
cv2.imshow("Dilation it=1", dilation)
cv2.imshow("Dilation it=2", dilation2)
cv2.imshow("Erosion it=1", erosion)
cv2.imshow("Erosion it=2", erosion2)
cv2.imshow("Mixed", erosionM)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradyan", gradyan)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
