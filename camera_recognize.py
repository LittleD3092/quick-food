import cv2 as cv
import numpy as np
import pic_demo
import time
import os
import rospy
from std_msgs.msg import Int16MultiArray
def detectpicture():
# read from camera
#     ret: whether capture is successful or not
#     frame: picture captured
	ret, frame = cap.read()
    # copy the frame
	img_flat = pic_demo.convert_to_flat(frame.copy())

	if type(img_flat) != type(int()):
		alphabet = pic_demo.guess_alphabet(img_flat)
		print("I think it is \'", alphabet, "\'", sep='')
		match alphabet:
			case T:
				return 1
			case D:
				return 2
			case K:
				return 3
	else:
		print("I can't recognize this alphabet")
		return 0


if __name__ == '__main__':
	# capture from camera, 0 means first camera attached
    cap = cv.VideoCapture(2)
    rospy.init_node('camera_recognize_services')
	s=rospy.Serivce('alphabet_recognize',Int16MultiArray,detectpicture)
    rospy.spin()
    cv.waitKey(1)