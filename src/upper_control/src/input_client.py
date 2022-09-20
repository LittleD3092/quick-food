#!/usr/bin/env python3.6

import rospy
from std_msgs.msg import Int8
from upper_control.srv import action,actionResponse

def client(msg):
    msg_to_server = rospy.ServiceProxy("upper_mechanism",action) 
    response = msg_to_server(msg)
    print("Arudino :" , response.response)
    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('upper_mechanism_client_test')
    rospy.wait_for_service("upper_mechanism")
    rate = rospy.Rate(1000) # 1000Hz
    while not rospy.is_shutdown():
        try:
            # input the command manually 
            command = int(input("command :"))
            client(command)
        except rospy.ServiceException :
            pass
    

