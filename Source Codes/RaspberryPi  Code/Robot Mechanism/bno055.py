import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')
import pigpio
from picamera2 import Picamera2, Preview
import cv2


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

def color_detect(frame, lower, upper):
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame1, lower, upper)
    x1,y1,w1,h1 = 0,0,0,0
    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxcolor = (255,255,255)
    try:
        contour = max(contours, key = cv2.contourArea)
    except:
        return img, x1
    area = cv2.contourArea(contour)
    if area >800:
        x,y,w,h = cv2.boundingRect(contour)
        if (x+w)<=320 and (y+h)>70:
            cv2.rectangle(frame, (x,y), (x+w,y+h), boxcolor,2)
        else:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
        cv2.putText(frame, str(y), (x,y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, boxcolor, 2)
        if (x+w)<=320 and (y+h)>70:
            x1 = 0
    return frame,x1



def pid(y, heading):
    if(y<360-y):
        y = y
    elif (y == 360-y):
        y=180
    else:
        y = -360+y
    if(heading<360-heading):
        heading = heading
    elif (heading == 360-heading):
        heading=180
    else:
        heading = -360+heading
    if heading<0 and y<0:
        error = heading-y
    elif heading<0 and y>0:
        error = y+heading
    else:
        error = heading - y
    turn = min(1600,max(800,1200 -error*5))
    return turn
pi = pigpio.pi()
pi.set_mode(18,pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
i2c = busio.I2C(board.SCL, board.SDA)
ser = serial.Serial('/dev/ttyACM1', 9600)
sensor = adafruit_bno055.BNO055_I2C(i2c)
heading = 0.0
roll = 0.0
pitch =0.0
dis =  0.0
value =  360
x = 0
logic = False
flag = True
cam = False
while True:
    #try:
    img = picam2.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.flip(img,-1)
    img[0:240, 50:640,:] = 255
    img[0:80, 0:50,:] = 255
    img,x = color_detect(img, (0,0,0) , (255,50,50))
    cv2.imshow("frame",img)
    heading, roll, pitch = sensor.euler
    try:
        heading = min(360,max(0,heading))
    except:
        heading = 0
    dis = float((ser.readline().decode('utf-8',errors='ignore').rstrip()))
#     try:
#         dis1,dis,dis3 = map(float, data.split(','))
#     except:
#         dis1 = dis = dis3 = 0
    #except:
   # heading = 0
    #dis = 0.0
#         heading = 0

    print(heading,dis)
    if (dis>100 and x==0) or logic:
        if flag:
            value = value-90
            flag  = False
        if (heading>(value+30)):
            logic = True
        elif (heading<(value+30)):
            logic = False
        pi.set_servo_pulsewidth(18, 900)
        print("turning", value, heading, dis)
    else:
        logic= False
        flag = True
        pi.set_servo_pulsewidth(18,pid(value,heading))        
   # pi.set_servo_pulsewidth(13,1600)
    key = cv2.waitKey(1)
    if key == 1 or key == ord('q'):
        break
    
logic = False
pi.set_servo_pulsewidth(13,0)
cv2.destroyAllWindows()
picam2.stop()
pi.stop()