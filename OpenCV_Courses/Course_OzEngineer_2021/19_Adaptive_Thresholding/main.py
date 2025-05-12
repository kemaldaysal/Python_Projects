import cv2

img_gray = cv2.imread("OpenCV_Courses\Course_OzEngineer\Sources\color_triangle.jpg", 0)

# simple thresholding
ret, thresh1 = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)

# adaptive thresholding
thresh2 = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
thresh3 = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cv2.imshow("Original Gray", img_gray)
cv2.imshow("Simple thresholding", thresh1)
cv2.imshow("Adpt Mean Binary", thresh2)
cv2.imshow("Adpt Gaussian Binary", thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows
