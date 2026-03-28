import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool, String
import time

class RecoveryNode(Node):
    """
    Otonom Kurtarma Davranışları (Recovery Behaviors) Modülü.
    Rover sıkıştığında veya teknik arıza durumunda devreye girer.
    """
    def __init__(self):
        super().__init__('recovery_node')
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.status_sub = self.create_subscription(
            String, 'system_fault', self.fault_callback, 10
        )
        self.get_logger().info('Otonom Kurtarma Modülü Aktif. Beklemede.')

    def fault_callback(self, msg):
        if msg.data == 'STUCK_IN_REGOLITH':
            self.shake_to_clear()
        elif msg.data == 'OVERHEATING':
            self.thermal_safe_drift()

    def shake_to_clear(self):
        """Regolitte sıkışma durumunda tekerlekleri titreterek kurtulma manevrası."""
        self.get_logger().warn('Manevra Başlatılıyor: ShakeToClear (Regolitten Kurtulma)')
        twist = Twist()
        for _ in range(5):
            twist.angular.z = 1.0; self.cmd_pub.publish(twist); time.sleep(0.2)
            twist.angular.z = -1.0; self.cmd_pub.publish(twist); time.sleep(0.2)
        twist.angular.z = 0.0; self.cmd_pub.publish(twist)

    def thermal_safe_drift(self):
        """Aşırı ısınma durumunda rover'ı gölgeye veya güvenli açıya sürükleme."""
        self.get_logger().warn('Manevra Başlatılıyor: ThermalSafeDrift (Termal Koruma)')
        # Basitçe geri gitme ve pasif soğuma moduna geçiş
        twist = Twist()
        twist.linear.x = -0.1
        self.cmd_pub.publish(twist)
        time.sleep(2.0)
        twist.linear.x = 0.0
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RecoveryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
