# AlphabetRecognize.py
# Class implementation for ROS client of server "alphabet_recognize".
import rospy
from std_msgs.msg import Empty

class AlphabetRecognize:
	
	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# This is empty intentionally.
		pass

	# Precondition: Nothing.
	# Postcondition: Return three integer values.
	# 				 1. The distance between the alphabet
	# 					and the middle of the camera.
	# 					In pixels.
	# 				 2. The depth of the alphabet. 
	# 					In centimeters.
	# 				 3. The alphabet.
	#					1 for 'T',
	# 					2 for 'D',
	# 					3 for 'K'.
	def request(self):
		rospy.wait_for_service('alphabet_recognize', 5)
		try:
			alphabet_recognize = rospy.ServiceProxy('alphabet_recognize', Empty)
			resp = alphabet_recognize()
			return (resp.data[0], resp.data[1], resp.data[2])
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1