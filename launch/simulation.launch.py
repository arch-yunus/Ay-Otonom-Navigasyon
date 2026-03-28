from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """Commander-Class Simülasyon Launch Yapılandırması."""
    return LaunchDescription([
        Node(
            package='ay_otonom_navigasyon',
            executable='mission_manager',
            name='mission_manager_node'
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='perception_node',
            name='perception_node'
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='navigation_node',
            name='navigation_node'
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='telemetry_node',
            name='telemetry_node'
        ),
        Node(
            package='ay_otonom_navigasyon',
            executable='fdir_node',
            name='fdir_watchdog'
        )
    ])
