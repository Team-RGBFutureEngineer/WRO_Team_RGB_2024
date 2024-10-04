# Programming Timeline
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

### Challenges Faced

- **Inaccurate Turn Detection with Ultrasonic Sensors** - We encountered difficulties in detecting turns accurately due to the ultrasonic sensors occasionally providing false or inconsistent readings. 
- **Maintaining a Straight Path Using Gyro PID** - Keeping the robot moving straight using Gyro PID control was challenging, especially when small disturbances caused the robot to drift.

### Resolutions

- We improved sensor accuracy by **filtering out** erratic values using an **averaging** method or by setting specific **thresholds** to disregard outliers. This helped the robot make more consistent decisions about when to turn.
- We tuned the **PID values** carefully to minimize drift and oscillations, ensuring the robot maintained a **stable straight path** over the course of the laps.

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

### Challenges Faced

- **Turning Without Collisions** - While making turns to avoid obstacles, we struggled to prevent the robot from colliding with objects or walls, as its turns were not always smooth or precise.
- **U-turn Logic and Block Detection** - Detecting blocks accurately for U-turn decisions posed difficulties. At times, the camera struggled to recognize blocks, leading to inconsistent U-turn execution.

### Resolutions

- We refined the **robot's turn logic**, adjusting the speed and timing of the turns to give it enough clearance from obstacles. We also used the **Gyro Sensor** to ensure smoother and more controlled turns.
We improved the **Pixy Camera’s** block detection by **fine-tuning** the camera’s **sensitivity** and ensuring the block's area was correctly calculated. This allowed the robot to make reliable **U-turn** decisions based on the **detected block color**.

## Pixy Camera Detection

The Pixy camera utilizes color-based object detection and assigns specific identifiers based on the detected object's color and type. The classification scheme operates as follows:

### 1. Blocks:
![greendetect](https://github.com/user-attachments/assets/8f2c7d68-ca96-41a7-9d9c-b52147d2e406)

- **Green** - Represented as **'G'**, these objects are recognized as blocks with a green hue.

![reddetect](https://github.com/user-attachments/assets/7ab89ed4-b708-4361-9521-fa06b9877806)

- **Red** - Represented as **'R'**, these objects are recognized as blocks with a red hue.
  
### 2. Lines:
![OrangeDetect](https://github.com/user-attachments/assets/fd4d97a4-ac7c-4d99-a3c3-51dfee903838)

- **Orange** - Represented as **'O'**, these objects are identified as lines with an orange hue.
![BlueDetect](https://github.com/user-attachments/assets/c2076157-f3e7-4132-a2b4-1e8b9f42cf15)

- **Blue** - Represented as **'B'**, these objects are identified as lines with a blue hue.

### 3. Parking Wall:
![parkingDetect](https://github.com/user-attachments/assets/d899cf96-7838-4987-9f85-3f9a7fc24d0f)

- **Magenta** - Represented as **'M'**, this object type indicates a parking wall with a magenta hue.


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
