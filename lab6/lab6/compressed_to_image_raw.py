import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge, CvBridgeError
import cv2
# TODO: you need to import CompressedImage from sensor_msgs.msg
# TODO: you need to import Image from sensor_msgs.msg


class CompressedImageConverter(Node):
    def __init__(self):
        super().__init__('compresed_to_image_raw')
        self.logger = self.get_logger()
        self.first_frame_published = False
        self.bridge = CvBridge()

        # TODO: create a new subscription:
        # 1. The message type will be CompressedImage.
        # 2. The topic is /camera/image/compressed
        # 3. The callback will be self.image_callback
        # 4. You can choose a queue size of 10

        # TODO: create a new publisher:
        # 1. The message type will be Image
        # 2. The topic name should be /camera/image_raw
        # 3. You can choose a queue size of 10

    def image_callback(self, msg):
        # This if statement is to simply check if we have received at least one
        # frame and published an image_raw once (we don't need to print it for
        # every frame received). It would help in the future, to debug, should
        # networking issues arise. When you run this node, you should look for
        # that info message in your terminal to verify that the subscriber
        # received at least a message (and therefore there is no issue with
        # networking).
        if not self.first_frame_published:
            self.logger.info('Started converting compressed image to image raw ...')
            self.first_frame_published = True

        try:
            # TODO: cv_image = ...
            # use the compressed_imgmsg_to_cv2 method of self.bridge to 
            # convert a compressed image to a normal cv2 image. Pass in "msg" 
            # to the method.

            # TODO: we still work with CV image, let's convert it to ROS image:
            # image_message = ....
            # use the cv2_to_imgmsg method of self.bridge to do this. You need
            # to provide 2 arguments: the cv_image and the "bgr8" string

            # TODO: now simply publish the image_message using your publisher.

        except CvBridgeError as e:
            print(f'Could not convert image: {e}')


def main():
    rclpy.init(args=None)
    image_converter = CompressedImageConverter()
    rclpy.spin(image_converter)


if __name__ == "__main__":
    main()
