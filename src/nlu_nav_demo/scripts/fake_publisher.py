#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import *
from nav_msgs.msg import *
from sensor_msgs.msg import *
from geometry_msgs.msg import *
from visualization_msgs.msg import *
from jsk_rviz_plugins.msg import OverlayText

class FakePublish:
    def __init__(self):

      # Define
      self.bbox=None
      self.detectimg=None
      self.trackimg=None
      self.map=None
      self.text=None


      # Publishers
      self.bbox_pub = rospy.Publisher("/detector/bbox_lines", Marker, queue_size=1)
      self.detectimg_pub = rospy.Publisher("/annotated_image", Image, queue_size=1)
      self.trackimg_pub = rospy.Publisher("/tracker/map_image", Image, queue_size=1)
      self.map_pub = rospy.Publisher("/map", OccupancyGrid, queue_size=1)
      self.text_pub = rospy.Publisher("/tracker/text", OverlayText, queue_size=1)

      # Subscribers
      rospy.Subscriber("/detector/bbox_lines", Marker, self.bbox_callback)
      rospy.Subscriber("/annotated_image", Image, self.detectimg_callback)
      rospy.Subscriber("/tracker/map_image", Image, self.trackimg_callback)
      rospy.Subscriber("/map", OccupancyGrid, self.map_callback)
      rospy.Subscriber("/tracker/text", OverlayText, self.text_callback)

    def bbox_callback(self, msg):
        self.bbox = msg

    def detectimg_callback(self, msg):
        self.detectimg = msg

    def trackimg_callback(self, msg):
        self.trackimg = msg

    def map_callback(self, msg):
        self.map = msg

    def text_callback(self, msg):
        self.text = msg

    def run(self):
        while not rospy.is_shutdown():
            try:
                self.bbox_pub.publish(self.bbox)
                self.detectimg_pub.publish(self.detectimg)
                self.trackimg_pub.publish(self.trackimg)
                self.map_pub.publish(self.map_pub)
                self.text_pub.publish(self.text)
            except:
                print("not publishing yet")
                time.sleep(1)

if __name__ == '__main__':
    rospy.init_node('fake_publisher')
    mod=FakePublish()
    mod.run()

