# main_control Node
# !/usr/bin/env python3.6

import rospy
from std_msgs.msg import Empty, Int16, Bool
from navigation.srv import main2nav, main2navRequest, main2navResponse
from color_detect_srvs.srv import colorSrv, colorSrvRequest, colorSrvResponse
from alphabet_recognize.srv import alphabetSrv, alphabetSrvRequest, alphabetSrvResponse
from upper_control.srv import action, actionRequest, actionResponse
from braille_recognize.srv import braille_request, braille_requestRequest, braille_requestResponse
from motor_communicate.srv import bowling, bowlingRequest, bowlingResponse

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
		rospy.wait_for_service('braille_recognize', 5)
		try:
			dot_recognize = rospy.ServiceProxy('braille_recognize', braille_request)
			resp = dot_recognize(braille_requestRequest(req = 0))
			return resp.array_length, resp.number, resp.position
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
			if cmd == 3:
				StatusPublisher().request(True)
			elif cmd == 4:
				StatusPublisher().request(False)
			return resp.response
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1

class StatusPublisher:
	
	# Precondition: Nothing.
	# Postcondition: The object StatusPublisher is created.
	def __init__(self):
		pass

	# Precondition: Given a parameter status that indicates the current status.
	#               Now is a boolean value that is either true or false.
	#               True for the ball is in the upper mechanism.
	#               False for the ball is not in the upper mechanism.
	# Postcondition: Ping the server bowling_load to update the status.
	def request(self, status):
		rospy.wait_for_service('bowling_load', 5)
		try:
			bowling_load = rospy.ServiceProxy('bowling_load', bowling)
			resp = bowling_load(bowlingRequest(load = status))
			return resp.done
		except rospy.ServiceException as e:
			print("Service call failed: %s" %e)
			return -1
		

if __name__ == '__main__': # main for B field.
	# init all nodes, uncomment the node you needed
	dotNode = DotRecognize()
	alphabetNode = AlphabetRecognize()
	ballNode = ColorDetect()
	baseNode = Navigation()
	# upperNode = UpperMechanism()
	# statusPub = StatusPublisher()

	# test chassis
	# upperNode.move(0)
	# -36 x
	print("moving back...")
	baseNode.move((-36, 0, 180, False))
	# +85 y
	print("moving right...")
	baseNode.move((-36, 85, 180, True))

	# recognize and take ball
	# print("taking ball...")
	# qu = []
	# for i in range(3):
	# 	qu.append(ballNode.request())
	# 	upperNode.move(1)
	# print("current ball queue has: ", qu, sep = "")
	
	# -160 y
	print("moving left...")
	baseNode.move((-36, -75, 180, False))
	# heading 270 degree
	print("turning...")
	baseNode.move((-36, -75, 270, True))
	# +49 x
	print("moving forward...")
	baseNode.move((13, -75, 270, False))

	# scan alphabet
	print("scanning alphabet...")
	result = ()
	while len(result) != 2:
		_, _, result = alphabetNode.request()
	print("result = ", result, sep = "")


	# 85-124 y
	# 85-196 y
	# 85-266 y
	BASKET_POSE = [(13, -39, 270, True), (13, -111, 270, True), (13, -181, 270, True)]
	dic = {}
	alphabetLeft = 6
	for i in range(2):
		dic[result[i]] = BASKET_POSE[i + 1]
		alphabetLeft -= result[i]
	dic[alphabetLeft] = BASKET_POSE[0]
	print("basket dic = ", dic, sep = "")

	# print("throwing to corresponding basket...")
	# for ele in qu:
	# 	baseNode.move(dic[ele])
	# 	upperNode.move(2)

	dotResult = []

	print("moving back...")

	baseNode.move((-36, 85, 180, True))
	print("seeing dots...")
	dotNum = []
	while len(dotNum) != 3:
		_, dotNum, dotPos = dotNode.request()
		i = 0
		while i < len(dotNum) - 1:
			if abs(dotPos[i] - dotPos[i + 1]) < 5:
				dotNum.pop(i)
				dotPos.pop(i)
			else:
				i += 1

	dotResult = dotNum

	print("going to another side...")

	# -130 x
	baseNode.move((-166, 85, 180, True))
	print("seeing dots...")
	dotNum = []
	while len(dotNum) != 3:
		_, dotNum, dotPos = dotNode.request()
		i = 0
		while i < len(dotNum) - 1:
			if abs(dotPos[i] - dotPos[i + 1]) < 5:
				dotNum.pop(i)
				dotPos.pop(i)
			else:
				i += 1

	for i in dotNum:
		dotResult.append(i)

	print("dot result = ", dotResult, sep = "")