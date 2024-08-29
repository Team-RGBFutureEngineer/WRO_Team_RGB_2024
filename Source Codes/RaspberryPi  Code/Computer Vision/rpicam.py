from picamera2 import Picamera2, Preview
import cv2
import time
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="libpng")

# Create a Picamera2 instance
picam2 = Picamera2()

# Configure the camera for video
video_config = picam2.create_video_configuration(
    main={"size": (640, 480)},  # Reduce the resolution for higher frame rate
    controls={"FrameDurationLimits": (33333, 33333)}  # Set frame duration to approximately 30 fps
)

# Apply the configuration
picam2.configure(video_config)

# Start the camera
picam2.start()

# Allow some time for the camera to start
time.sleep(2)

while True:
    # Capture an image as a numpy array
    image = picam2.capture_array()

    # Convert the image to RGB (if needed)
    imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    # Display the image using OpenCV
    cv2.imshow('Captured Image', imagergb)

    # Wait until a key is pressed
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()

# Stop the camera
picam2.stop()

