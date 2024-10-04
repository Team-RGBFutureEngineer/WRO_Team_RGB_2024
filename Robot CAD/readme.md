# Iterations
### Iteration 1 (IT1)
In the **Initial phase** of our design, we prioritized selecting lightweight yet durable components to ensure the robot maintained an optimal balance between strength and weight. Our first iteration featured a **3D-printed chassis** combined with a **steering mechanism** constructed from **LEGO parts**. However, this design presented several limitations, as the integration of the LEGO components with the 3D-printed chassis proved unreliable, and the overall structure became too bulky and heavy.
### Iteration 2 (IT2)
For the **Second iteration**, we transitioned to a **fully 3D-printed design**, including the steering mechanism. This solved many of the issues encountered in the previous version. The meshing of the **3D-printed gears** and steering components was precise. However, we faced challenges in aligning some parts during assembly, and reprinting components was **time-consuming** when adjustments were needed.
### Final Iteration (FI)
In the **Third iteration**, we opted for a **fully LEGO-based chassis**. Given that we had already achieved a precise gear mesh using custom **3D-printed gears and racks**, we integrated these components into the new design. The rear wheel motor relied on LEGO gears, while the steering mechanism utilized a custom 3D-printed gear perfectly matched with a custom 3D-printed rack, offering the best combination of customization and reliability.

# Custom 3D Printed Parts

## Rack & Gear
We designed a **custom 7.2 cm rack** with a similar **groove** pattern and design as the standard **6.4 cm LEGO rack**. The original 6.4 cm LEGO rack had some problems wherein its shorter length made it difficult to mesh smoothly with the **20-tooth double bevel black LEGO gear**, which restricted the wheels from achieving specific steering angles.

However, even with our 7.2 cm rack, we encountered a minor issue: the grooves of the black LEGO gear and our custom rack weren’t perfectly meshing. While it functioned temporarily, the meshing wasn't ideal, and the **error compounded by 0.01 with each turn**. To overcome this, we also created a **custom 12 tooth gear** whose grooves are **perfectly meshing** with custom rack thus eliminating meshing errors and significantly improved the accuracy of the steering, allowing the wheels to turn at **precise angles**.

## Pixy Mount & Beam

During the robot’s journey, we encountered **instability with the Pixy camera**, which frequently shifted and struggled to accurately detect objects. To address this issue and secure the Pixy at a precise angle, we 3D-printed two custom components.

First, we created a **custom beam** that perfectly aligned with the **holes of the H-frame**, enabling us to securely attach the Pixy to the connector. Additionally, we designed a **custom mount** to provide further support and stability for the Pixy camera.

Both the beam and the Pixy mount were connected using **3 mm screws**, allowing for easy adjustment and locking of the camera at the **desired angle**. This setup ensured that the Pixy could consistently scan and detect objects with accuracy, especially during the obstacle round challenge.

