# Technical Architecture: Ay-Otonom-Navigasyon

## 1. Localization & Mapping (SLAM)
The navigation stack utilizes a hybrid localization approach:
-   **Primary:** LiDAR-based SLAM for local obstacle avoidance.
-   **Secondary:** Terrain Relative Navigation (TRN) using crater patterns for global drift correction.

## 2. Path Planning Strategy
Algorithms are constrained by:
-   **Slope Angles:** Max 20 degrees for safety.
-   **Power Consumption:** Path length vs. terrain difficulty.
-   **Hazard Zones:** Shadows (loss of solar) and steep craters.

## 3. Sensor Fusion (EKF)
The Extended Kalman Filter integrates:
-   Wheel Odometry (Low frequency)
-   IMU (High frequency)
-   Visual Odometry (Stability)
-   Lunar Star Tracker (Absolute Heading)

## 5. Algorithmic Deep-Dive

### A* Path Planning
The `AStarPlanner` implementation utilizes a priority-queue based search with a custom cost function:
$$Cost(n) = g(n) + h(n) \cdot W_{terrain}$$
Where $W_{terrain}$ is derived from the hazard mapping variance, effectively penalizing steep slopes and high-regolith-risk areas.

### EKF Sensor Fusion
The Extended Kalman Filter tracks a 9-DOF state vector:
-   **Position:** $[x, y, z]$
-   **Orientation:** $[roll, pitch, yaw]$
-   **Velocity:** $[v_x, v_y, v_z]$
The prediction step uses a constant-velocity kinematic model, while the update step integrates absolute position fixes from the `CraterDetector` module.

## 6. How to Run (Development)
To verify the navigation logic without a full ROS2 stack:
```bash
python src/test_algorithms.py
```
This script validates the path-finding capability and obstacle avoidance logic in real-time.
