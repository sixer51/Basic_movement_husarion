#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("move")
move_forward = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
velocity = Twist()
rate = rospy.Rate(10)

def stop():
    velocity.linear.x = 0.0
    move_forward.publish(velocity)
    rate.sleep()

def forward(forward_velocity, distance):
    velocity.linear.x = forward_velocity
    t0	= rospy.Time.now().to_sec()
    distance_travelled = 0

    while distance_travelled < distance:
        move_forward.publish(velocity)
        t1 = rospy.Time.now().to_sec()
        distance_travelled = forward_velocity*(t1-t0)
        rate.sleep()
    stop()

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.sleep(3.0) 
        forward(0.2, 1.0)
        rospy.spin()
