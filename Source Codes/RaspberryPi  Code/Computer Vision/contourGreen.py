import numpy as np
import cv2
from picamera2 import Picamera2
from time import sleep

picamera2 = Picamera2()
config = picamera2.create_video_configuration(main={"size": (640, 480)})
picamera2.configure(config)

picamera2.start()
while True:
    image = picamera2.capture_array()
    image = cv2.flip(image, -1)
    imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imagehsv = cv2.cvtColor(imagergb, cv2.COLOR_BGR2HSV)
    key = cv2.waitKey(1)
    
    lowergreen1 = np.array([35, 100, 50])  # Saturation Less = Lighter
    uppergreen1 = np.array([80, 255, 255])
    
    result = cv2.inRange(imagehsv, lowergreen1, uppergreen1)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around detected contours and display area
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1200:  # Adjust the threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Display the area on the image
            cv2.putText(image, f'Area: {int(area)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Display the image with contours and areas
    cv2.imshow("image_combined", image)
    
    if key == ord("q") or key == 27:
        break

picamera2.stop()
cv2.destroyAllWindows()
