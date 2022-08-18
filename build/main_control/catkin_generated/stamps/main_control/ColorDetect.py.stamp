# ColorDetect.py
# class implementation for ROS client of server "color_detect".
import rospy
from std_msgs.msg import Empty

class ColorDetect:

	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# This is empty intentionally.
		pass

	# Precondition: Nothing.
	# Postcondition: Return three integer values.
	# 				 1. Distance between the ball and the
	#					middle of the camera. In pixels.
	#				 2. Depth of the ball. In centimeters.
	#				 3. The color of the ball.
	#					1 for orange.
	#					2 for blue.
	# 					3 for black.
	def request(self):
		rospy.wait_for_service('color_detect', 5)
		try:
			color_detect = rospy.ServiceProxy('color_detect', Empty)
			resp = color_detect()
			return (resp.data[0], resp.data[1], resp.data[2])
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1