import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericTalker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.numericPublisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.numericTimer = self.create_timer(timer_in_seconds, self.numeric_talker_callback)
        self.counter = 0
        self.numericCounter = 0

        
    def talker_callback(self):
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.counter += 1
        

    def numeric_talker_callback(self):
        msgNT = Int8()
        msgNT.data = self.numericCounter
        self.numericPublisher.publish(msgNT)
        self.get_logger().info(f'Publishing: {str(msgNT.data)}')
        self.numericCounter += 1
        self.numericCounter = self.numericCounter % 128


def main(args=None):
    rclpy.init(args=args)

    numericTalker = NumericTalker()
    rclpy.spin(numericTalker)


if __name__ == '__main__':
    main()


