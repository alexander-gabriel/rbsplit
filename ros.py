import rospy
from sensor_msgs.msg import Image
from rosgraph_msgs.msg import Clock
from threading import Thread


class Ros(Thread):

    def __init__(self, callback):
        self.parent_callback = callback
        rospy.init_node("rbsplit")
        #rospy.Subscriber("/zed/left/image_rect_color", Image, self.timestamp_callback)
        rospy.Subscriber("/clock", Clock, self.time_callback)
        rospy.loginfo("rbsplit online")


    def time_callback(self, data):
        self.parent_callback(data)

    def run():
        rospy.spin()
