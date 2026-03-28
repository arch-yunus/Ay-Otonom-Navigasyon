import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from .perception import CraterDetector, HazardMapper

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.detector = CraterDetector()
        self.mapper = HazardMapper()
        self.subscription = self.create_subscription(
            PointCloud2, 'lidar_points', self.lidar_callback, 10
        )
        self.get_logger().info('Perception Node Started.')

    def lidar_callback(self, msg):
        # Implementation of point cloud processing
        pass

def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
