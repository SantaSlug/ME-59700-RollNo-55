import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time

class TimePublisherNode(Node):
    def __init__(self):
        super().__init__('time_publisher_node') #Node name is "time_publisher_node"
        
        # Publisher setup
        self.publisher = self.create_publisher(Float64, 'my_first_topic', 10)
        
        # Setting the publishing frequency (10 Hz)
        self.timer_period = 1.0 / 10  # 0.1 seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        # Time when node started
        self.start_time = time.time()
        self.get_logger().info('Time Publisher Node has been started.')
        
    def timer_callback(self):
        elapsed_time = time.time() - self.start_time
        msg = Float64()
        msg.data = elapsed_time
        
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data:.2f} seconds')

def main(args=None):
    rclpy.init(args=args)
    
    time_publisher_node = TimePublisherNode()
    
    rclpy.spin(time_publisher_node)
    
    # Clean up on exit
    time_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
