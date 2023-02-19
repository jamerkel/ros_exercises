#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32

def calc_log(data):
    pub = rospy.Publisher('random_float_log', Float32, queue_size=20)
    random_log = np.log(data.data)
    rospy.loginfo(random_log)
    pub.publish(random_log)

def simple_subscriber():
    rospy.init_node('simple_subscriber')
    rospy.Subscriber('my_random_float', Float32, calc_log)
    rospy.spin()

if __name__ == '__main__':
    simple_subscriber()
