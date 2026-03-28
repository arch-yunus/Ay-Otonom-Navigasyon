# Technical Specifications: Ay-Otonom-Navigasyon

## 1. Software Stack
| Component | Implementation | Version/Metric |
| :--- | :--- | :--- |
| Core Language | Python | 3.10+ |
| Middleware | ROS2 | Humble / Foxy |
| Math Engine | NumPy / SciPy | Industrial Grade |
| Local Planner | DWA | 10Hz Update Rate |
| Global Planner | A* | Multi-constaint (Energy/Slope) |

## 2. Hardware Compatibility (Validated)
- **Primary LiDAR:** Ouster OS1-64 or Velodyne VLP-16.
- **Stereo Vision:** Intel RealSense D435i (Radiation-hardened casing recommended).
- **IMU:** Bosch BNO055 or high-precision Honeywell HG1120.
- **Compute:** NVIDIA Jetson Orin (Edge Computing) or Radiation-Hardened Xilinx FPGA.

## 3. Physics Constraints
- **Gravity:** $1.622 m/s^2$
- **Regolith Cohesion:** 0.1 to 1.0 kPa
- **Min Operating Temp:** -230°C (with thermal heaters)
- **Max Operating Temp:** +120°C (with radiator fins)

## 4. Communication Latency
| Link Type | Distance | Latency (Typical) |
| :--- | :--- | :--- |
| Earth-Moon (Distant) | 384,400 km | 1.28 s (one-way) |
| Local Mesh (Rover-to-Rover) | < 5 km | < 10 ms |
