import cv2

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/noisy_1.jpg")

img_mean_filter_1 = cv2.blur(img, (3, 3))
img_mean_filter_2 = cv2.blur(img, (5, 5))
img_mean_filter_3 = cv2.blur(img, (7, 7))

img_median_filter_1 = cv2.medianBlur(img, 3)
img_median_filter_2 = cv2.medianBlur(img, 5)
img_median_filter_3 = cv2.medianBlur(img, 7)

img_gauss_filter_1 = cv2.GaussianBlur(img, (3, 3), 0)
img_gauss_filter_2 = cv2.GaussianBlur(img, (5, 5), 0)
img_gauss_filter_3 = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow("img_original", img)
cv2.imshow("Mean Filter 3,3", img_mean_filter_1)
cv2.imshow("Mean Filter 5,5", img_mean_filter_2)
cv2.imshow("Mean Filter 7x7", img_mean_filter_3)

cv2.imshow("Median Filter 3x3", img_median_filter_1)
cv2.imshow("Median Filter 5x5", img_median_filter_2)
cv2.imshow("Median Filter 7x7", img_median_filter_3)

cv2.imshow("Gauss Filter 3x3", img_gauss_filter_1)
cv2.imshow("Gauss Filter 5x5", img_gauss_filter_2)
cv2.imshow("Gauss Filter 7x7", img_gauss_filter_3)


cv2.waitKey(0)
cv2.destroyAllWindows()
