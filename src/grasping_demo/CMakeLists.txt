cmake_minimum_required(VERSION 3.0.2)
project(grasping_demo)

find_package(catkin REQUIRED)

catkin_python_setup()
catkin_package()
catkin_install_python(PROGRAMS
    nodes/capture_helper.py
    nodes/pcd_processing.py
    nodes/kuka_controller.py
    nodes/command_prompt.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES
    launch/grasping_pcd_processing.launch
    launch/grasping_controller.launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
