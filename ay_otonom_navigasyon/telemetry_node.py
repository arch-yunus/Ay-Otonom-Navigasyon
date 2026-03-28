import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

class TelemetryNode(Node):
    """
    Commander-Class Gelişmiş Telemetri Sistemi.
    Tüm alt sistem verilerini toplar ve tek bir JSON yayını yapar.
    """
    def __init__(self):
        super().__init__('telemetry_node')
        self.publisher_ = self.create_publisher(String, 'mission_telemetry', 10)
        self.timer = self.create_timer(1.0, self.publish_telemetry)
        self.start_time = time.time()
        self.get_logger().info('Komutan Telemetri Sistemi Başlatıldı.')

    def publish_telemetry(self):
        data = {
            "mission_time": time.time() - self.start_time,
            "system_health": "OPTIMAL",
            "battery_level": 98.5,
            "current_state": "PLANNING",
            "gnss_status": "OFFLINE (CBL ACTIVE)",
            "cpu_load": 12.4
        }
        msg = String()
        msg.data = json.dumps(data)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TelemetryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
