# Pose.py
# Class implementation of a object representing a pose of robot.
# This object includes elements of a pose, including position and orientation.
# We use three elements pointX, pointY, and pointZ to represent the position of the robot.
# We use four elements qX, qY, qZ, and qW to represent the orientation of the robot.

class Pose:
	# Precondition: 7 numbers representing coordinates.
	#				- pointX, pointY, pointZ: the position
	#				  of the robot.
	#				- qX, qY, qZ, qW: the direction that
	#				  the robot is facing. Represented in
	#				  quarternion.
	# Postcondition: The object is set.
	def __init__(self, pointX, pointY, pointZ, qX, qY, qZ, qW):
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Print the object.
	def print():
		pass
	
	# Precondition: Object is initted properly.
	# Postcondition: Return the element pointX.
	def getPointX():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element pointY.
	def getPointY():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element pointZ.
	def getPointZ():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element QX.
	def getQX():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element QY.
	def getQY():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element QZ.
	def getQZ():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return the element QW.
	def getQW():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return a tuple of 
	# 				 the point x, y, and z.
	def getPoint():
		pass

	# Precondition: Object is initted properly.
	# Postcondition: Return a tuple of the quaternion
	# 				 qX, qY, qZ, qW.
	def getQ():
		pass

	# Precondition: A number is given.
	# Postcondition: PointX is set to the given value.
	def setPointX(pointX):
		pass

	# Precondition: A number is given.
	# Postcondition: PointY is set to the given value.
	def setPointY(pointY):
		pass

	# Precondition: A number is given.
	# Postcondition: PointZ is set to the given value.
	def setPointZ(pointZ):
		pass

	# Precondition: A number is given.
	# Postcondition: QX is set to the given value.
	def setQX(qX):
		pass

	# Precondition: A number is given.
	# Postcondition: QY is set to the given value.
	def setQY(qY):
		pass

	# Precondition: A number is given.
	# Postcondition: QZ is set to the given value.
	def setQZ(qZ):
		pass

	# Precondition: A number is given.
	# Postcondition: QW is set to the given value.
	def setQW(qW):
		pass

	# Precondition: Three numbers representing coordinates are given.
	# Postcondition: Point is set to the given value.
	def setPoint(pointX, pointY, pointZ):
		pass

	# Precondition: Four numbers representing quaternion are given.
	# Postcondition: Q is set to the given value.
	def setQ(qX, qY, qZ, qW):
		pass