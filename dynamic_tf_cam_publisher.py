#!/usr/bin/env python

import rospy
import tf
import tf2_ros as tf2
import numpy as np
import geometry_msgs.msg
from nav_msgs.msg import Odometry

tf_vector_left = np.array([-0.05, 0, 0])
tf_vector_right = np.array([0.1, 0, 0])
trans_left = tf.transformations.translation_matrix(tf_vector_left)
trans_right = tf.transformations.translation_matrix(tf_vector_right)

def dynamic_tf_cam_publisher(data):
    br = tf2.TransformBroadcaster()
    r = rospy.Rate(200)

    world_pos = np.array([data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z])

    world_tf = tf.transformations.compose_matrix(translate=world_pos)
    left_cam_pos = tf.transformations.concatenate_matrices(world_tf, trans_left)
    left_trans_vec = tf.transformations.translation_from_matrix(left_cam_pos)
    right_cam_pos = tf.transformations.concatenate_matrices(left_cam_pos, trans_right)
    right_trans_vec = tf.transformations.translation_from_matrix(right_cam_pos)

    t_left = geometry_msgs.msg.TransformStamped()
    t_left.header.stamp = rospy.Time.now()
    t_left.header.seq = data.header.seq
    t_left.header.frame_id = "base_link_gt"
    t_left.child_frame_id = "left_cam"

    t_left.transform.translation.x = left_trans_vec[0]
    t_left.transform.translation.y = left_trans_vec[1]
    t_left.transform.translation.z = left_trans_vec[2]
    t_left.transform.rotation.w = 1

    t_right = geometry_msgs.msg.TransformStamped()
    t_right.header.stamp = rospy.Time.now()
    t_right.header.seq = data.header.seq
    t_right.header.frame_id = "left_cam"
    t_right.child_frame_id = "right_cam"

    t_right.transform.translation.x = right_trans_vec[0]
    t_right.transform.translation.y = right_trans_vec[1]
    t_right.transform.translation.z = right_trans_vec[2]
    t_right.transform.rotation.w = 1

    br.sendTransform(t_left)
    br.sendTransform(t_right)
    r.sleep()


if __name__ == '__main__':
    rospy.init_node('dynamic_tf_cam_publisher')
    rospy.Subscriber('tesse/odom', Odometry, dynamic_tf_cam_publisher)
    rospy.spin()
