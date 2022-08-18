# UpperMechanism.py
# Class implementation for ROS client of server "upper_mechanism".

import rospy
from std_msgs.msg import Int16

class UpperMechanism:

	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# intentionally empty
		pass

	# Precondition: Client is up. Given an integer 
	# 				representing the movement. 
	# 				- 0 for standard position.
	# 				- 1 for take basketball.
	# 				- 2 for throw basketball.
	# 				- 3 for take bowling.
	#				- 4 for release bowling.
	def move(self, cmd):
		rospy.wait_for_service('upper_mechanism', 5)
		try:
			upper_mechanism = rospy.ServiceProxy('upper_mechanism', Int16)
			resp = upper_mechanism(cmd)
			return resp.data
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1