#!/usr/bin/env python
import rospy
import numpy as np
import random
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=20)
    rospy.init_node('fake_scan_publisher')
    r = rospy.Rate(20)
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        scan = LaserScan()
        
        scan.header.stamp = current_time
        scan.header.frame_id = 'base_link'
        scan.angle_min = (-2*np.pi)/3
        scan.angle_max = (2*np.pi)/3
        scan.angle_increment = (np.pi)/300
        scan.time_increment = 0.05
        scan.range_min = 1.0
        scan.range_max = 10.0
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
