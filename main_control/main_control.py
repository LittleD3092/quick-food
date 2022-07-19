# main_control Node
# !/usr/bin/env python
import rospy
from std_msgs.msg import String
from AlphabetRecognize import AlphabetRecognize
from ColorDetect import ColorDetect
from DotRecognize import DotRecognize
from Navigation import Navigation
from Pose import Pose
from UpperMechanism import UpperMechanism

POSE_B = Pose(870,  170, 0, 0, 0, 0, 0)
POSE_I = Pose(425,  100, 0, 0, 0, 0, 0)
POSE_G = Pose(870,  0,   0, 0, 0, 0, 0)
POSE_J = Pose(1000, 390, 0, 0, 0, 0, 0)
POSE_H = Pose(1000, 390, 0, 0, 0, 0, 0)

if __name__ == '__main__':
	# init all nodes
	dotNode = DotRecognize()
	alphabetNode = AlphabetRecognize()
	ballNode = ColorDetect()
	baseNode = Navigation()
	upperNode = UpperMechanism()

	# go to I
	baseNode.move()

	# take basketball three times

	# go to G

	# throw the basketballs to three baskets marked T, D, K

	# go to B (checkpoint)

	# go to J

	# take bowling three times

	# go to H

	# release bowling to three goals marked in dot numbers