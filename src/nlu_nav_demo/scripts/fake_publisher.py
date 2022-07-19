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
    #   self.bbox=None
    #   self.detectimg=None
    #   self.trackimg=None
    #   self.map=None
    #   self.text=None
    #   self.scan=None
    #   self.path=None
      self.symbol=None
      self.speech=None
      self.world=None


      # Publishers
    #  self.bbox_pub = rospy.Publisher("/detector/bbox_lines", Marker, queue_size=1)
    #  self.detectimg_pub = rospy.Publisher("/annotated_image", Image, queue_size=1)
    #  self.trackimg_pub = rospy.Publisher("/tracker/map_image", Image, queue_size=1)
    #   self.map_pub = rospy.Publisher("/map", OccupancyGrid, queue_size=1)
    #  self.text_pub = rospy.Publisher("/tracker/text", OverlayText, queue_size=1)
    #  self.scan_pub = rospy.Publisher("/haetae/scan_merged", LaserScan, queue_size=50)
    #  self.path_pub = rospy.Publisher("/move_base/TebLocalPlannerROS/global_plan", Path, queue_size=1)
      self.symbol_pub = rospy.Publisher("/haetae/symbol_grounding", String, queue_size=10)
      self.speech_pub = rospy.Publisher("/speech_recognition", String, queue_size=10)
      self.world_pub = rospy.Publisher("/world_model", String, queue_size=10)

      # Subscribers
    #  rospy.Subscriber("/detector/bbox_lines", Marker, self.bbox_callback)
    #  rospy.Subscriber("/annotated_image", Image, self.detectimg_callback)
    #  rospy.Subscriber("/tracker/map_image", Image, self.trackimg_callback)
    #   rospy.Subscriber("/map", OccupancyGrid, self.map_callback)
    #  rospy.Subscriber("/tracker/text", OverlayText, self.text_callback)
    #  rospy.Subscriber("/haetae/scan_merged", LaserScan, self.scan_callback)
    #  rospy.Subscriber("/move_base/TebLocalPlannerROS/global_plan", Path, self.path_callback)
      rospy.Subscriber('/haetae/symbol_grounding', String, self.symbol_callback)
      rospy.Subscriber("/speech_recognition", String, self.speech_callback)
      rospy.Subscriber("/world_model", String, self.world_callback)

    # def bbox_callback(self, msg):
    #     self.bbox = msg

    # def detectimg_callback(self, msg):
    #     self.detectimg = msg

    # def trackimg_callback(self, msg):
    #     self.trackimg = msg

    # def map_callback(self, msg):
    #     self.map = msg

    # def text_callback(self, msg):
    #     self.text = msg

    # def scan_callback(self, msg):
    #     self.scan = msg

    # def path_callback(self, msg):
    #     self.path = msg

    def symbol_callback(self, msg):
        print(msg)
        self.symbol = msg

    def speech_callback(self, msg):
        self.speech = msg

    def world_callback(self, msg):
        self.world = msg

    def run(self):
        while not rospy.is_shutdown():
            #try:
            #    self.bbox_pub.publish(self.bbox)
            #except:
            #    print("bbox not publishing yet")
            #try:
            #    self.detectimg_pub.publish(self.detectimg)
            #except:
            #    print("detectimg not publishing yet")
            #try:            
            #    self.trackimg_pub.publish(self.trackimg)
            #except:
            #    print("trackimg not publishing yet")
            # try:  
            #     self.map_pub.publish(self.map_pub)
            # except:
            #     print("map not publishing yet")                
            # try:  
            #     self.text_pub.publish(self.text)
            # except:
            #     print("text not publishing yet")                
            # try:  
            #     self.scan_pub.publish(self.scan)
            # except:
            #     print("scan not publishing yet")  
            # try:  
            #     self.path_pub.publish(self.path)
            # except:
            #     print("path not publishing yet")           
            try:  
                if self.symbol!= None:
                  self.symbol_pub.publish(self.symbol)
            except:
                print("symbol not publishing yet")             
            try:  
                if self.speech!= None:
                  self.speech_pub.publish(self.speech)
            except:
                print("speech not publishing yet") 
            try:  
                if self.world!= None:
                  self.world_pub.publish(self.world)
            except:
                print("world not publishing yet") 


if __name__ == '__main__':
    rospy.init_node('fake_publisher')
    mod=FakePublish()
    mod.run()

