import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class ServiceServerNode(Node):
    def __init__(self):
        super().__init__('service_server_node')
        self.srv = self.create_service(JointState, 'joint_service', self.service_callback)

    def service_callback(self, request, response):
        total = request.x + request.y + request.z
        if total >= 0:
            response.valid = True
        else:
            response.valid = False
        self.get_logger().info(f'Service request: x={request.x}, y={request.y}, z={request.z}. Response: valid={response.valid}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServiceServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

