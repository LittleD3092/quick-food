# main_control Node
# !/usr/bin/env python
from AlphabetRecognize import AlphabetRecognize
from ColorDetect import ColorDetect
from DotRecognize import DotRecognize
from Navigation import Navigation
from UpperMechanism import UpperMechanism
from main_control.srv import main2nav, main2navRequest, main2navResponse
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

assert True # turn off this before race

if __name__ == '__main__':
	# init all nodes
	dotNode = DotRecognize()
	alphabetNode = AlphabetRecognize()
	ballNode = ColorDetect()
	baseNode = Navigation()
	upperNode = UpperMechanism()
	upperNode.move(0)


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