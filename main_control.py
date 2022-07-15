# main_control Node
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class DotRecognize:
	
	# Precondition: Nothing.
	# Postcondition: Client is up and ready to request.
	def __init__(self):
		# TODO: Implement function
		pass

	# Precondition: Client is up.
	# Postcondition: Return an integer value,
	# 				 meaning the dot number in the middle 
	#  				 of the camera.
	def request(self):
		# TODO: Implement function.
		pass

class AlphabetRecognize:
	
	# Precondition: Nothing.
	# Postcondition: Client is up and ready to request.
	def __init__(self):
		# TODO: implement function
		pass

	# Precondition: Client is up.
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
		# TODO: implement function
		pass

class ColorDetect:

	# Precondition: Nothing
	# Postcondition: Client is up and ready to request.
	def __init__(self):
		# TODO: implement function
		pass

	# Precondition: Client is up
	# Postcondition: Return three integer values.
	# 				 1. Distance between the ball and the
	#					middle of the camera. In pixels.
	#				 2. Depth of the ball. In centimeters.
	#				 3. The color of the ball.
	#					1 for orange.
	#					2 for blue.
	# 					3 for black.
	def request(self):
		# TODO: implement function
		pass

class Navigation:
	
	# Precondition: Nothing.
	# Postcondition: Subscriber and publisher is up.
	def __init__(self):
		pass

	# Precondition: Subscriber is up.
	# Postcondition: Returns the current position of robot.
	def getPos(self):
		pass

	# Precondition: Publisher is up. Given a 3D point and a quaternion as parameter.
	# Postcondition: Robot moves to the location and pose determined.
	def move(self, pointX, pointY, pointZ, qX, qY, qZ, qW):
		pass

if __name__ == '__main__':
	rospy.init_node('main_control', anonymous=True)
	# TODO: init all subscribers and publishers
	
	rospy.spin()