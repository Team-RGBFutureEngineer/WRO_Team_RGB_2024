# Team RGB – WRO Future Engineers 2024



We are **Team RGB**, a duo of engineering students from **RFL Academy**, united by our passion for **Robotics**. We have clearly divided our roles to maximize our strengths:

**Bhavya Sanghrajka – Lead Programmer & Electronics**: Bhavya is responsible for the robot's programming and electronics systems. He specializes in developing advanced control algorithms, including PID control, and designing the logic that powers the robot’s movements and decision-making. Bhavya ensures the seamless integration of sensors and motors, programming the robot to execute precise maneuvers for both the open-round and obstacle-round. 

**Raj Kothari – Lead Designer & Constructor**: Raj is responsible for the structural and mechanical design of the robot. With a focus on precision and functionality, he uses CAD software to create a robust and lightweight design that adheres to the competition’s strict dimension and weight restrictions. Raj specializes in optimizing the integration of LEGO components with custom-designed parts, ensuring the robot performs reliably in both maneuverability and stability under competition conditions.

**Sahil Gajera - Mentor**:  A computer engineer by profession, Sahil sir is a robotics and linux enthusiast. His experience in First Robotics Competition (FRC) has helped us a lot in this entire joureny of Future Engineer category. 

# Construction Timeline

## First Iteration

![Iteration 1](https://github.com/user-attachments/assets/653f6a88-978d-4fd7-a753-c714621104b3)


In the **Initial phase** of our design, we prioritized selecting lightweight yet durable components to ensure the robot maintained an optimal balance between strength and weight. Our first iteration featured a **3D-printed chassis** combined with a **steering mechanism** constructed from **LEGO parts**. However, this design presented several limitations, as the integration of the LEGO components with the 3D-printed chassis proved unreliable, and the overall structure became too bulky and heavy.

**Strengths**
- **Lightweight and Durable Focus** - Prioritizing lightweight yet durable components ensured that the robot had an optimal balance between strength and weight, which is essential for performance.
- **Customization Options** - Using a 3D-printed chassis allowed for high levels of customization, enabling us to explore innovative design possibilities.

**Weakness**
- **Structural Instability** - Integration of LEGO components with 3D-printed parts lacked mechanical stability, leading to weak points in the structure.
- **Bulky Design** - The overall structure became too bulky and heavy, which negated the initial focus on lightweight components.

**Opportunities**
- **Material Optimization** - Explore alternative 3D printing materials or geometries (e.g., honeycomb structures) to reduce weight without compromising durability.
- **Enhanced Modular Design** - Refining the integration of modular components (e.g., steering mechanisms) could improve adaptability and reduce structural issues in future iterations.

**Threats**
- **Performance Limitations** - The bulky and unreliable design could limit the robot’s performance, particularly in speed, maneuverability, and battery efficiency.
- **Time and Resource Constraints** - Continuous redesigns or modifications to address the weaknesses could impact project timelines and require additional resources.

## Second Iteration

![Iteration 2](https://github.com/user-attachments/assets/3209f422-feb9-4308-bdc3-57603cd147a6)


For the **Second iteration**, we transitioned to a **fully 3D-printed design**, including the steering mechanism. This solved many of the issues encountered in the previous version. The meshing of the **3D-printed gears** and steering components was precise. However, we faced challenges in aligning some parts during assembly, and reprinting components was **time-consuming** when adjustments were needed.

**Strengths**
- **Fully 3D-Printed Design** - Transitioning to a fully 3D-printed design, including the steering mechanism, resolved many integration issues from the previous iteration.
- **Precision in Gear Meshing** - Full control over gear design allowed for highly accurate meshing between 3D-printed gears and steering components, minimizing backlash and increasing mechanical efficiency.

**Weakness**
- **Assembly Complexity** - Alignment challenges arose during assembly, as 3D-printed components lacked built-in tolerances, making precise fitting of parts difficult.
- **Reprinting Delays** - Adjustments or design modifications required lengthy reprints, which increased downtime and reduced iteration speed.

**Opportunities**
- **Improved Assembly Process** - Refining the design for easier alignment during assembly could streamline the building process and reduce errors.
- **Iterative Refinement** - With continued iterations, the 3D-printed design could become more efficient and quicker to produce, especially by fine-tuning the parts for better fit.

**Threats**
- **Time Constraints** - The need to frequently reprint parts for adjustments could significantly impact project timelines, especially if iterations are slow.
- **Dimensional Inaccuracies** - Printer calibration or material expansion during cooling could lead to dimensional inaccuracies, affecting part performance and requiring reprints.

## Final Iteration

![LEGO CAD](https://github.com/user-attachments/assets/643c7b24-d85f-4893-a01c-d619c50e29b4)


In the **Third iteration**, we opted for a **fully LEGO-based chassis**. Given that we had already achieved a precise gear mesh using custom **3D-printed gears and racks**, we integrated these components into the new design. The rear wheel motor relied on LEGO gears, while the steering mechanism utilized a custom 3D-printed gear perfectly matched with a custom 3D-printed rack, offering the best combination of customization and reliability.

**Strengths**
- **Fully 3D-Printed Design** - Transitioning to a fully 3D-printed design, including the steering mechanism, resolved many integration issues from the previous iteration.
- **Precision Gear Integration** - The combination of custom 3D-printed gears and racks with LEGO components resulted in highly precise gear meshing, minimizing mechanical losses and maximizing drive efficiency.

**Weakness**
- **Design Flexibility Limitations** - While the LEGO chassis offered modularity, it imposed constraints on component arrangement and customization compared to a fully 3D-printed or custom design.
- **Potential Compatibility Issues** - Integrating 3D-printed components with LEGO parts introduced potential alignment and mechanical fit challenges that could affect reliability over time.

**Opportunities**
- **Hybrid System Optimization** - Further optimization of the hybrid LEGO-3D printed design could lead to increased system robustness, combining the strengths of both approaches (e.g., modularity of LEGO, precision of custom parts).
- **Enhanced Design Modularity** - Expand modularity by developing interchangeable 3D-printed parts compatible with LEGO, facilitating quick upgrades or repairs without major redesigns.

**Threats**
- **Component Wear and Tear** - Over time, the wear on LEGO gears and 3D-printed parts could affect performance, requiring maintenance or replacement of key components.
- **Structural Limitations** - LEGO's inherent structural limitations could impact the robot's ability to handle heavy loads or more demanding tasks, potentially hindering further scaling or robustness improvements.

# Custom 3D Printed Parts
## Rack & Gear
![rack](https://github.com/user-attachments/assets/8095da94-c97d-4a3a-9b54-2e79d7d563b5)
![gear](https://github.com/user-attachments/assets/e8f77b26-07b3-4e20-b14b-a0db9464e79c)

We designed a **custom 7.2 cm rack** with a similar **groove** pattern and design as the standard **6.4 cm LEGO rack**. The original 6.4 cm LEGO rack had some problems wherein its shorter length made it difficult to mesh smoothly with the **20-tooth double bevel black LEGO gear**, which restricted the wheels from achieving specific steering angles.

However, even with our 7.2 cm rack, we encountered a minor issue: the grooves of the black LEGO gear and our custom rack weren’t perfectly meshing. While it functioned temporarily, the meshing wasn't ideal, and the **error compounded by 0.01 with each turn**. To overcome this, we also created a **custom 12 tooth gear** whose grooves are **perfectly meshing** with custom rack thus eliminating meshing errors and significantly improved the accuracy of the steering, allowing the wheels to turn at **precise angles**.

**Strengths**
- **Improved Rack Design** - The custom 7.2 cm rack, designed to replicate the LEGO rack's groove pattern, provided better meshing with the LEGO gear, reducing initial steering issues and improving maneuverability.
- **Enhanced Steering Precision** - The development of a custom 12-tooth gear that perfectly meshed with the custom rack eliminated alignment issues, significantly improving the steering accuracy and control.

**Weakness**
- **Initial Misalignment Issues** - Despite the improvement with the custom rack, the minor alignment issue between the grooves of the LEGO gear and custom rack introduced a small cumulative error (0.01 degrees), which reduced precision over time.
- **Complex Manufacturing** - The creation of custom racks and gears requires precision manufacturing (likely 3D printing), which can be time-consuming and requires access to specialized equipment for accurate results.

**Opportunities**
- **Optimized Custom Components** - Further refinement of custom components, such as varying tooth profiles or gear materials, could increase durability, precision, and overall performance in steering and navigation systems.

**Threats**
- **Component Wear and Tear** - Over time, custom 3D-printed components may wear down faster than standard LEGO parts, introducing alignment or meshing issues, which could degrade steering accuracy.
- **Component Compatibility** - Relying on custom gears and racks introduces the risk of incompatibility with other standard LEGO components, potentially limiting future upgrades or repairs using off-the-shelf LEGO parts.


## Pixy Mount & Beam
![pixy mount and beam](https://github.com/user-attachments/assets/d1139705-3865-4015-92a2-d88d2dcb0b4b)

During the robot’s journey, we encountered **instability with the Pixy camera**, which frequently shifted and struggled to accurately detect objects. To address this issue and secure the Pixy at a precise angle, we 3D-printed two custom components.

First, we created a **custom beam** that perfectly aligned with the **holes of the H-frame**, enabling us to securely attach the Pixy to the connector. Additionally, we designed a **custom mount** to provide further support and stability for the Pixy camera.

Both the beam and the Pixy mount were connected using **3 mm screws**, allowing for easy adjustment and locking of the camera at the **desired angle**. This setup ensured that the Pixy could consistently scan and detect objects with accuracy, especially during the obstacle round challenge.

**Strengths**
- **Improved Camera Stability** - The custom 3D-printed beam and mount provided secure, adjustable positioning for the Pixy camera, ensuring accurate object detection and eliminating the instability encountered during movement.
- **Precise Alignment** - The beam design was tailored to align perfectly with the holes of the H-frame, facilitating a secure connection and stable support for the Pixy, improving its performance during the obstacle challenge.

**Weakness**
- **Complex Assembly** - The custom setup, involving 3 mm screws and custom components, added complexity to the assembly process and may require careful calibration to achieve the optimal camera angle.
- **Potential Adjustability Limitations** - While the camera can be adjusted, any significant design changes in future iterations may require reprinting the custom components, introducing delays in development.

**Opportunities**
- **Modular Design Improvements** - Refining the 3D-printed mount and beam to be modular or flexible could allow for easier adjustments, enabling the camera to adapt to different angles or robot configurations.
- **Enhanced Object Detection** - The secure and precise positioning of the Pixy camera opens the possibility for improved computer vision or AI-driven detection algorithms, leading to better object recognition and navigation accuracy.

**Threats**
- **Component Durability** - Over time, the 3D-printed beam and mount may experience wear, especially if frequent adjustments are made, potentially leading to loosening or misalignment that affects detection accuracy.

## Our Robot

![lego with dimensions](https://github.com/user-attachments/assets/b4a35bbf-7c4b-40c1-873d-20524598dfb4)


Our robot measures **16.5 cm in length, 16 cm in width, and 24 cm in height**, with a total weight of **0.9 kg**. It is powered by **two medium motors**—one dedicated to driving the rear wheels and the other for controlling the steering mechanism. The rear wheels (62.4 x 20s) are mounted on a **single axle** and connected to the motor via LEGO gears. The steering wheels (62.3 x 21s) are also mounted on a single axle and connected to the motor, with the steering system operating through the custom 3D-printed gear and rack, ensuring smooth and precise movement.

The robot is equipped with two **LEGO ultrasonic sensors**, mounted on both left & right side, and a **gyro sensor** placed on top for navigation. For obstacle detection, we integrated a **Pixy 2.1 camera**. The entire system is powered by a **LEGO Mindstorms EV3 brick**, which manages the control and coordination of the sensors and motors. 

- **Turning Radius of our robot is 75 degree**
- **Centre Distance between both wheels is 11 cm** 


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

## Conclusion

The robot's construction and programming are optimized for high precision and efficiency, tailored to meet the requirements of both the Open Round and Obstacle Round challenges. 

### Construction

The robot’s compact size **(16.5 cm x 16 cm x 24 cm) and light weight (0.9 kg)** ensure a balance of agility and stability. Powered by two medium LEGO motors, it controls rear-wheel propulsion and steering through a custom 3D-printed gear and rack system. Equipped with LEGO ultrasonic sensors, a gyro sensor, and a Pixy 2.1 camera, the robot effectively detects obstacles and navigates the course, including parking walls, with precision.

### Open Round Challenge

In the Open Round, the program uses Ultrasonic Sensors and Gyro PID control to maintain alignment and execute precise turns. The robot detects missing walls **(sensor reading >80)** and turns left or right based on sensor data. With the Gyro sensor ensuring accuracy, the robot completes **12 turns over 3 laps in 65 seconds**, efficiently navigating using optimized sensor feedback.

### Obstacle Round Challenge

In the Obstacle Round, the Pixy 2.1 camera detects colored blocks and lines, prompting the robot to turn based on the block color **(right for red, left for green)**. It continuously checks for blue or orange lines to adjust its direction, storing detected data in an array to guide decisions, including **U-turns after 8 turns**. The round concludes with the robot searching for a magenta parking area and using motor encoder values to park precisely. The entire Obstacle Round, **including parking, is completed in 140 seconds.**

# Video Links
## Link Tree
https://linktr.ee/rgbfe2024
## Open Round Challenge
**Youtube** - https://youtu.be/_w3JlFxCa_E?si=RLct2GLcysBRvsGL
## Obstacle Round Challenge
**Youtube** - https://youtu.be/dA7stuY_RsI
