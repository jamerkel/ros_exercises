#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

def return_distance(data):
    pub1 = rospy.Publisher('open_space/distance', Float32, queue_size=20)
    distance = max(data.ranges)
    rospy.loginfo(distance)

def return_angle(data):
    pub2 = rospy.Publisher('open_space/angle', Float32, queue_size=20)
    angle_count = data.angle_min
    for i in data.ranges:
        if i != max(data.ranges):
            angle_count += data.angle_increment
        else:
            angle = angle_count
            break
    rospy.loginfo(angle)
def open_space_publisher():
    rospy.init_node('open_space_publisher')

    rospy.Subscriber('fake_scan', LaserScan, return_distance)
    rospy.Subscriber('fake_scan', LaserScan, return_angle)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher() 
