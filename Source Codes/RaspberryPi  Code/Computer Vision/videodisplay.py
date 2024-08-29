from picamera2 import Picamera2
from time import sleep
import cv2


cap = cv2.VideoCapture("frc.mp4")
cv2.namedWindow("video")


while True:
    sucess, img = cap.read()
    
    cv2.imshow("video", img)
    key = cv2.waitKey(1)
    if key == ord("q") or key == 27:
        break;

cap.release()
cv2.destroyAllWindows()
