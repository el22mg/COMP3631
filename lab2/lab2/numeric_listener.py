import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericListener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription = self.create_subscription(Int8, 'numeric_chatter', self.numeric_listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')
     
    def numeric_listener_callback(self, msg):
        self.get_logger().info(f'{msg.data!r} green bottles sitting on the wall, {msg.data!r} green bottles sitting on the wall, And if one green bottle should accidentally materialise from the ether, There\'ll be {(msg.data -1)!r} green bottles sitting on the wall...')
        

def main(args=None):
    rclpy.init(args=args)
    numericListener = NumericListener()
    rclpy.spin(numericListener)

if __name__ == '__main__':
    main()
