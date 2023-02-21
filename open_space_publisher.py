#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace

rospy.set_param('subscriber_topic', 'fake_scan')
rospy.set_param('publisher_topic', 'open_space')

def return_OpenSpace(data):
    pub = rospy.Publisher(rospy.get_param('publisher_topic'), OpenSpace, queue_size=20)
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

   # rospy.Subscriber(rospy.get_param('subscriber_topic'), LaserScan, return_distance)
  #  rospy.Subscriber(rospy.get_param('subscriber_topic'), LaserScan, return_angle)
    rospy.Subscriber(rospy.get_param('subscriber_topic'), LaserScan, return_OpenSpace)
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher() 
