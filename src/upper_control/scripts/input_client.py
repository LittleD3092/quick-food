import rospy
from std_msgs.msg import String
def talker():

    rospy.init_node('upper_mechanism_client')
    rate = rospy.Rate(1000) # 10Hz
    while not rospy.is_shutdown():
        msg = input()
        rospy.loginfo(msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
