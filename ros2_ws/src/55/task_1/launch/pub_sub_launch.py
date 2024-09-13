import launch
import launch.actions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='task_1',
            executable='talker',
            name='time_publisher_node',
            output='screen',
            parameters=[],
        ),
        launch_ros.actions.Node(
            package='task_1',
            executable='listner',
            name='time_subscriber_node',
            output='screen',
            parameters=[],
        ),
    ])
