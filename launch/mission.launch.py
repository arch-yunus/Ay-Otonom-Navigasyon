from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """Generates a ROS2 launch description for the lunar navigation mission."""
    params_file = os.path.join(
        'g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/Ay-Otonom-Navigasyon/config', 
        'params.yaml'
    )

    return LaunchDescription([
        Node(
            package='ay_otonom_navigasyon',
            executable='perception_node',
            name='perception',
            parameters=[params_file]
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='navigation_node',
            name='navigation',
            parameters=[params_file]
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='estimation_node',
            name='estimator',
            parameters=[params_file]
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='mission_manager',
            name='manager',
            parameters=[params_file]
        )
    ])
