# DotRecognize.py
# Class implementation for ROS client of server "dot_recognize".

import rospy
from std_msgs.msg import Empty

class DotRecognize:
	
	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# This is empty intentionally.
		pass

	# Precondition: Client is up.
	# Postcondition: Return an integer value,
	# 				 meaning the dot number in the middle 
	#  				 of the camera.
	def request(self):
		rospy.wait_for_service('dot_recognize', 5)
		try:
			dot_recognize = rospy.ServiceProxy('dot_recognize', Empty)
			resp = dot_recognize()
			return resp.data
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1