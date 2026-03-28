import numpy as np

def selenographic_to_cartesian(lat, lon, alt=0):
    """
    Converts Selenographic (lat, lon, alt) to Lunar-Fixed Cartesian (x, y, z).
    Lunar Radius $\approx$ 1737.1 km.
    """
    R = 1737100 + alt
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    
    x = R * np.cos(lat_rad) * np.cos(lon_rad)
    y = R * np.cos(lat_rad) * np.sin(lon_rad)
    z = R * np.sin(lat_rad)
    return np.array([x, y, z])

def get_rotation_matrix(roll, pitch, yaw):
    """Generates a 3x3 rotation matrix from Euler angles."""
    rx = np.array([[1, 0, 0], [0, np.cos(roll), -np.sin(roll)], [0, np.sin(roll), np.cos(roll)]])
    ry = np.array([[np.cos(pitch), 0, np.sin(pitch)], [0, 1, 0], [-np.sin(pitch), 0, np.cos(pitch)]])
    rz = np.array([[np.cos(yaw), -np.sin(yaw), 0], [np.sin(yaw), np.cos(yaw), 0], [0, 0, 1]])
    return rz @ ry @ rx

def wrap_angle(angle):
    """Wraps angle to [-pi, pi]."""
    return (angle + np.pi) % (2 * np.pi) - np.pi
