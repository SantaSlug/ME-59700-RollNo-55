import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(JointData, 'joint_topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = JointData()
        msg.center.x = float(self.i)  # Ensure this is a float
        msg.center.y = float(self.i)  # Ensure this is a float
        msg.center.z = 0.0  # This is already a float
        msg.vel = 1.0  # This is already a float
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: center=({msg.center.x}, {msg.center.y}), vel={msg.vel}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
