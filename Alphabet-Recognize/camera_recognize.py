import cv2 as cv
import numpy as np
import pic_demo
import time
import os

if __name__ == '__main__':
	# capture from camera, 0 means first camera attached
	cap = cv.VideoCapture(2)

	while True:
		# read from camera
		#     ret: whether capture is successful or not
		#     frame: picture captured
		ret, frame = cap.read()
		# copy the frame
		img_flat = pic_demo.convert_to_flat(frame.copy())
		
		if type(img_flat) != type(int()):
			alphabet = pic_demo.guess_alphabet(img_flat)
			print("I think it is \'", alphabet, "\'", sep = '')
		else:
			print("I can't recognize this alphabet")
		cv.imshow('img', frame)

		cv.waitKey(1)