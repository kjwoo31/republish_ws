#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from nav_msgs.msg import *
from sensor_msgs.msg import *
from geometry_msgs.msg import *
from visualization_msgs.msg import *

class FakePublish:
  def __init__():
      # Publishers
      self.state_pub = rospy.Publisher("/detector/state",String,queue_size=1)
      self.pose_array_pub = rospy.Publisher("/detector/pose_array",PoseArray,queue_size=1,latch=True)
      self.bbox_pub = rospy.Publisher("/detector/bbox_lines", Marker, queue_size=1)

      # Subscribers
      rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)
      rospy.Subscriber('map', String, self.map_callback)

    def image_callback(self, msg):
        with self.img_lock:
            try:
                self.cv_rgb_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            except CvBridgeError as e:
                print("CVBridgeError!!!")

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

if __name__ == '__main__':
    rospy.init_node('fake_publisher')

    # Subscriber
    rospy.Subscriber('map', String, map_callback)
    
    # Publisher
    pub = rospy.Publisher('chatter', String, queue_size=10)

    while not rospy.is_shutdown():
        pub.publish(hello_str)
