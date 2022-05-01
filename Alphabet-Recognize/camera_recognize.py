import cv2 as cv
import numpy as np
import pic_demo

if __name__ == '__main__':
	# capture from camera, 0 means first camera attached
	cap = cv.VideoCapture(0)

	while True:
		# read from camera
		#     ret: whether capture is successful or not
		#     frame: picture captured
		ret, frame = cap.read()

		img_flat = pic_demo.convert_to_flat(frame.copy())
		if type(img_flat) != type(1):
			frame = img_flat

		# copy the frame
		img2 = frame.copy()

		# full color --> gray
		gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)

		# gray -- 150 ~ 200 --> canny
		cny = cv.Canny(gray ,150 ,200)

		# get contour data from canny
		contours, hier = cv.findContours(cny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
		
		# draw contour
		for cnt in contours:
			cv.drawContours(img2, cnt, -1, (255, 0, 0), 4)
			peri = cv.arcLength(cnt, True)
			vertices = cv.approxPolyDP(cnt, peri * 0.02, True)
		
		mask = np.zeros(frame.shape, np.uint8)
		cv.drawContours(mask, contours, -1, 255, -1)
		pixelpoints = np.transpose(np.nonzero(mask))

		alphabet = pic_demo.guess_alphabet(pixelpoints)
		print("I think it is \'", alphabet, "\'", sep = '')

		cv.imshow('img2', img2)
		cv.waitKey(1)