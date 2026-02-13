import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype="uint8")

cv2.line(img, (50, 50), (100, 100), (20, 60, 255), 3)  # (0,0) is the top-left
cv2.line(img, (50, 150), (100, 100), (150, 60, 255), 5)
# img, p1, p2, bgr values, width
cv2.circle(img, (150, 150), 25, (0, 255, 0), 2)

cv2.putText(
    img, "KD", (40, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2
)

cv2.imshow("test", img)

cv2.waitKey(0)
cv2.destroyAllWindows
