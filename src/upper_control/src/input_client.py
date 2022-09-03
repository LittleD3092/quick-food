import rospy
from std_msgs.msg import String
from test.srv import action,actionResponse

def client(msg):
    msg_to_server = rospy.ServiceProxy("action",action) 
    response = msg_to_server(msg)
    rospy.loginfo(response.response)
    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('upper_mechanism_client')
    rospy.wait_for_service("action")
    rate = rospy.Rate(1000) # 10Hz
    while not rospy.is_shutdown():
        try:
            # input the command manually 
            command = input("command :")
            client(command)
        except rospy.ServiceException :
            pass
    

