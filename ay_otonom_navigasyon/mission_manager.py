import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Twist
import time

class MissionManager(Node):
    """
    Finite State Machine (FSM) for Lunar Mission Coordination.
    States: IDLE, PLANNING, EXECUTING, HAZARD_RECOVERY
    """
    def __init__(self):
        super().__init__('mission_manager')
        self.state = 'IDLE'
        self.publisher_ = self.create_publisher(String, 'mission_state', 10)
        self.timer = self.create_timer(1.0, self.state_callback)
        self.get_logger().info('Mission Manager Initialized. State: IDLE')

    def state_callback(self):
        msg = String()
        msg.data = self.state
        self.publisher_.publish(msg)

    def transition_to(self, new_state):
        self.get_logger().info(f'Transitioning from {self.state} to {new_state}')
        self.state = new_state

def main(args=None):
    rclpy.init(args=args)
    node = MissionManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
