# Iterations
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
