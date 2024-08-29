import numpy as np
import cv2
from picamera2 import Picamera2
from time import sleep

picamera2 = Picamera2()
config = picamera2.create_video_configuration(main={"size": (640,480)})
picamera2.configure(config)

picamera2.start()
while True:
    image =picamera2.capture_array()
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(1)
    mask_3 =cv2.cvtColor(image2,cv2.COLOR_GRAY2BGR)
    _,image3 = cv2.threshold(image2, 200, 255, cv2.THRESH_BINARY)
    
    lowerred1 = np.array([35, 100, 50])
    #lowerred2 = np.array([15, 150, 100])
    upperred1 = np.array([85, 255, 255])
    #upperred2 = np.array([180, 255, 255])
    
    final = cv2.inRange(image1, lowerred1, upperred1)
    #final2 = cv2.inRange(image1, lowerred2, upperred2)
    
    #result = cv2.bitwise_or(final, final2)
    cv2.imshow("image_combined", final)
    
    if key == ord("q") or key == 27:
        break;
#cv2.imwrite("HSV&GRAY.jpg", combined)
picamera2.stop()


cv2.destroyAllWindows()
