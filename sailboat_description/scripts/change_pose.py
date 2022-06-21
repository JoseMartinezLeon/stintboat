#! /usr/bin/env python

import rospy #Application Programming Interface (API)
# Enables Python programmers to quickly interface with ROS Topics, Services and Parameters. 
from nav_msgs.msg import Odometry
# wiki.ros.org/nav_msgs
# nav_msgs.msg - defines the common messages used to interact with the navigation stack
# nav_msgs.msg/Odometry.msg 
# This represents an estimate of a position and velocity in free space
# The pose in this message should be specified in coordinate frame given by the header.frame_id
# The twist in this message should be specified in the coordinate frame given by the child_frame_id
from gazebo_msgs.msg import ModelState
# wiki.ros.org/gazebo_msgs.msg
# gazebo_msgs - Message and service data structures for interacting with Gazebo from ROS
# gazebo_msgs/ModelState.msg 
# Set Gazebo Model pose and twist
from gazebo_msgs.srv import SetModelState, GetModelState, GetModelStateRequest
# SetModelState
# GetModelState
# GetModelStateRequest
from tf.transformations import euler_from_quaternion
# transformations: A library for calculating 4x4 matrices for translating, rotating, reflecting
# scaling, shearing, projecting, orthogonalizing and superimposing arrays of 3D homogeneous 
# coordinates as well as for converting between rotation matrices, Euler angles, and quaternions.
# Requirements: Python 2.6, Numpy 1.3, transformations.c 20090418
# euler_from_quaternion (quaternion, axes = 'sxyz')
# Return Euler angles from quaternion for specified axis sequences 
from math import atan2
# math - This module provides acces to the mathematical functions defined by the C standard 
# atan2 - Return atan(y/x), in radians. The result is between -pi and pi. 

# Global variables - variables that are created outside of a function. 
# Pose: describes a position and an orientation
global pose_x # Current position in x 
global pose_y # Current position in y  
global yaw    # Current orientation in z
global waypoint_x # Next position in x 
global waypoint_y # Next position in y  


def callback(msg):
# callback - a function that is passed as an argument to other function.
# This other function is expected to call this callback function in its definition. 
	pub_odom = rospy.Publisher('/sailboat/odom', Odometry, queue_size = 10)
    # pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10)    
	pose_x = msg.pose.pose.position.x
	pose_y = msg.pose.pose.position.y
    # x = data.pose.pose.position.x
    # y = data.pose.pose.position.y 
	state_msg = ModelState()
    # ModelState() - Initializes a new instance of the ModelState class
        state_msg.model_name = 'sailboat'
    #Example (source: answers.gazebosim): 
    # state_msg = ModelState()
    # state_msg.model_name = 'my_robot'
    # state_msg.pose.position.x = 0
    # state_msg.pose.position.y = 0
    # state_msg.pose.position.z = 0
    # state_msg.pose.orientation.x = 0
    # state_msg.pose.orientation.y = 0
    # state_msg.pose.orientation.z = 0
    # state_msg.pose.orientation.w = 0
	
	#Caclulate pitch, yaw and roll values from the orientation numbers to determine the direction the boat is facing.	
	orientation_q = msg.pose.pose.orientation 
	orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
	(roll, pitch, yaw) = euler_from_quaternion(orientation_list)
	print 'x:', pose_x 
	print 'y:', pose_y
	print '------------'
	print 'yaw:', yaw
	print '------------'
	
	# Calculating how much the boat has to turn to face the direction of waypoint.
	inc_x = waypoint_x - pose_x # Next x coordinate - current x coordinate
	inc_y = waypoint_y - pose_y # Next y coordinate - current y coordinate
	angle_to_goal = atan2(inc_y, inc_x) 
	print inc_x, inc_y, angle_to_goal
	# If the boat is facing the wrong way, rotate it until it is positioned in the direction of the waypoint otherwise print the message.
	if abs(angle_to_goal - yaw)>0.1:
        	state_msg.pose.position.x = pose_x + 0.3 
        	#pub_odom.publish(pose_z + 0.3)
		rospy.wait_for_service('/gazebo/get_model_state')
		set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
		resp = set_state(state_msg)
	else:
		print ('sailboat faces the waypoint')

waypoint_x = 5.0
waypoint_y = 5.0
rospy.init_node('odom_subscriber')
sub_odom = rospy.Subscriber('/sailboat/odom', Odometry, callback)
rospy.spin()
