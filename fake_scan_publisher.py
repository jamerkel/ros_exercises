#!/usr/bin/env python
import rospy
import numpy as np
import random
from sensor_msgs.msg import LaserScan

rospy.set_param('publish_topic', 'fake_scan')
rospy.set_param('publish_rate', 20)
rospy.set_param('angle_min', (-2*np.pi)/3)
rospy.set_param('angle_max', (2*np.pi)/3)
rospy.set_param('range_min', 1.0)
rospy.set_param('range_max', 10.0)
rospy.set_param('angle_increment', (np.pi)/300)

def fake_scan_publisher():
    pub = rospy.Publisher(rospy.get_param('publish_topic'), LaserScan, queue_size=20)
    rospy.init_node('fake_scan_publisher')
    r = rospy.Rate(rospy.get_param('publish_rate'))
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        scan = LaserScan()
        
        scan.header.stamp = current_time
        scan.header.frame_id = 'base_link'
        scan.angle_min = rospy.get_param('angle_min')
        scan.angle_max = rospy.get_param('angle_max')
        scan.angle_increment = rospy.get_param('angle_increment')
        scan.time_increment = 0.05
        scan.range_min = rospy.get_param('range_min')
        scan.range_max = rospy.get_param('range_max')
        scan.ranges = []
        i = scan.angle_min
        while i <= scan.angle_max + scan.angle_increment:
            range_i = random.uniform(1,10)
            scan.ranges.append(range_i)
            i += scan.angle_increment

        rospy.loginfo(scan)
        pub.publish(scan)
        r.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
    except rospy.ROSInterruptException:
        pass
