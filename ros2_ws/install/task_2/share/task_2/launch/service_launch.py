from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='task_2',
            executable='service_server_node',
            name='service',
            output='screen',
        ),
        Node(
            package='task_2',
            executable='publisher_node',
            name='talker',
            output='screen',
        ),
    ])
