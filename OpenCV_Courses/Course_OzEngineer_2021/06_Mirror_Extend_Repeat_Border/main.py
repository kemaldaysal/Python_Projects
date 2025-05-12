import cv2
import numpy as np

img = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_1.jpg")

img_mirrored = cv2.copyMakeBorder(img, 90, 90, 200, 200, cv2.BORDER_REFLECT)
img_extended = cv2.copyMakeBorder(img, 120, 120, 120, 120, cv2.BORDER_REPLICATE)
img_repeated = cv2.copyMakeBorder(img, 300, 300, 300, 300, cv2.BORDER_WRAP)
img_bordered = cv2.copyMakeBorder(
    img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=(75, 150, 255)
)

cv2.imshow("mirrored", img_mirrored)
cv2.imshow("extended", img_extended)
cv2.imshow("repeated", img_repeated)
cv2.imshow("bordered", img_bordered)

cv2.waitKey(0)
cv2.destroyAllWindows
