import cv2
import numpy as np

camera = cv2.VideoCapture(0)  # 0 for internal webcam

while True:
    check, video_frame_captured = camera.read()

    cv2.rectangle(video_frame_captured, (100, 100), (200, 200), (0, 0, 255), 2)

    cv2.line(video_frame_captured, (0, 0), (100, 100), (255, 0, 0), 1)

    cv2.circle(video_frame_captured, (100, 100), 50, (0, 255, 0), 2)

    cv2.putText(
        video_frame_captured,
        "KD",
        (150, 150),
        cv2.FONT_HERSHEY_DUPLEX,
        4,
        (200, 100, 100),
        2,
    )

    cv2.imshow("Webcam", video_frame_captured)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()
