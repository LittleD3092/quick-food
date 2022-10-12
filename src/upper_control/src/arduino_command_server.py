#!/usr/bin/env python3.6
# this program get the msg sended from client ,which we manually input ,and then send it to arduino

import rospy
from std_msgs.msg import Int8
import serial 
from time import sleep
from upper_control.srv import action,actionResponse 

'''
    The representations of actions:
    0 , standard position
    1 , taking basketball
    2 , throwing basketball
    3 , taking bowling
    4 , relasing bowling
'''

def callback(request):
    motion_pkg = [0,1,2,3,4]
    action = [51,52,53,61,62,63,71,72,73,81,82,83]
    if(request.request in motion_pkg): 
    
        # 如果 client 的 request 滿足要求 , send it to arduino
        ser.write(bytes(str(request.request), 'utf-8'))
        arduino_echo = ''
        while arduino_echo == '' :
            arduino_echo = ser.readline().decode('utf').strip()
    elif(request.request in action):
        ser.write(bytes(str(request.request), 'utf-8'))
    else :
        print('Arduino :invalid command')
        request.request = -1
        
    # send the request to the client 
    return actionResponse(request.request) 


if __name__ == '__main__':

    rospy.init_node('upper_mechanism')
    
    # connect to arduino board
    ser = serial.Serial('/dev/arduino_control',57600)
    ser.timeout = 3

    # if arduino is ready , we will received "Ready"
    arduino_echo = "Arduino :" + ser.readline().decode('utf').strip()
    print(arduino_echo) 
    
    try:
        while True:

            # if client sends a request  , call callback function
            rospy.Service("upper_mechanism",action,callback) 
            rospy.spin()

    except rospy.ROSInterruptException:
        ser.close()
        print('\nend')
        exit()