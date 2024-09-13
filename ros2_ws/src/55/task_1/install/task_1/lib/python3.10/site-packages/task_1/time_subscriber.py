import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class TimeSubscriberNode(Node):
    def __init__(self):
        super().__init__('time_subscriber_node')
        self.subscription = self.create_subscription(
            Float64,
            'my_first_topic',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        original_value = msg.data
        doubled_value = 2 * original_value
        self.get_logger().info(f'Received: {original_value:.2f}, Doubled: {doubled_value:.2f}')

def main(args=None):
    rclpy.init(args=args)
    time_subscriber_node = TimeSubscriberNode()
    rclpy.spin(time_subscriber_node)
    time_subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
