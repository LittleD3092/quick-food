# Navigation.py
# Class implementation for ROS client of server "navigation".

class Navigation:
	
	# Precondition: Nothing.
	# Postcondition: Client is up.
	def __init__(self):
		pass

	# Precondition: Client is up. Given a 3D point and a quaternion as parameter or a pose object.
	# Postcondition: Robot moves to the location and pose determined.
	def move(self, pose = None,
			 	   pointX = None, pointY = None, pointZ = None, qX = None, qY = None, qZ = None, qW = None):
		pass