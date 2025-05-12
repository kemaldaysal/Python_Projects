import cv2
import numpy as np

camera = cv2.VideoCapture(
    0
)  # 0 for internal webcam. 1 for USB webcam. 2 for getting video from an address

while True:
    check, video_frame_captured = (
        camera.read()
    )  # "check" variable for checking if camera is ready. Captured video will be saved into "video_frame_captured" variable

    cv2.imshow("Webcam", video_frame_captured)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

    # cv2.waitKey(30) :
    #   Waits 30 milliseconds for a key event.
    #   Returns a 32-bit integer representing the key pressed (if any) during that interval.
    #   If no key is pressed within 30 ms, it returns -1

    # & with 0xFF :
    #   This ensures only the lowest 8 bits of the key code are kept, which is necessary on some platforms (especially Windows) to correctly interpret ASCII keys.

    # ord('q') :
    #   Converts the character 'q' to its ASCII value, which is 113

    # Summary: Checks every 30 milliseconds if the user pressed 'q'. If so, it exits the loop — typically used to stop video playback or end the program.


camera.release()
cv2.destroyAllWindows
