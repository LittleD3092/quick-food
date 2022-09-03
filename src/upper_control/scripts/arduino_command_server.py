#!/usr/bin/env python
# this program get the msg from ros topic ,which we manually input ,and then send it to arduino.
import rospy
from std_msgs.msg import String
import serial 
from time import sleep
from test.srv import upper_mechanism,upper_mechanismResponse


def listener(data):
    
    actions = ['t1','t2','t3','d1','d2','d3','p1','p2','p3','f1','f2','f3']
    if(data.data in actions):

        ser.write(bytes(data.data, 'utf-8'))

        arduino_echo = "Arduino :" + ser.readline().decode('utf').strip()
        rospy.loginfo(arduino_echo)

    else :
        rospy.loginfo('invalid command')

if __name__ == '__main__':

    rospy.init_node('upper_mechanism_server', anonymous=True)
    rospy.wait_for_service()
    ser = serial.Serial('/dev/ttyUSB0',57600)
    ser.timeout = 3
    sleep(3)

    arduino_echo = "Arduino :" + ser.readline().decode('utf').strip()
    rospy.loginfo(arduino_echo) 
    
    try:
        while True:
            rospy.Subscriber("chatter", String, listener )
            rospy.spin()
    except rospy.ROSInterruptException:
        ser.close()
        rospy.loginfo('\nend')
        exit()