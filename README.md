# Team RGB – WRO Future Engineers 2024

We are Team RGB, the duo of engineering students from RFL Academy, driven by a passion for robotics. We have divided our roles:

**Bhavya – Programmer & Electronics**: He works on the robot with PID control, creates logic & algorithms. He programmed the robot’s journey in both the open-round challenge and the obstacle round, ensuring smooth and precise operation. 

**Raj - Constructor**: He is into Robot’s CAD design and enjoys working with LEGO components. He focuses on designing a sturdy and functional robot considering the dimensions and weight restrictions.

# Programming
In our first two iterations while we were using the 3D printed chassis for better customizations and to try something new, we decided to use the **Raspberry Pi**.
It was our first time using the Raspi having no hands-on experience with all the schematics or even the programming aspect of the raspberry pi. At the start, inorder to use the raspi we researched the best way to program it which gave us an option of the __Real-VNC viewer__ which turned out to be really good. But, this virtual machine was too laggy, therefore not giving us the best experience to work with. 

Later, we found out that using __OBS studio__ we could use an Hdmi Input to Output converter to view Raspberry Pi’s screen and edit in the main window.
Being newbies in working with raspberry pi, I found it too difficult to gather resources and then compile codes to run it. Several features required too much of installation on the board and for setting it up.

After working with it for more than 30 days, we felt that we could add an Arduino board to improve performance of several components and also divide the tasks between **Arduino and Rapsberry Pi**. This worked to our expectations.

Due to construction difficulties we were not able to incorporate so many components, wiring, power distribution board on the robot under the given size restrictions.
Finally, after discussing with my teammate about the difficulties that both of us face for the construction and the programming, we finally decided to shift to **Lego Ev3**. We were pretty much familiar with these components making it easy for us to move with. With the help of EV3 Mindstorms and the PixyCam that is compatible with Ev3, we are now able to perform the tasks at a better pace rather than using the Raspberry Pi. Lego helps us modify and customize the blocks as per our ease making it too easy to work with.

## Open Round Challenge

![OpenRound_Flowchart](https://github.com/user-attachments/assets/fa6db531-46c2-4e71-9b5b-24b2b72e4e04)


We begin our journey by determining which side the robot should turn for the next 3 laps. To do this, we rely on **Ultrasonic Sensors** mounted on both sides of the bot to detect where a wall is absent.
As the robot approaches the turning point, it calculates the average of the sensor readings. The robot continues moving forward as long as this average remains below 80, indicating that walls are detected on both sides.
The **Gyro sensor** keeps the robot moving straight during this phase.
When the sensor reading exceeds 80, it signals that a wall is missing on one side. At this point, the robot checks if UltrasonicLeft > 100. If true, it means the bot needs to make a Left Turn. Otherwise, it will make a Right Turn.
>The turns are executed using the Gyro sensor for increased accuracy.
After determining the direction, the robot continues moving forward with Gyro PID control until the relevant sensor (For eg: If a left turn is decided, the UltrasonicLeft plays the role in the program ahead) detects the wall again and when it does not detect the wall, the robot takes the turn.
To determine the end of 3 laps, with each turn the counter increments by 1. If the values of counter == 12 that is 3 laps are completed, the robot stops.

**_Description of blocks are given in the sections later_**

### Blocks Description
**Gyro PID**: This block is responsible to keep the robot driving straight with respect to the gyro sensor’s value.  The calculation goes as follows:
Gyro Sensor’s current reading – Threshold value(set by the user)  = Current Error
Current Error * 0.8 = kp (The value 0.8 needs to be tuned with respect to each robot)
(Current Error – Previous Error) * 0.5 = kd (The value 0.8 needs to be tuned with respect to each robot)
Kp + kd = final_value (This value needs to be passed to the Steering motor’s power)
Assign the previous value as the current error for the next loop
(previous_error = current_error)

![Screenshot_16](https://github.com/user-attachments/assets/b8905f74-a691-403a-8494-04db38c7a1e8)

**GyroTurnLeft or GyroTurnRight**: This block is used to ensure that the robot turns a specific angle that is the required target position
Here the current value of Gyro sensor is noted.
Turn and Steering motor and keep the drive motor ON until the gyro sensor’s value is not greater than the target value
Run this in a loop
Make the steering motor back to its original position 
(Motor Encoder value * -1) is given to the motor’s target position to bring the steering motor back to its original position

**Obstacle Sense:** Here we calculate how much the robot has to turn and return to its value for passing an obstacle (red or green)
Read the values of the detected object, Multiply the height and width of object to check how near it is to the robot
When it is near to the robot, take a turn and drive the motor until **The camera cannot see the block**
Return the Steering motor to its original positon and keep moving ahead


**Ultrasonic Sensor Wall Follow PID**: This block is responsible to keep the robot driving straight with respect to the deviation of the robot from both the side walls.  We’ll be using 2 sensors, 1 on left and the other on right for better accuracy. The calculation goes as follows:
Left Ultrasonic Sensor’s current reading – Right Ultrasonic Sensor’s current reading  = Current Error
(Current Error – Previous Error) * 0.5 = magnified final value (The value 0.5 needs to be tuned with respect to each robot)
This final value needs to be passed to the Steering motor’s power
Assign the previous error value as the current error value



# Construction
In the initial phase of our design, we focused on selecting lightweight yet sturdy components to ensure our robot met the desired balance of strength and weight. Our first iteration featured a **3D-printed chassis** and a steering mechanism made from **LEGO parts**. However, this design had limitations as the integration of LEGO parts with the 3D-printed chassis was **unreliable, and the overall structure was too bulky and heavy.** 

For the second iteration, we shifted to a **fully 3D-printed design**, including the steering mechanism. This resolved many of the issues from the previous version. The **meshing** of the 3D-printed gears and steering components was **precise**, but we encountered challenges in assembling the components as some parts didn't align perfectly, and reprinting components was time-consuming.

In the third iteration, we opted for a **fully LEGO-based chassis**, since we had already achieved a perfect gear mesh with our custom 3D-printed gears and racks, we integrated them into this new design. For the rear wheel motor, we relied on **LEGO gears**, while the steering mechanism used a **custom 3D-printed gear** that matched perfectly with the **custom 3D-printed rack**, providing the best of both worlds.

Our bot measures **16.5 cm in length, 16 cm in width, and 24 cm in height, with a total weight of 1.2 kg**. It is powered by **two medium motors**: one dedicated to driving the rear wheels and the other for the steering mechanism. The **rear wheels (62.4 x 20s)** are mounted on a single axle and connected to the motor through LEGO gears. The **steering wheels (62.3 x 21s)** are mounted on a single axle and connected to the motor, with the steering system meshing seamlessly with a custom 3D-printed gear and rack. The bot is equipped with **two LEGO ultrasonic sensors**, one on each side, and a **gyro sensor** mounted on top. For obstacle detection, we integrated a **Pixy 2.1 camera**. The entire system is powered by a **LEGO Mindstorms EV3 brick**.

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
### Rack & Gear
We designed a **custom 7.2 cm rack** with a similar **groove pattern** and design as the standard **6.4 cm LEGO rack**. The original 6.4 cm LEGO rack had some problems wherein its shorter length made it **difficult to mesh smoothly** with the **20-tooth double bevel black LEGO gear**, which restricted the wheels from achieving **specific steering angles**. 
However, even with our 7.2 cm rack, we encountered a minor issue: the grooves of the black LEGO gear and our custom rack weren’t perfectly meshing. While it functioned temporarily, the meshing wasn't ideal, and the **error compounded by 0.01 with each turn**. To overcome this, we also created a **custom 12 tooth gear** whose grooves are perfectly meshing with custom rack thus **eliminating meshing errors** and significantly **improved the accuracy of the steering**, allowing the wheels to turn at precise angles.
