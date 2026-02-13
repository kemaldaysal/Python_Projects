import cv2

img_gray = cv2.imread("fp.jpg", 0)

# Simple Thresholding
ret1, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Otsu Thresholding

ret2, thresh2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Original Gray", img_gray)
cv2.imshow("Simple", thresh1)
cv2.imshow("Otsu", thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()
