import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist
from .navigation import AStarPlanner, RoverController

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.planner = AStarPlanner()
        self.controller = RoverController()
        self.subscription = self.create_subscription(
            PoseStamped, 'goal_pose', self.goal_callback, 10
        )
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info('Navigation Node Started.')

    def goal_callback(self, msg):
        self.get_logger().info('Received new mission goal.')
        # Trigger A* planning and controller execution

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
