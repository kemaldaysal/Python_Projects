import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_2.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# or to initially import it as gray
# img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_2.jpg",0)

img_height, img_width, img_channel_count = img.shape
img_height, img_width = img_gray.shape


print("Dimensions of original: ", img_width, img_height, img_channel_count)
print("Dimensions of gray: ", img_width, img_height)

cv2.imshow("img_original", img)
cv2.imshow("img_gray", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows
