import cv2 as cv
import numpy as np
from math import sqrt
import time
from PIL import Image
import pytesseract
import sys

#################### SCAN FOR BOARD ##################

def nothing(a):
	pass

# from contours, get biggest
def get_biggest_contour(contours, mode = "paper"):
	biggest_contour = np.array([])
	max_area = 0
	if mode == "paper":
		for i in contours:
			area = cv.contourArea(i)
			peri = cv.arcLength(i, True)
			approx = cv.approxPolyDP(i, 0.02 * peri, True)
			if area > max_area and len(approx) == 4 and area > 2000:
				biggest_contour = approx
				max_area = area
	else:
		for i in contours:
			area = cv.contourArea(i)
			peri = cv.arcLength(i, True)
			approx = cv.approxPolyDP(i, 0.02 * peri, True)
			if area > max_area:
				biggest_contour = approx
				max_area = area
	return biggest_contour, max_area

# list of contour data need to be reorder
def reorder_contour(myPoints):
	myPoints = myPoints.reshape((4, 2))
	myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
	add = myPoints.sum(1)
 
	myPointsNew[0] = myPoints[np.argmin(add)]
	myPointsNew[3] = myPoints[np.argmax(add)]
	diff = np.diff(myPoints, axis=1)
	myPointsNew[1] = myPoints[np.argmin(diff)]
	myPointsNew[2] = myPoints[np.argmax(diff)]
 
	return myPointsNew

# draw rectangle based on the points
def drawRectangle(img,points,thickness):
	cv.line(img, (points[0][0][0], points[0][0][1]), (points[1][0][0], points[1][0][1]), (0, 255, 0), thickness)
	cv.line(img, (points[0][0][0], points[0][0][1]), (points[2][0][0], points[2][0][1]), (0, 255, 0), thickness)
	cv.line(img, (points[3][0][0], points[3][0][1]), (points[2][0][0], points[2][0][1]), (0, 255, 0), thickness)
	cv.line(img, (points[3][0][0], points[3][0][1]), (points[1][0][0], points[1][0][1]), (0, 255, 0), thickness)
 
	return img

# convert img to scanned document
def convert_to_flat(img):
	img_height, img_width, img_channel = img.shape

	# pre processing
	# only white left
	img_white_left = img.copy()



	# Threshold of blue in HSV space
	lower_black = np.array([0, 0, 0])
	upper_black = np.array([359, 128, 100])
	
	# preparing the mask to overlay
	hsv = cv.cvtColor(img_white_left, cv.COLOR_BGR2HSV)
	mask = cv.inRange(hsv, lower_black, upper_black)
	mask = np.where(mask >= 128, 0, 255)
	mask = mask.astype(np.uint8)
	cv.imshow("convert_to_flat", mask)
	 
	# The black region in the mask has the value of 0,
	# so when multiplied with original image removes all non-white regions
	img_white_left = cv.bitwise_and(img_white_left, img_white_left, mask = mask)

	# gray
	img_gray = cv.cvtColor(img_white_left, cv.COLOR_BGR2GRAY)
	# blur
	img_blur = cv.GaussianBlur(img_gray, (5, 5), 1)
	# canny
	threshold1, threshold2 = 200, 200
	img_canny = cv.Canny(img_blur, threshold1, threshold2)
	kernel = np.ones((5, 5))
	img_dial = cv.dilate(img_canny, kernel, iterations = 2)
	img_canny = cv.erode(img_dial, kernel, iterations = 1)

	# find contours
	# for display purposes
	img_contours = img.copy()
	contours, hierarchy = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	cv.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

	cv.imshow('contours', img_contours)
	# cv.waitKey(0)

	# get biggest contour
	# for display purposes
	img_biggest_contour = img.copy()
	biggest_contour, max_area = get_biggest_contour(contours)

	# get warp perspective image
	if biggest_contour.size == 0:
		print("no document found")
		return 1
	
	biggest_contour = reorder_contour(biggest_contour)
	cv.drawContours(img_biggest_contour, biggest_contour, -1, (0, 255, 0), 20)
	img_biggest_contour = drawRectangle(img_biggest_contour, biggest_contour, 2)
	pts1 = np.float32(biggest_contour) # PREPARE POINTS FOR WARP
	pts2 = np.float32([[0, 0],[img_width, 0], [0, img_height],[img_width, img_height]]) # PREPARE POINTS FOR WARP
	matrix = cv.getPerspectiveTransform(pts1, pts2)
	img_warp_colored = cv.warpPerspective(img, matrix, (img_width, img_height))

	# get scanned paper
	# remove 20 pixels from each side
	img_warp_colored = img_warp_colored[20:img_warp_colored.shape[0] - 20, 20:img_warp_colored.shape[1] - 20]
	img_warp_colored = cv.resize(img_warp_colored,(img_width, img_height))
	# # apply adaptive threshold
	# imgWarpGray = cv.cvtColor(img_warp_colored,cv.COLOR_BGR2GRAY)
	# imgAdaptiveThre = cv.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
	# imgAdaptiveThre = cv.bitwise_not(imgAdaptiveThre)
	# imgAdaptiveThre = cv.medianBlur(imgAdaptiveThre,3)

	img_blank = np.zeros((img_height, img_width, 3))

	img_gray = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
	img_blur = cv.cvtColor(img_blur, cv.COLOR_GRAY2BGR)
	img_canny = cv.cvtColor(img_canny, cv.COLOR_GRAY2BGR)
	images = np.hstack([img_white_left, img_gray, img_blur, img_canny,	img_contours, img_biggest_contour, img_warp_colored])
	images = cv.resize(images, (img_width * 7 // 3, img_height // 3))

	# cv.imshow('flaten process', images)

	# return result
	return img_warp_colored

######################################################

#################### GET ALPHABET ####################

def guess_alphabet(img):
	lastresult = ''

	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	kernel = np.ones((1, 1), np.uint8)
	img = cv.dilate(img, kernel, iterations=1)
	img = cv.erode(img, kernel, iterations=1)
	tessdata_dir_config = ""
	if sys.platform.startswith('linux'):
		tessdata_dir_config = r'--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata/" --psm 10  --oem 3 '
	elif sys.platform.startswith('win32'):
		tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata\" --psm 10  --oem 3 '
	arr = Image.fromarray(img)
	raw_result = pytesseract.image_to_string(arr, config = tessdata_dir_config)
	# print(result)
	result = ""
	for ch in raw_result:
		if ch.isalpha() and (ch == "T" or ch == 'D' or ch == 'K'):
			result += ch
	return result

######################################################

######################## MAIN ########################

if __name__ == '__main__':
	# read image from file
	img = cv.imread('pics/held_k.jpg')
	scale = 1
	while (not img.shape[0] / scale <= 480) and (not img.shape[1] / scale <= 640):
		scale += 1
	img = cv.resize(img, (img.shape[1] // scale, img.shape[0] // scale))
	#img = cv.imread('pics/k.png')

	cv.imshow('original', img)

	# convert image to flat
	img_flat = convert_to_flat(img)
	if type(img_flat) != type(int()):
		img = img_flat

	alphabet = guess_alphabet(img = img.copy())
	print("I think it is \'", alphabet, "\'", sep = '')

	cv.imshow('result', img)
	cv.waitKey(0)

######################################################