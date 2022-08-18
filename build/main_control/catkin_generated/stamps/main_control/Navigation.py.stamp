# Navigation.py
# Class implementation for ROS client of server "navigation".
from main_control.srv import main2nav, main2navRequest, main2navResponse
import rospy

class Navigation:
	
	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# This is empty intentionally.
		pass

	# Precondition: Given a 3D point and a quaternion as parameter or a pose object.
	# Postcondition: Robot moves to the location and pose determined.
	def move(self, req):
		rospy.wait_for_service('navigation', 5)
		assert type(req) == main2navRequest
		try:
			navigation = rospy.ServiceProxy('navigation', main2nav)
			resp = navigation(req)
			return resp
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1