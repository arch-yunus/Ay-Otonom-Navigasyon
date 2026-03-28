import numpy as np

class ExtendedKalmanFilter:
    """
    Non-linear State Estimation for Lunar Rovers.
    States: [x, y, z, roll, pitch, yaw, vx, vy, vz]
    """
    def __init__(self, dt=0.1):
        self.dt = dt
        self.x = np.zeros(9)
        self.P = np.eye(9) * 0.1
        self.Q = np.eye(9) * 0.01
        self.R = np.eye(3) * 0.1 # Observation noise (for xyz)

    def predict(self, u):
        """Standard EKF prediction step using a constant-velocity model."""
        # Simple transition matrix (F)
        F = np.eye(9)
        F[0, 6] = self.dt
        F[1, 7] = self.dt
        F[2, 8] = self.dt
        
        self.x = F @ self.x + u
        self.P = F @ self.P @ F.T + self.Q
        return self.x

    def update(self, z):
        """Update step using absolute measurements (e.g. from Crater Matcher)."""
        H = np.zeros((3, 9))
        H[0:3, 0:3] = np.eye(3)
        
        y = z - H @ self.x # Innovation
        S = H @ self.P @ H.T + self.R # Innovation covariance
        K = self.P @ H.T @ np.linalg.inv(S) # Kalman gain
        
        self.x = self.x + K @ y
        self.P = (np.eye(9) - K @ H) @ self.P
        return self.x
