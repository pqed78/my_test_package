from launch import LaunchDescription
from launch_ros.actions import Node

def generate_laucnch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
            )
    ])