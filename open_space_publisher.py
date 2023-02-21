#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace

def return_OpenSpace(data):
    pub = rospy.Publisher('open_space', OpenSpace, queue_size=20)
    space = OpenSpace()
    os_distance = max(data.ranges)
    angle_count = data.angle_min
    for i in data.ranges:
        if i != os_distance:
            angle_count += data.angle_increment
        else:
            os_angle = angle_count

    space.angle = os_angle
    space.distance = os_distance
    rospy.loginfo(space)

    pub.publish(space)

def return_distance(data):
    pub1 = rospy.Publisher('open_space/distance', Float32, queue_size=20)
    distance = max(data.ranges)
    rospy.loginfo(distance)

    pub1.publish(distance)

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

    pub2.publish(angle)
def open_space_publisher():
    rospy.init_node('open_space_publisher')

   # rospy.Subscriber('fake_scan', LaserScan, return_distance)
  #  rospy.Subscriber('fake_scan', LaserScan, return_angle)
    rospy.Subscriber('fake_scan', LaserScan, return_OpenSpace)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher() 
