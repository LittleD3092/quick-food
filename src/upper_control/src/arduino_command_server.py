#!/usr/bin/env python
# this program get the msg from ros topic ,which we manually input ,and then send it to arduino.
import rospy
from std_msgs.msg import String
import serial 
from time import sleep
from test.srv import action,actionResponse 

def callback(request):
    actions = ['t1','t2','t3','d1','d2','d3','p1','p2','p3','f1','f2','f3']
    if(request.request in actions): 
        
        # 如果 client 的 request 滿足要求 , send it to arduino
        ser.write(bytes(request.request, 'utf-8'))
        arduino_echo = "Arduino :" + ser.readline().decode('utf').strip()
        rospy.loginfo(arduino_echo)

    else :
        rospy.loginfo('invalid command')
        
    # 回傳response 給 client
    return actionResponse(request.request) 


if __name__ == '__main__':

    rospy.init_node('upper_mechanism_server')
    
    # connect to arduino board
    ser = serial.Serial('/dev/ttyUSB0',57600)
    ser.timeout = 3
    sleep(3)

    # if arduino is ready , we will received "Ready"
    arduino_echo = "Arduino :" + ser.readline().decode('utf').strip()
    rospy.loginfo(arduino_echo) 
    
    try:
        while True:

            # client 丟了一個 request 進來 , 呼叫callback
            rospy.Service("action",action,callback) 
            rospy.spin()

    except rospy.ROSInterruptException:
        ser.close()
        rospy.loginfo('\nend')
        exit()