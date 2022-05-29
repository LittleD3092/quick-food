# import the necessary packages
import numpy as np
import cv2
import imutils
from skimage.filters import threshold_local
def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect
def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped
def convert_to_flat(img):
	img_height, img_width, img_channel = img.shape

	# pre processing
	# only white left
	img_white_left = img.copy()



	# Threshold of blue in HSV space
	lower_white = np.array([0, 0, 190])
	upper_white = np.array([359, 20, 255])
	
	# preparing the mask to overlay
	hsv = cv2.cvtColor(img_white_left, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_white, upper_white)
	 
	# The black region in the mask has the value of 0,
	# so when multiplied with original image removes all non-white regions
	img_white_left = cv2.bitwise_and(img_white_left, img_white_left, mask = mask)

	# gray
	img_gray = cv2.cvtColor(img_white_left, cv2.COLOR_BGR2GRAY)
	# blur
	img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)

	# canny
	threshold1, threshold2 = 200,200
	img_threshold = cv2.Canny(img_blur, threshold1, threshold2)
	kernel = np.ones((5, 5))
	img_dial = cv2.dilate(img_threshold, kernel, iterations = 2)
	img_threshold = cv2.erode(img_dial, kernel, iterations = 1)
	return img_threshold

#=========================================================================================================	
if __name__ == '__main__':
	image = cv2.imread('pics/held_t.jpg')
	img_T = cv2.imread('pics/T.jpg')
	img_T=cv2.resize(img_T, (332, 320), interpolation=cv2.INTER_AREA)
	img_T=convert_to_flat(img_T)
	cv2.imshow('img_T',imutils.resize(img_T, height = 650))
	#img_T = cv2.adaptiveThreshold(img_T,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,10)
	#cv2.imshow('img_T',imutils.resize(img_T, height = 650))
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image=convert_to_flat(image)
	edged = imutils.resize(image, height = 500)
# convert the image to grayscale, blur it, and find edges
# in the image

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
# loop over the contours
	for c in cnts:
	# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break
	
	
	warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
# convert the warped image to grayscale, then threshold it
# to give it that 'black and white' paper effect
	warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	T = cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,11)
	
	warped = (warped > T).astype("uint8") * 255
# show the original and scanned images
	print("STEP 3: Apply perspective transform")
	size=warped.shape
	print(size)
	#dst=cv2.bitwise_xor(warped,img_T)
	cv2.imshow("Original", imutils.resize(orig, height = 650))
	cv2.imshow("Scanned", imutils.resize(warped, height = 650))
	#cv2.imshow("xor", imutils.resize(dst, height = 650))
	cv2.waitKey(0)
	