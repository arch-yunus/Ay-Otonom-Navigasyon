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

## 4. Simulation Environment
The `sim/` folder provides Gazebo configurations for the **Shackleton Crater** region, accounting for:
-   $1/6g$ Gravity.
-   Regolith soil modeling.
-   Low-angle lighting conditions.
