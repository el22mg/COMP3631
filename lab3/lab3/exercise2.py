import threading
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.exceptions import ROSInterruptException
import signal


class ThirdWalker(Node):
    def __init__(self):
        super().__init__('thirdwalker')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.rate = self.create_rate(10)  # 10 Hz

    def walk_square(self):
        desired_velocity = Twist()
        
        for _ in range(4): # For loops, each traversing one side and rotating 90 degrees
            
            desired_velocity.linear.x = 0.5 # Forward at 0.5 m/s
        
            for _ in range(40): # Walk distance
                self.publisher.publish(desired_velocity)
                self.rate.sleep()
         
            desired_velocity.linear.x = 0.0 # Stop traversing in order to rotate
            desired_velocity.angular.z = 0.314159256 # Rotate anticlockwise at 0.314149256 rad/s (non-integer factor of pi/2, allowing rotation of exact right angle)
            
            for _ in range(50): # Rotating until 90 degree turn achieved (50 sleeps = 5 seconds)
                self.publisher.publish(desired_velocity)
                self.rate.sleep()
                
            desired_velocity.angular.z = 0.0 # Stop rotating
        
    

    def stop(self):
        desired_velocity = Twist()
        desired_velocity.linear.x = 0.0  # Send zero velocity to stop the robot
        self.publisher.publish(desired_velocity)
        

def main():
    def signal_handler(sig, frame):
        third_walker.stop()
        rclpy.shutdown()

    rclpy.init(args=None)
    third_walker = ThirdWalker()

    signal.signal(signal.SIGINT, signal_handler)
    thread = threading.Thread(target=rclpy.spin, args=(third_walker,), daemon=True)
    thread.start()

    try:
        while rclpy.ok():
            third_walker.walk_square()
    except ROSInterruptException:
        pass


if __name__ == "__main__":
    main()


