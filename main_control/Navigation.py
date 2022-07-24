# Navigation.py
# Class implementation for ROS client of server "navigation".
from geometry_msgs import Pose
import rospy

class Navigation:
	
	# Precondition: Nothing.
	# Postcondition: Nothing.
	def __init__(self):
		# This is empty intentionally.
		pass

	# Precondition: Given a 3D point and a quaternion as parameter or a pose object.
	# Postcondition: Robot moves to the location and pose determined.
	def move(self, pose):
		rospy.wait_for_service('navigation', 5)
		assert type(pose) == Pose
		try:
			navigation = rospy.ServiceProxy('navigation', Pose)
			resp = navigation(pose)
			return resp
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1