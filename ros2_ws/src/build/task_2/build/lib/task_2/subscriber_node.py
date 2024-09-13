import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            JointData,
            'joint_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Log the received message data
        self.get_logger().info(
            f'Received: center=({msg.center.x:.2f}, {msg.center.y:.2f}), vel={msg.vel:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
