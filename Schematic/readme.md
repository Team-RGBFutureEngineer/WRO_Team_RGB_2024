# Electricals 

![Robot Schematic](https://github.com/user-attachments/assets/d2b84f4b-e492-4aad-9a12-90fa8efba9e2)

This diagram illustrates the wiring and components configuration of our robot 

### Central Unit
EV3 Brick
### Input Ports (1-4)
- **Port 1: Left LEGO Ultrasonic Sensor**
- **Port 2: Right LEGO Ultrasonic Sensor**
- **Port 3: Gyro Sensor**
- **Port 4: Pixy Camera**
### Output Ports (A-D)
- **Port A: Rear Wheel Motor**
- **Port B: Steering Wheel Motor**

# Power Management

![LEGO DC BATTERY](https://github.com/user-attachments/assets/9227707d-84c7-4975-9733-bac62a0f826d)

This is our 2050 mA DC Rechargeable Battery which provides power to the EV3 Brick and other components. Here's an estimated power consumption breakdown for each component:

**1. LEGO Ultrasonic Sensor:**
- Current Consumption: Approximately **20 mA**
- Power Consumption: Approximately **0.2W**

**2. LEGO Medium Motor:**
- Current Consumption: Between **100-150 mA** 
- Power Consumption: Approximately **1.25W**
  
**3. LEGO Gyro Sensor:**
- Current Consumption: Approximately **10-15 mA**
- Power Consumption: Approximately **0.15W**
  
**4. LEGO EV3 Brick:**
- Current Consumption: Between **150-250 mA**
- Power Consumption: Approximately **2W**
  
**5. Pixy 2.1 Camera:**
- Current Consumption: Approximately **140 mA**
- Power Consumption: Approximately **1.4W**

![graph](https://github.com/user-attachments/assets/310029dd-aa59-4a5c-bcad-7cd09deb4638)


# Components

Our bot consists of the following components:
- LEGO Mindstorm EV3 Brick
- LEGO Rechargeable DC Battery
- EV3 Medium Servo Motor
- LEGO Ultrasonic Sensors
- LEGO Gyro Sensor
- PIXY 2.1 Camera
- Lego Cables
- Russian Wheels
- Steering Wheels
### 1. LEGO Mindstorm EV3 Brick
The EV3 Brick is the central control unit of our robot. It features a programmable interface with a display screen and buttons for manual control. It is programmed using LEGO's Mindstorm software. It has 4 ports for Input and output, currently, our bot uses 2 output ports for both medium motors and 3 input ports for 2 ultrasonic sensors and gyro sensors.

### 2. LEGO Rechargeable DC Battery
This 2000 mAh battery provides power to the EV3 Brick and other components. It is rechargeable and designed to fit into the EV3 Brick.

### 3. EV3 Medium Servo Motor
The medium servo motor is used for precise movements and rotations. It is smaller in size compared to the large motor and is capable of rotating 360 degrees with precise angle control, useful for the steering mechanism.

### 4. LEGO Ultrasonic Sensors
The sensors are mounted on both sides of the robot to accurately measure the proximity to adjacent walls. The sensor then measures the round-trip time for the reflected waves to return. By calculating the time interval between emission and reception, the sensor determines the distance between the robot and the wall using the speed of sound in air as a constant.

### 5. LEGO Gyro Sensor
The sensor is mounted on the top of the robot, it enables precise control over the robot's orientation adjustments and stability by detecting minute changes in angular displacement. It plays an essential role in trajectory tracking by calculating and storing the robot’s initial position. Over the course of three laps, the gyro ensures that the robot consistently returns to its starting position.

### 6. Pixy 2.1 Camera
The PIXY 2.1 Camera is an advanced vision sensor that can detect and track objects based on color. It provides real-time image processing capabilities and is used for object detection in obstacle challenge.

### 7. LEGO Cables
These cables help in building connections between motors, and sensors to the EV3 Brick. They are responsible for transmitting power and data between the components and EV3 Brick.

### 8. LEGO Russian Wheels (62.4 x 20)
These wheels are used as rear wheels in our robot. These wheels are 62.4 mm in diameter and 20 mm in width.

### 9. LEGO Tractor Wheels (56 x 26)
These wheels are used as front wheels in our robot. These wheels are 56 mm in diameter and 26 mm in width.
