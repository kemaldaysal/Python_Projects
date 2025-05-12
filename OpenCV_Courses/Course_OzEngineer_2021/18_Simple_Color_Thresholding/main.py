import cv2

img_gray = cv2.imread("OpenCV_Courses\Course_OzEngineer\Sources\color_triangle.jpg", 0)

ret, thresh1 = cv2.threshold(
    img_gray, 127, 255, cv2.THRESH_BINARY
)  #  (colors < 127 : floor to 0) (colors > 127 : ceil to 255)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow("Original Gray", img_gray)
cv2.imshow("Thresh1", thresh1)
cv2.imshow("Thresh2", thresh2)
cv2.imshow("Thresh3", thresh3)
cv2.imshow("Thresh4", thresh4)

cv2.waitKey(0)
cv2.destroyAllWindows
