import os
import sys


os.system("ros2 run gazebo_ros spawn_entity.py -file model/PR001.sdf -entity PR001 -x 93 -y -11.5  -Y -1.57")
os.system("ros2 run gazebo_ros spawn_entity.py -file model/PR002.sdf -entity PR002 -x 93 -y -15.9  -Y -1.57")
