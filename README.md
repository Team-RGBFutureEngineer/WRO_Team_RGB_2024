# Team RGB – WRO Future Engineers 2024

We are **Team RGB**, a duo of engineering students from **RFL Academy**, united by our passion for **Robotics**. We have clearly divided our roles to maximize our strengths:

**Bhavya – Lead Programmer & Electronics**: Bhavya is responsible for the robot's programming and electronics systems. He specializes in developing advanced control algorithms, including PID control, and designing the logic that powers the robot’s movements and decision-making. Bhavya ensures the seamless integration of sensors and motors, programming the robot to execute precise maneuvers for both the open-round and obstacle-round. 

**Raj – Lead Designer & Constructor** Raj is responsible for the structural and mechanical design of the robot. With a focus on precision and functionality, he uses CAD software to create a robust and lightweight design that adheres to the competition’s strict dimension and weight restrictions. Raj specializes in optimizing the integration of LEGO components with custom-designed parts, ensuring the robot performs reliably in both maneuverability and stability under competition conditions.

# Programming
During the initial two iterations of our robot, we utilized a 3D-printed chassis to allow for greater customization and explore new design possibilities. For processing and control, we opted to use a Raspberry Pi, despite it being our first time working with this platform, including its schematics and programming interface.

To streamline our workflow, we researched methods for accessing and controlling the **Raspberry Pi** without the need for external peripherals like a monitor or keyboard. We initially implemented **RealVNC Viewer**, a software solution that enabled remote access to the Raspberry Pi from the development computer. However, we soon encountered performance limitations, as the virtual environment proved to be too laggy, negatively impacting the overall user experience and efficiency.

Later, we discovered that by utilizing OBS Studio in conjunction with an HDMI Input to Output converter, we could display the Raspberry Pi's interface on a primary monitor, enabling direct editing in the main window. As we were new to working with the Raspberry Pi, initially, gathering resources and compiling the necessary code posed a significant challenge. Several features required extensive installation and configuration, further complicating the process.

After over **30 days of working with the Raspberry Pi**, we identified opportunities to enhance system performance by incorporating an **Arduino board**. This allowed us to optimize the robot's functionality by distributing tasks between the **Arduino and the Raspberry Pi**, which successfully met our performance objectives.

However, due to structural constraints and the limited available space for components, wiring, and the power distribution board, we faced difficulties fitting everything within the robot’s designated size restrictions. Following a comprehensive evaluation of both the construction and programming challenges, we collectively decided to transition to the **LEGO EV3** system. Our prior familiarity with these components enabled a smoother transition, allowing us to work more efficiently. With the **EV3 Mindstorms platform** and the **PixyCam**, which is compatible with the EV3, we achieved greater efficiency compared to the Raspberry Pi setup. The LEGO system also provided the flexibility to easily modify and customize the robot’s design to suit our needs.

## Open Round Challenge

![OpenRound_Flowchart](https://github.com/user-attachments/assets/fa6db531-46c2-4e71-9b5b-24b2b72e4e04)


The robot’s journey begins by determining which direction it should turn over the course of the next **3 laps**. To achieve this, we rely on **Ultrasonic Sensors** mounted on both sides of the robot to detect the absence of walls.

As the robot approaches a potential **turning point**, it calculates the average of the sensor readings. The robot continues moving forward as long as this average remains below 80, which indicates that walls are detected on both sides. During this phase, the **Gyro Sensor** ensures that the robot maintains a **straight path**.

When the sensor reading exceeds 80, this indicates that a wall is missing on one side. At this point, the robot checks whether the **UltrasonicLeft** reading is greater than 100. If this condition is met, the robot initiates a left turn. Otherwise, it performs a right turn.

The turns are executed with the assistance of the **Gyro Sensor**, providing increased accuracy during the maneuver.

Once the direction is determined, the robot continues moving forward under **Gyro PID control** until the relevant sensor (for example, if a left turn was initiated, the UltrasonicLeft sensor) detects the presence of a wall again. When the wall is no longer detected, the robot completes the turn.

To track the robot’s progress, a **counter** is incremented by one with each turn. When the counter reaches 12, indicating that three laps have been completed, the robot stops.

**_Description of blocks are given in the sections later_**

## Obstacle Round

![OBSTACLE ROUND FLOWCHART](https://github.com/user-attachments/assets/00f83453-4397-4a2c-9bf4-4a0780c4e030)

The robot’s journey begins with checking Ultrasonic Sensor’s readings for deciding what turn to take. Once that is decided the code for taking respective turns starts.

The **Pixy Camera** connected to the Ev3 constantly keeps checking if any block **(Green or Red is detected)**. If yes, then it moves closer to the block until its area is above 2000 (Area is calculated by multiplying the length &  width of the block. 
If the block is RED --> Take a Right Turn
If the block is Green --> Take a Left Turn

With every operation a separate loop of checking the Blue lines and Orange lines is checked. If at the start it was decided that the robot will take a Left turn then the Blue line is checked and vice verse.
When the line is detected the robot takes a **Gyro based** 90 degree turn.

At the end of 7 turns, the robot keeps on detecting the elements and the values of them are stored in an array. After the 8th turn **the robot decides if it has to take a U-Turn or not** based on the last block which is Red or Green.

Later the 4 rounds are completed and the robot gets into the search of parking that is of color Magenta. After following it using the **encoder** values of the motor we have tried to park the robot fully inside the provided parking area.

## Blocks Description

**Gyro PID**: This block is responsible to keep the robot driving straight with respect to the gyro sensor’s value.  The calculation goes as follows:
Gyro Sensor’s current reading – Threshold value(set by the user)  = Current Error
Current Error * 0.8 = kp (The value 0.8 needs to be tuned with respect to each robot)
(Current Error – Previous Error) * 0.5 = kd (The value 0.8 needs to be tuned with respect to each robot)
Kp + kd = final_value (This value needs to be passed to the Steering motor’s power)
Assign the previous value as the current error for the next loop
(previous_error = current_error)

![gyro pid](https://github.com/user-attachments/assets/df2e87f6-e31c-473d-8be8-edd3ce14a413)

**GyroTurnLeft or GyroTurnRight**: This block is used to ensure that the robot turns a specific angle that is the required target position
Here the current value of Gyro sensor is noted.
Turn and Steering motor and keep the drive motor ON until the gyro sensor’s value is not greater than the target value
Run this in a loop
Make the steering motor back to its original position 
(Motor Encoder value * -1) is given to the motor’s target position to bring the steering motor back to its original position

![gyro left](https://github.com/user-attachments/assets/da88db00-fbdf-4519-8119-1803e69f0982)

**Obstacle Sense:** Here we calculate how much the robot has to turn and return to its value for passing an obstacle (red or green)
Read the values of the detected object, Multiply the height and width of object to check how near it is to the robot
When it is near to the robot, take a turn and drive the motor until **The camera cannot see the block**
Return the Steering motor to its original positon and keep moving ahead
![obstacle sense](https://github.com/user-attachments/assets/d01555af-ee1a-4ebf-9800-b036567c54c6)


**Ultrasonic Sensor Wall Follow PID**: This block is responsible to keep the robot driving straight with respect to the deviation of the robot from both the side walls.  We’ll be using 2 sensors, 1 on left and the other on right for better accuracy. The calculation goes as follows:
Left Ultrasonic Sensor’s current reading – Right Ultrasonic Sensor’s current reading  = Current Error
(Current Error – Previous Error) * 0.5 = magnified final value (The value 0.5 needs to be tuned with respect to each robot)
This final value needs to be passed to the Steering motor’s power
Assign the previous error value as the current error value

![wall follow pid](https://github.com/user-attachments/assets/f416382a-693f-4a13-9c9a-8b2b8eae5fdd)



# Construction
In the **Initial phase** of our design, we prioritized selecting lightweight yet durable components to ensure the robot maintained an optimal balance between strength and weight. Our first iteration featured a **3D-printed chassis** combined with a **steering mechanism** constructed from **LEGO parts**. However, this design presented several limitations, as the integration of the LEGO components with the 3D-printed chassis proved unreliable, and the overall structure became too bulky and heavy.

For the **Second iteration**, we transitioned to a **fully 3D-printed design**, including the steering mechanism. This solved many of the issues encountered in the previous version. The meshing of the **3D-printed gears** and steering components was precise. However, we faced challenges in aligning some parts during assembly, and reprinting components was **time-consuming** when adjustments were needed.

In the **Third iteration**, we opted for a **fully LEGO-based chassis**. Given that we had already achieved a precise gear mesh using custom **3D-printed gears and racks**, we integrated these components into the new design. The rear wheel motor relied on LEGO gears, while the steering mechanism utilized a custom 3D-printed gear perfectly matched with a custom 3D-printed rack, offering the best combination of customization and reliability.

Our robot measures **16.5 cm in length, 16 cm in width, and 24 cm in height**, with a total weight of **0.9 kg**. It is powered by **two medium motors**—one dedicated to driving the rear wheels and the other for controlling the steering mechanism. The rear wheels (62.4 x 20s) are mounted on a **single axle** and connected to the motor via LEGO gears. The steering wheels (62.3 x 21s) are also mounted on a single axle and connected to the motor, with the steering system operating through the custom 3D-printed gear and rack, ensuring smooth and precise movement.

The robot is equipped with two **LEGO ultrasonic sensors**, mounted on both left & right side, and a **gyro sensor** placed on top for navigation. For obstacle detection, we integrated a **Pixy 2.1 camera**. The entire system is powered by a **LEGO Mindstorms EV3 brick**, which manages the control and coordination of the sensors and motors.

# Custom 3D Printed Parts
## Rack & Gear
![rack](https://github.com/user-attachments/assets/8095da94-c97d-4a3a-9b54-2e79d7d563b5)
![gear](https://github.com/user-attachments/assets/e8f77b26-07b3-4e20-b14b-a0db9464e79c)

We designed a custom 7.2 cm rack with a similar groove pattern and design as the standard 6.4 cm LEGO rack. The original 6.4 cm LEGO rack had some problems wherein its shorter length made it difficult to mesh smoothly with the 20-tooth double bevel black LEGO gear, which restricted the wheels from achieving specific steering angles.

However, even with our 7.2 cm rack, we encountered a minor issue: the grooves of the black LEGO gear and our custom rack weren’t perfectly meshing. While it functioned temporarily, the meshing wasn't ideal, and the error compounded by 0.01 with each turn. To overcome this, we also created a custom 12 tooth gear whose grooves are perfectly meshing with custom rack thus eliminating meshing errors and significantly improved the accuracy of the steering, allowing the wheels to turn at precise angles.


## Pixy Mount & Beam

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
### LEGO Mindstorm EV3 Brick
The EV3 Brick is the central control unit of our robot. It features a programmable interface with a display screen and buttons for manual control. It is programmed using LEGO's Mindstorm software. It has 4 ports for Input and output, currently, our bot uses 2 output ports for both medium motors and 3 input ports for 2 ultrasonic sensors and gyro sensors.
### LEGO Rechargeable DC Battery
This 2000 mAh battery provides power to the EV3 Brick and other components. It is rechargeable and designed to fit into the EV3 Brick.
### EV3 Medium Servo Motor
The medium servo motor is used for precise movements and rotations. It is smaller in size compared to the large motor and is capable of rotating 360 degrees with precise angle control, useful for the steering mechanism.
### LEGO Ultrasonic Sensors
These sensors are placed on both sides of the robot and measure the distance between the wall and the robot by emitting ultrasonic waves and measuring the time it takes for the waves to return. It's useful for obstacle detection and open-round challenge.
### LEGO Gyro Sensor
The gyro sensor mounted on top measures the rate of rotation around the sensor’s axis. It helps in precise robot movement, detecting orientation changes, and stabilizing movements, which is crucial for our robot’s journey.
### Pixy 2.1 Camera
The PIXY 2.1 Camera is an advanced vision sensor that can detect and track objects based on color. It provides real-time image processing capabilities and is used for object detection in obstacle challenge.
### LEGO Cables
These cables help in building connections between motors, and sensors to the EV3 Brick. They are responsible for transmitting power and data between the components and EV3 Brick.
### LEGO Russian Wheels (62.4 x 20)
These wheels are used as rear wheels in our robot. These wheels are 62.4 mm in diameter and 20 mm in width.
### LEGO Tractor Wheels (56 x 26)
These wheels are used as front wheels in our robot. These wheels are 56 mm in diameter and 26 mm in width.

