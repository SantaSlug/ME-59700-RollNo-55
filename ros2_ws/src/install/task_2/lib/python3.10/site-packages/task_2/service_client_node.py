import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class ServiceClientNode(Node):
    def __init__(self):
        super().__init__('service_client_node')
        self.cli = self.create_client(JointState, 'joint_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.request = JointState.Request()
        self.make_request()

    def make_request(self):
        self.request.x = 1.0
        self.request.y = -0.5
        self.request.z = 0.2
        self.future = self.cli.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            response = self.future.result()
            self.get_logger().info(f'Response: valid={response.valid}')
        else:
            self.get_logger().error('Service call failed')

def main(args=None):
    rclpy.init(args=args)
    node = ServiceClientNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

