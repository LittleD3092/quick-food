# main_control Node
# !/usr/bin/env python3.6

import rospy
from std_msgs.msg import Empty, Int16, Bool
from navigation.srv import main2nav, main2navRequest, main2navResponse
from color_detect_srvs.srv import colorSrv, colorSrvRequest, colorSrvResponse
from alphabet_recognize.srv import alphabetSrv, alphabetSrvRequest, alphabetSrvResponse
from upper_control.srv import action, actionRequest, actionResponse
from dot_recognize.srv import dotSrv, dotSrvRequest, dotSrvResponse
from main_control.msg import main_status

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
			resp = color_detect(colorSrvRequest(position_srv = num))
			return resp.color_srv
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
			dot_recognize = rospy.ServiceProxy('dot_recognize', dotSrv)
			resp = dot_recognize(dotSrvRequest(position = 0))
			return resp.dot_number
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
	def move(self, req = (0, 0, 180, False)):
		assert type(req) == tuple
		assert len(req) == 3
		req = main2navRequest(main_x = req[0], main_y = req[1], rotation = req[2], check_pose = req[3])
		rospy.wait_for_service('/navigation', 5)
		assert type(req) == main2navRequest
		try:
			done_flag = False
			while not done_flag:
				navigation = rospy.ServiceProxy('/navigation', main2nav)
				resp = navigation(req)
				done_flag = resp.done_flag
			return True
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
			upper_mechanism = rospy.ServiceProxy('upper_mechanism', action)
			resp = upper_mechanism(actionRequest(request = cmd))
			if cmd == 1 or cmd == 3:
				StatusPublisher().publish(True)
			elif cmd == 2 or cmd == 4:
				StatusPublisher().publish(False)
			return resp.response
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1

class StatusPublisher:
	
	# Precondition: Nothing.
	# Postcondition: The publisher is up. The topic is main_status.
	def __init__(self):
		self.pub = rospy.Publisher('main_status', Bool, queue_size = 100)
		rospy.init_node("main_control", anonymous = True)
		self.pub.publish(main_status(has_ball = False))

	# Precondition: Given a parameter status that indicates the current status.
	#               Now is a boolean value that is either true or false.
	#               True for the ball is in the upper mechanism.
	#               False for the ball is not in the upper mechanism.
	# Postcondition: Publish the status code.
	def publish(self, status):
		if type(status) == bool:
			status = main_status(has_ball = status)
		else:
			assert type(status) == main_status()
		self.pub.publish(status)

if __name__ == '__main__': # main for B field.
	# init all nodes, uncomment the node you needed
	dotNode = DotRecognize()
	alphabetNode = AlphabetRecognize()
	ballNode = ColorDetect()
	baseNode = Navigation()
	upperNode = UpperMechanism()
	upperNode.move(0)
	statusPub = StatusPublisher()

	# # test ballNode
	# print("Ball node test:")
	# print(ballNode.request())

	# test alphabet node
	# print("Alphabet node test:")

	# while True:
	# 	req = alphabetNode.request()
	# 	if req != (0, 0, 0):
	# 		print(req)
	# 		break

	# while True:
	# 	req = ballNode.request()
	# 	if req != 0:
	# 		print(req)
	# 		break

	# test dot node
	# print("Dot node test:")
	# while True:
	# 	req = dotNode.request()
	# 	if req != 0:
	# 		print(req)
	# 		break

	# test navigation
	# while(not(nav.move(main2navRequest(main_x = 5, main_y = 0, rotation = 180)))):
	# 	print("not done")

	# print("done")

	######################################################################################
	# main loop: This is the main loop that will be running on the race.
	
	# go to I
	print("moving forward...")
	baseNode.move((393, 0, 180))
	print("moving sideways...")
	baseNode.move((393, 40, 180))
	print("moving sideways to basketball...")
	baseNode.move((393, 90, 180, True))

	# take basketball three times
	basketballQueue = [] # record the queue of basketballs on the robot
	basketballOptions = ("", "T", "D", "K") # the options of basketballs
	for i in range(3):
		ballColor = 0
		print("scanning ball...")
		while ballColor == 0:
			ballColor = ballNode.request()
		print("ball scanned.")
		basketballQueue.append(basketballOptions[ballColor])
		upperNode.move(1)
	assert basketballQueue.count("T") == 1, "There should be one T in the stack."
	assert basketballQueue.count("D") == 1, "There should be one D in the stack."
	assert basketballQueue.count("K") == 1, "There should be one K in the stack."
	assert len(basketballQueue) == 3, "There should be three basketballs in the stack."
	print("basketballStack =", basketballQueue)

	# go to G
	print("moving sideways to intersection...")
	baseNode.move((392.5, 40, 180))
	print("moving forward...")
	baseNode.move((900, 40, 180))
	print("turning...")
	baseNode.move((900, 40, 270))
	print("moving to basketball...")
	baseNode.move((900, -138, 270))
	

	# throw the basketballs to three baskets marked T, D, K
	POSE_BASKET = ((900, -208, 270, True), 
				   (900, -138, 270, True), 
				   (900, -68, 270, True))
	# scan for board
	chrs = alphabetNode.request()
	print(chrs)
	assert type(chrs) == list, "The characters should be a list."
	for i in range(0, 3):
		basketballQueue[basketballQueue.index(chrs[i])] = i
	# remove the queue
	for i in range(0, 3):
		print("throwing to basket", chrs[i], "at", POSE_BASKET[ basketballQueue[i] ], "...")
		baseNode.move(POSE_BASKET[ basketballQueue[i] ])
		upperNode.move(2)


	# go to the front of B (checkpoint)
	print("moving to checkpoint...")
	baseNode.move((900, 138, 270))
	baseNode.move((900, 138, 180))
	baseNode.move((1000, 138, 180))
	baseNode.move((1000, 138, 90))
	print("moving to bowling...")
	baseNode.move((1000, 373, 90, True))

	# go to J

	# take bowling three times
	print("taking bowling...")
	for i in range(3):
		upperNode.move(3)

	print("publish loaded...")
	statusPub.publish(True)

	# go to H
	baseNode.move((930, 373, 90))

	# release bowling to three goals marked in dot numbers
	POSE_GOAL = ((935, 289, 90, True),
				 (935, 331, 90, True),
				 (935, 373, 90, True),
				 (935, 415, 90, True),
				 (935, 457, 90, True), 
				 (935, 499, 90, True))
	dic = {}
	nums = dotNode.request()
	for i in range(6):
		if nums[i] in range(1, 4):
			dic[nums[i]] = POSE_GOAL[i]

	for i in range(0, 3):
		baseNode.move(dic[i])
		upperNode.move(4)

	# # End of main loop
	##############################################################
