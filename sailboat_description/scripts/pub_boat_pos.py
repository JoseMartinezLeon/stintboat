#!/usr/bin/env python

import rospy 
from nav_msgs.msg import Odometry
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

global sailboat_odom_list

def get_odom(odom):
	#Create the list for the x and y coordinates of the boat position in the Gazebo.
	sailboat_odom_list = odom.pose.pose.position.x, odom.pose.pose.position.y
	print sailboat_odom_list

def main():
	#Create the new node.
	rospy.init_node('movement', anonymous=True)
	#Create the subscriber to the /sailboat/odom topic.
	rospy.Subscriber('/sailboat/odom', Odometry, get_odom)
	rospy.spin()

if __name__=="__main__":
	main()
