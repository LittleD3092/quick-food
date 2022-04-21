import numpy as np
import cv2 as cv


#################### FIND CORNERS ####################
# return a picture of dots representing corners
def detect_corner(img):
	# convert the image to gray
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	# convert the numbers in gray to float
	# cv.cornerHarris() needs float image
	gray = np.float32(gray)

	# detect corners
	dst = cv.cornerHarris(gray, 2, 3, 0.04)
	dst = cv.dilate(dst, None)

	return dst

######################################################


#################### SCAN FOR BOARD ##################

def nothing(a):
	pass

# initialize trackbars for canny
def initialize_trackbars():
	cv.namedWindow("Trackbars")
	cv.resizeWindow("Trackbars", 360, 240)
	cv.createTrackbar("Threshold1", "Trackbars", 200, 255, nothing)
	cv.createTrackbar("Threshold2", "Trackbars", 200, 255, nothing)

# get trackbars for canny
def get_trackbars_value():
	threshold1 = cv.getTrackbarPos("Threshold1", "Trackbars")
	threshold2 = cv.getTrackbarPos("Threshold2", "Trackbars")
	return (threshold1, threshold2)

def get_biggest_contour(contours):
	biggest_contour = np.array([])
	max_area = 0
	for i in contours:
		area = cv.contourArea(i)
		if area > 5000:
			peri = cv.arcLength(i, True)
			approx = cv.approxPolyDP(i, 0.02 * peri, True)
			if area > max_area and len(approx) == 4:
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

	img_blank = np.zeros((img_height, img_width, img_channel), np.uint8)

	# pre processing
	# gray
	img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	# blur
	img_blur = cv.GaussianBlur(img_gray, (5, 5), 1)
	# canny
	threshold1, threshold2 = get_trackbars_value()
	img_threshold = cv.Canny(img_blur, threshold1, threshold2)
	kernel = np.ones((5, 5))
	img_dial = cv.dilate(img_threshold, kernel, iterations = 2)
	img_threshold = cv.erode(img_dial, kernel, iterations = 1)

	# find contours
	# for display purposes
	img_contours = img.copy()
	contours, hierarchy = cv.findContours(img_threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	cv.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

	cv.imshow('contours', img_contours)

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
	imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
	imgWarpColored = cv.resize(imgWarpColored,(img_width, img_height))
	# apply adaptive threshold
	imgWarpGray = cv.cvtColor(imgWarpColored,cv.COLOR_BGR2GRAY)
	imgAdaptiveThre = cv.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
	imgAdaptiveThre = cv.bitwise_not(imgAdaptiveThre)
	imgAdaptiveThre = cv.medianBlur(imgAdaptiveThre,3)

	# return result
	return imgAdaptiveThre

######################################################


####################### MAIN #########################

if __name__ == '__main__':
	# set filename to the picture location and import image
	filename = '../pics/T.png'
	# filename = '../pics/T.png'
	img = cv.imread(filename)

	# # scan document
	# initialize_trackbars()
	# img = convert_to_flat(img)
	# # show scanned document
	# cv.imshow('scanned', img)
	# cv.waitKey(0)

	# detect corners
	dst = detect_corner(img)

	# make red dot on corners and show picture
	img[dst > 0.01 * dst.max()] = [0, 0, 255]
	cv.imshow('dst', img)
	cv.waitKey(0)

######################################################