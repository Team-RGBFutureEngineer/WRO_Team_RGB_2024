import numpy as np
import cv2
from picamera2 import Picamera2
from time import sleep

# Initialize the camera
picamera2 = Picamera2()
config = picamera2.create_video_configuration(main={"size": (640, 480)})
picamera2.configure(config)

# Start the camera
picamera2.start()

while True:
    # Capture image from camera
    image = picamera2.capture_array()
    # Flip the image if necessary
    image = cv2.flip(image, -1)
    
    rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(rgba, cv2.COLOR_RGB2GRAY)
    
    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY_INV)

    # Apply Canny edge detection on the binary image
    canny_image = cv2.Canny(binary_image, 100, 200)
    
    # Apply Hough Line Transform on the Canny edge-detected image
    lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, threshold=100, minLineLength=10, maxLineGap=100)

    # Draw lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(rgba, (x1, y1), (x2, y2), (0, 255, 0), 4)
    
    # Convert Canny image to BGR so it can be stacked with the original
    canny_bgr = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)

    # Display the original and Canny images side by side
    combined_image = np.hstack((rgba, canny_bgr))
    cv2.imshow("Original and Canny Image", combined_image)

    # Exit on 'q' or ESC key press
    key = cv2.waitKey(1)
    if key == ord("q") or key == 27:
        break

# Stop the camera and close windows
picamera2.stop()
cv2.destroyAllWindows()
