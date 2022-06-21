#! /usr/bin/env python
# based on code from: https://answers.ros.org/question/222033/how-do-i-publish-gazebo-position-of-a-robot-model-on-odometry-topic/

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
# std_msgs/Header.msg 
# Standard metadata for higher-level stamped data types. 
# This is generally used to communicate timestamped data in a particular coordinate frame. 
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

if __name__ == '__main__':
	# Create the odom_pub node.
	rospy.init_node('odom_pub')
	# rospy.init_node('my_node_name')
	#Create the publisher to the /boat/odom topic.
	odom_pub=rospy.Publisher ('/sailboat/odom', Odometry, queue_size=10)
	# pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10)
	rospy.wait_for_service ('/gazebo/get_model_state')
	get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	# ROS services are defined by srv files, which contains a request message and a responde message.
	# These are identical to the messages used with ROS Topics. 
	# rospy convers these srv files into Python source codes. 
	# Three classes: service definitions, request messages and response messages. 
	# add_two_ints = rospy.ServiceProxy('service_name', my_package.srv.Foo)

	odom=Odometry()
	header = Header()
	header.frame_id='sailboat/odom'
	# header.frame_id ='/odom' 

	model = GetModelStateRequest()
	model.model_name='sailboat'
	# model.model_name='the_name_of_your_robot'

	r = rospy.Rate(2)

	while not rospy.is_shutdown():
	    result = get_model_srv(model)
	    # Assign the received values from the Gazebo to the odometry topic.
	    odom.pose.pose = result.pose
	    odom.twist.twist = result.twist

	    header.stamp = rospy.Time.now()
	    odom.header = header
	    # Publish the received values to the odometry topic.
	    odom_pub.publish (odom)

	    r.sleep()
