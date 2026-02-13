import cv2
import numpy as np

img_wolf_1 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_1.jpg")
img_wolf_2 = cv2.imread("OpenCV_Courses/Course_OzEngineer/Sources/wolf_2.jpg", 0)

cv2.imshow("Wolf Image", img_wolf_1)
cv2.imshow("Wolf Image Gray", img_wolf_1)
print(
    img_wolf_1[(230, 80)]
)  # (0,0) is the top-left point. This shows the matris if we go 280 to the right and 80 to the bottom.
print("Size of 1st image: " + str(img_wolf_1.size))
print("Specs of 1st image: " + str(img_wolf_1.shape))
print("Datatype of 1st image: " + str(img_wolf_1.dtype))
print("")
print("Size of 2nd image: " + str(img_wolf_2.size))
print("Specs of 2nd image: " + str(img_wolf_2.shape))
print("Datatype of 2nd image: " + str(img_wolf_2.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
