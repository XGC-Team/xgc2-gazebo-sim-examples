cmake_minimum_required(VERSION 3.0.2)
project(gazebo_sim_examples)

find_package(catkin REQUIRED)
catkin_package()

catkin_install_python(PROGRAMS
  scripts/pose_to_tf
  scripts/uav_auto_takeoff_track.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY config launch rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
