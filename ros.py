import rospy
from sensor_msgs.msg import Image


class Ros:

    def __init__(self, callback):
        self.parent_callback = callback
        rospy.init_node("rbsplit")
        rospy.Subscriber("/zed/left/image_rect_color", Image, self.timestamp_callback)
        rospy.loginfo("rbsplit online")
        rospy.spin()

    def timestamp_callback(self, data):
        self.parent_callback(data)
