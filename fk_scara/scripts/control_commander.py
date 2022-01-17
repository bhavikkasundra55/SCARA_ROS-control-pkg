#!/usr/bin/env python3
import numpy as np
from math import pi
import rospy
from std_msgs.msg import Float64
import matplotlib.pyplot as plt
#from trajectory_msgs.msg import JointTrajectory
# theta1, theta2 and d are joint angles of robot


def control_commander():
    pub1 = rospy.Publisher('/scara_control/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/scara_control/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/scara_control/joint3_position_controller/command', Float64, queue_size=10)    
    
    rospy.init_node('control_commander', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #traj1 = JointTrajectory()
        cmd_pos1 = -1.0
        cmd_pos2 = - 1.0
        cmd_pos3 = 1.0
        x = [0,1,2,3,4]
        fig, axs = plt.subplots(2, 2)
        '''
        axs[0, 0].plot(cmd_pos1)
        axs[0, 0].set_title('Axis [0, 0]')
        axs[0, 1].plot(i, y, 'tab:orange')
        axs[0, 1].set_title('Axis [0, 1]')
        axs[1, 0].plot(x, -y, 'tab:green')
        axs[1, 0].set_title('Axis [1, 0]')
        axs[1, 1].plot(x, -y, 'tab:red')
        axs[1, 1].set_title('Axis [1, 1]')
        '''

           
        # rospy.loginfo(cmd_pos1)
        pub1.publish(cmd_pos1)
        pub2.publish(cmd_pos2)
        pub3.publish(cmd_pos3)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        control_commander()
    except rospy.ROSInterruptException:
        pass