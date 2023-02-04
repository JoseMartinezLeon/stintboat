# Stintboat

Stintboat project // FabLab UTP

This project is centered around developing all the necessary systems that are needed to convert a regular sailboat into a fully autonomous one.
The hull of the sailboat has already been built in the central campus of the Technological University of Panama; the sail and the rudder are in active development. 

This repository contains all the packages developed so far for the simulation of said sailboat in the ROS/Gazebo environment. The packages contained in this repository represent a first stable build. The hull in the simulation is based on the one that has already been built while the sail and the rudder
are placeholders. 


# Setup

This first build was developed around the Ubuntu 18.04 LTS release and therefore uses ROS Melodic Morenia and Gazebo 9. Said release can be found here: https://releases.ubuntu.com/18.04/ 

For the ROS Melodic installation: http://wiki.ros.org/melodic/Installation/Ubuntu

ROS Control packages should also be installed, as they are used for the controller portion of the simulation: https://classic.gazebosim.org/tutorials?tut=ros_control

The stintboat_description package makes heavy use of the VRX simulation environment, which is available here: https://github.com/osrf/vrx

The VRX simulation environment has 2 main contributions. First, the example_course.world will be automatically loaded into Gazebo by the .launch file contained in the stintboat_description package. Additionally, the URDF file contained in said package makes use of the usv_gazebo_dynamics_plugin causing the sailboat model to float above water and be affected by the waves.     

# Running the simulation

After the VRX simulation environment and the avaliable packages have been setup in the corresponding catkin workspace, the simulation can be run using the following commands in the terminal: 

$ source ~/catkin_ws/devel/setup.bash

$ roslaunch stintboat_description gazebo.launch

Both RVIZ and Gazebo should open and display the model: 

![rviz](https://user-images.githubusercontent.com/90019998/171939609-bb5bd0ca-7dfe-43f2-bf96-61ffe8c39657.png)

![gazebo](https://user-images.githubusercontent.com/90019998/171939867-71581a12-8176-4623-bd23-03d77d38dcd6.png)

# Contacts

jose.martinez18@utp.ac.pa 
