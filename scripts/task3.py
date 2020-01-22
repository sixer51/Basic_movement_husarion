#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker

rospy.init_node("get_position")
rate = rospy.Rate(10)

marker_msg = Marker()
marker_msg.ns = "position"
marker_msg.id = 0
marker_msg.type = 2 # SPHERE
marker_msg.action = 0
marker_msg.scale.x = 0.2
marker_msg.scale.y = 0.2
marker_msg.scale.z = 0.2
marker_msg.color.a = 1.0
marker_msg.color.g = 1.0 # green

def update_odom(msg):
    marker_msg.pose = msg.pose
    marker_msg.header = msg.header

pos_sub = rospy.Subscriber("/pose", PoseStamped, update_odom)
marker_pub = rospy.Publisher("/marker", Marker, queue_size = 0)

if __name__ == "__main__":
    while not rospy.is_shutdown():
        marker_pub.publish(marker_msg)
        rate.sleep()
