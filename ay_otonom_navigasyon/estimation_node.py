import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from .state_estimation import ExtendedKalmanFilter

class EstimationNode(Node):
    def __init__(self):
        super().__init__('estimation_node')
        self.ekf = ExtendedKalmanFilter()
        self.publisher_ = self.create_publisher(Odometry, 'odom_filtered', 10)
        self.get_logger().info('State Estimation Node Started.')

def main(args=None):
    rclpy.init(args=args)
    node = EstimationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
