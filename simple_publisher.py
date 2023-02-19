#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Float32

def simple_publisher():
    pub = rospy.Publisher('my_random_float', Float32, queue_size=20)
    rospy.init_node('simple_publisher', anonymous=True)
    r = rospy.Rate(20)
    while not rospy.is_shutdown():
        random_float = random.uniform(0,10)
        rospy.loginfo(random_float)
        pub.publish(random_float)
        r.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
