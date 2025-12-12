import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/thkim0508/ros2_ws/install/open_manipulator_teleop'
