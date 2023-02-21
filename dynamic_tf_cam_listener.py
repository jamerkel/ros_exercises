#!/usr/bin/env python 
import rospy
import tf2_ros as tf2
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('dynamic_tf_cam_listener')

    tfBuffer = tf2.Buffer()
    listener = tf2.TransformListener(tfBuffer)

    new_left = rospy.Publisher('left_cam_pose', geometry_msgs.msg.Pose, queue_size=200)
    new_right = rospy.Publisher('right_cam_pose', geometry_msgs.msg.Pose, queue_size=200)

    r = rospy.Rate(200)

    while not rospy.is_shutdown():
        try:
            transform_left = tfBuffer.lookup_transform("base_link_gt", "left_cam",rospy.Time())
            transform_right = tfBuffer.lookup_transform("left_cam", "right_cam", rospy.Time())

        except (tf2.LookupException, tf2.ConnectivityException, tf2.ExtrapolationException):
            r.sleep()
            continue

        left_pose = geometry_msgs.msg.Pose()
        left_pose.position.x = transform_left.transform.translation.x
        left_pose.position.y = transform_left.transform.translation.y
        left_pose.position.z = transform_left.transform.translation.z
        left_pose.orientation.w = 1.0

        right_pose = geometry_msgs.msg.Pose()
        right_pose.position.x = transform_right.transform.translation.x
        right_pose.position.y = transform_right.transform.translation.y
        right_pose.position.z = transform_right.transform.translation.z
        right_pose.orientation.w = 1.0

        new_left.publish(left_pose)
        new_right.publish(right_pose)
        r.sleep()

