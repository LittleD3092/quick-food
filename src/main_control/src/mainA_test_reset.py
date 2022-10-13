# main_control Node
# !/usr/bin/env python3.6

import rospy
from std_msgs.msg import Empty, Int16, Bool
from nav.srv import main2nav, main2navRequest, main2navResponse
from color_detect_srvs.srv import colorSrv, colorSrvRequest, colorSrvResponse
from alphabet_recognize.srv import alphabetSrv, alphabetSrvRequest, alphabetSrvResponse
from upper_control.srv import action, actionRequest, actionResponse
from braille_recognize.srv import braille_request, braille_requestRequest, braille_requestResponse
# from main_control.msg import main_status
from motor_communicate.srv import bowling, bowlingRequest, bowlingResponse
# import time

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
			# if position[i] is too close to position[i+1],
			# delete position[i+1] and number[i + 1].
			i = 0
			# for j in range(len(resp.position) - 1):
				# if resp.position[i] + 10 >= resp.position[i + 1]:
				# 	del resp.position[i + 1]
				# 	del resp.number[i + 1]
				# 	i -= 1
				# i += 1
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
		assert len(req) == 4
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
	# alphabetNode = AlphabetRecognize()
	# ballNode = ColorDetect()
	baseNode = Navigation()
	upperNode = UpperMechanism()
	upperNode.move(0)

	print("moving to get bowling")
	baseNode.move((0, 150, 180, False))
	baseNode.move((220, 150, 180, True))
	baseNode.move((220, 158, 180, True))

	# take bowling three times
	print("taking bowling...")
	for i in range(3):
		upperNode.move(3)

	# go to H
	# baseNode.move((-895, 373, 270))
	print("reach red line")
	baseNode.move((220, 63, 180, False))

	# # release bowling to three goals marked in dot numbers
	BOWLING_GOAL_COOR = ((115, 63, 180, True),
				         (157, 63, 180, True),
				         (199, 63, 180, True),
				         (241, 63, 180, True),
				         (283, 63, 180, True), 
				         (324, 63, 180, True))

	# NOTE: Abandon dot recognize
	# ## scan for dot
	# dotResult = []

	# read_dot = True
	# dotNum = []
	# dotNum2 = []
	# dot_length = 0
	# dot_length2 = 0
	# check_length = 0
	# for atmp in range(3):
		
	# 	print("seeing dots...")
	# 	baseNode.move((283, 63, 180, True))
	# 	print("move to first place")
		
	# 	flag = False
		
	# 	while flag != True:
	# 		rospy.sleep(2.0)
	# 		dot_length, dotNum, dotPos = dotNode.request()
	# 		print(dotNum)
	# 		print(dotPos)
	# 		i = 0
	# 		flag = True
	# 		for i in range(len(dotNum) - 1):
	# 			if ((abs(dotPos[i] - dotPos[i + 1]) < 5) and (dotNum[i] != dotNum[i + 1])):
	# 				flag = False

	# 	print(f"dot num is {dotNum}")

	# 	print("seeing dots on the other side...")
	# 	baseNode.move((157, 63, 180, True))
	# 	print("move to 2nd place")
		
	# 	flag = False
	# 	while flag != True:
	# 		rospy.sleep(2.0)
	# 		dot_length2, dotNum2, dotPos2 = dotNode.request()
	# 		print(dotNum2)
	# 		print(dotPos2)
	# 		i = 0
	# 		flag = True
	# 		for i in range(len(dotNum2) - 1):
	# 			if ((abs(dotPos2[i] - dotPos2[i + 1]) < 5) and (dotNum2[i] != dotNum2[i + 1])):
	# 				flag = False

	# 	print(f"dot num2 is {dotNum2}")

	# 	if ((dot_length + dot_length2) < 6):
	# 		continue

	# 	check_length = (dot_length + dot_length2) - 6

	# 	if(dotNum[:check_length] == dotNum2[-1*check_length:]):
	# 		read_dot = False
		
	# 	if read_dot == False:
	# 		break
	# 	elif atmp == 2:
	# 		dotResult = [1, 2, 3, 4, 5, 6]

	# for ele in dotNum2:
	# 	dotResult.append(ele)
	# for i in range(check_length , len(dotNum)):
	# 	dotResult.append(dotNum[i])

	# print("dot result = ", dotResult, sep = "")

	baseNode.move(BOWLING_GOAL_COOR[3])
	for i in range(1, 4):
		# print("throwing to goal ", i, "...", sep = "")
		# for j in range(len(dotResult)):
		# 	if dotResult[j] == i:
		# 		baseNode.move(BOWLING_GOAL_COOR[j])
		# 		upperNode.move(4)
		# 		break
		upperNode.move(4)

	# going back to take basketball
	print("Going back to take basketball...")
	baseNode.move((220, 150, 180, False))
	baseNode.move((-20, 150, 180, False))
	baseNode.move((-20, 0, 180, False))
	baseNode.move((-170, 0, 180, False))
	baseNode.move((-170, 0, 90, False))
	baseNode.move((-170, -425, 90, True))
	baseNode.move((-72, -425, 90, True))

	print("taking basketball three times...")
	for i in range(3):
		upperNode.move(1)

	print("going to intersection...")
	baseNode.move((-170, -425, 90, False))
	baseNode.move((-170, 0, 90, False))
	baseNode.move((-170, 0, 0, False))
	baseNode.move((-220, 0, 0, True))
	baseNode.move((-220, 77, 0, True))
	upperNode.move(2)

	print("This program ended successfully.")

	# # # End of main loop
	##############################################################
