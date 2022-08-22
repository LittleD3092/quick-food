# main_control Node
# !/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int16
from main_control.srv import main2nav, main2navRequest, main2navResponse
from color_detect_srvs.srv import colorSrv, colorSrvRequest, colorSrvResponse
from alphabet_recognize.srv import alphabetSrv, alphabetSrvRequest, alphabetSrvResponse

assert True # turn off this before race

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
	def request(self, num = 0):
		rospy.wait_for_service('alphabet_recognize', 5)
		try:
			alphabet_recognize = rospy.ServiceProxy('alphabet_recognize', alphabetSrv)
			resp = alphabet_recognize(alphabetSrvRequest(position_req = num))
			return (resp.x_diff_srv, resp.distance_srv, resp.alphabet_srv)
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1

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
	def request(self, num = 0):
		rospy.wait_for_service('color_detect', 5)
		try:
			color_detect = rospy.ServiceProxy('color_detect', colorSrv)
			resp = color_detect(num)
			return (resp.color_srv, resp.distance_srv, resp.x_diff_srv)
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1

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

if __name__ == '__main__':
	# # init all nodes, uncomment the node you needed
	# dotNode = DotRecognize()
	alphabetNode = AlphabetRecognize()
	# ballNode = ColorDetect()
	# baseNode = Navigation()
	# upperNode = UpperMechanism()
	# upperNode.move(0)

	# # test ballNode
	# print("Ball node test:")
	# print(ballNode.request())

	# test alphabet node
	print("Alphabet node test:")

	while True:
		req = alphabetNode.request()
		if req != (0, 0, 0):
			print(req)
			break

	######################################################################################
	## main loop: This is the main loop that will be running on the race.
	
	# # go to I
	# baseNode.move(POSE_I)

	# # take basketball three times
	# basketballStack = [] # record the stack of basketballs on the robot
	# basketballOptions = ("T", "D", "K") # the options of basketballs
	# for i in range(3):
	# 	basketballStack.append(basketballOptions[ballNode.request() - 1])
	# 	upperNode.move(1)
	# assert basketballStack.count("T") == 1, "There should be one T in the stack."
	# assert basketballStack.count("D") == 1, "There should be one D in the stack."
	# assert basketballStack.count("K") == 1, "There should be one K in the stack."
	# assert len(basketballStack) == 3, "There should be three basketballs in the stack."

	# # go to G
	# baseNode.move(POSE_G)

	# # throw the basketballs to three baskets marked T, D, K
	# for i in range(3):
	# 	baseNode.move(POSE_BASKET[i])
	# 	chr = AlphabetRecognize.request()
	# 	assert type(chr) == str, "The character should be a string."
	# 	assert chr[0] in ('T', 'D', 'K'), "The character should be T, D, or K."
	# 	basketballStack[basketballStack.index(chr)] = i

	# for i in range(-1, -4, -1):
	# 	baseNode.move(POSE_BASKET[ basketballStack[i] ])
	# 	upperNode.move(2)


	# # go to B (checkpoint)
	# baseNode.move(POSE_B)

	# # go to J
	# baseNode.move(POSE_J)

	# # take bowling three times
	# for i in range(3):
	# 	upperNode.move(3)

	# # go to H
	# baseNode.move(POSE_H)

	# # release bowling to three goals marked in dot numbers
	# dic = {}
	# for i in range(6):
	# 	baseNode.move(POSE_GOAL[i])
	# 	num = DotRecognize.request()
	# 	if num in range(1, 4):
	# 		dic[num] = POSE_GOAL[i]

	# for i in range(3, 0, -1):
	# 	baseNode.move(dic[i])
	# 	upperNode.move(4)

	# End of main loop
	##############################################################