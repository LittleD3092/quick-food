import cv2 as cv
import numpy as np
from math import sqrt

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
			if area > max_area and len(approx) == 4:
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
	lower_white = np.array([0, 0, 190])
	upper_white = np.array([359, 20, 255])
	
	# preparing the mask to overlay
	hsv = cv.cvtColor(img_white_left, cv.COLOR_BGR2HSV)
	mask = cv.inRange(hsv, lower_white, upper_white)
	 
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

	# cv.imshow('contours', img_contours)
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

	cv.imshow('flaten process', images)

	# return result
	return img_warp_colored

######################################################

#################### GET ALPHABET ####################

def get_max_y(dots):
	max_y = 0
	for dot in dots:
		if dot[0] > max_y:
			max_y = dot[0]
	return max_y

def get_min_y(dots):
	min_y = 100000
	for dot in dots:
		if dot[0] < min_y:
			min_y = dot[0]
	return min_y

def filter_max_min_y(dots, max_y, min_y):
	new_dots = np.zeros((1, 2))
	init = False
	for dot in dots:
		if ( dot[0] > (max_y - 5) or dot[0] < (min_y + 5) ) and init:
			new_dots = np.append(new_dots, np.reshape(dot, (1, 2)), axis = 0)
		elif dot[0] > (max_y - 5) or dot[0] < (min_y + 5):
			new_dots[0][0], new_dots[0][1] = dot[0], dot[1]
			init = True
	return new_dots

def distance_between_dots(dot1, dot2):
	dot1_x = dot1[0]
	dot1_y = dot1[1]
	dot2_x = dot2[0]
	dot2_y = dot2[1]
	distance = sqrt( (dot2_x - dot1_x) ** 2 + (dot2_y - dot1_y) ** 2)

	return distance

def organize_group(group = []):
	group_size = len(group)
	max_num = max(group)
	num_of_groups = 0
	iterator = 0
	while iterator <= max_num:
		if iterator in group:
			for i in range(group_size):
				if group[i] == iterator:
					group[i] = num_of_groups
			num_of_groups += 1
		iterator += 1
	return group

def avg_of_cluster(dots, cluster_group):
	num_of_groups = max(cluster_group) + 1
	num_of_dots = np.shape(dots)[0]
	avg_dots = []
	for group in range(num_of_groups):
		group_x_sum = 0
		group_y_sum = 0
		group_size = 0
		for i in range(num_of_dots):
			if group == cluster_group[i]:
				group_x_sum += dots[i][0]
				group_y_sum += dots[i][1]
				group_size += 1
		group_x_avg = group_x_sum // group_size
		group_y_avg = group_y_sum // group_size
		avg_dots.append([group_x_avg, group_y_avg])

	return avg_dots

def std_deviation_of_cluster(dots, cluster_group):
	num_of_groups = max(cluster_group) + 1
	num_of_dots = np.shape(dots)[0]
	std_deviation_list = []
	avg_dots = avg_of_cluster(dots, cluster_group)
	for group in range(num_of_groups):
		std_deviation = 0
		group_size = 0
		for i in range(num_of_dots):
			if group == cluster_group[i]:
				dot_x = dots[i][0]
				dot_y = dots[i][1]
				dot_avg_x = avg_dots[group][0]
				dot_avg_y = avg_dots[group][1]
				std_deviation += (dot_x - dot_avg_x) ** 2 + (dot_y - dot_avg_y) ** 2
				group_size += 1
		std_deviation = sqrt(std_deviation / group_size)
		std_deviation_list.append(std_deviation)
	return std_deviation_list

def merge_cluster(dots):
	# return cluster info
	# average point for each cluster
	# standard deviation of cluster

	# asign group to dots, each group is a cluster
	cluster_group = []
	for i in range(np.shape(dots)[0]):
		cluster_group.append(i)

	for i in range(np.shape(dots)[0]):
		for j in range(i + 1, np.shape(dots)[0]):
			if(distance_between_dots(dots[i], dots[j]) < 10):
				merge_to = cluster_group[i]
				merge_from = cluster_group[j]
				for k in range(np.shape(dots)[0]):
					if cluster_group[k] == merge_from:
						cluster_group[k] = merge_to

	cluster_group = organize_group(cluster_group)

	# get average point
	avg_points = avg_of_cluster(dots, cluster_group)

	# get standard deviation
	std_deviation = std_deviation_of_cluster(dots, cluster_group)

	return avg_points, std_deviation

def guess_alphabet(dots, img = None):
	max_y = get_max_y(dots)
	min_y = get_min_y(dots)

	dots = filter_max_min_y(dots, max_y, min_y)
	feature_points, std_deviation = merge_cluster(dots)

	try:
		for dot in dots:
			cv.circle(img,(int(dot[1]), int(dot[0])), 1, (0, 0, 255), -1)
		for dot in feature_points:
			cv.circle(img,(int(dot[1]), int(dot[0])), 5, (0, 255, 0), -1)
		cv.imshow('guess alphabet', img)
	except:
		pass
		

	num_of_verticle_lines = 0
	max_ratio_of_std_deviation = 0.0
	for i in range(len(feature_points)):
		for j in range(i + 1, len(feature_points)):
			point1_y = feature_points[i][0]
			point1_x = feature_points[i][1]
			point2_y = feature_points[j][0]
			point2_x = feature_points[j][1]
			if abs(point1_x - point2_x) < 20:
				num_of_verticle_lines += 1
			try:
				if max(std_deviation[i], std_deviation[j]) / min(std_deviation[i], std_deviation[j]) > max_ratio_of_std_deviation:
					max_ratio_of_std_deviation = max(std_deviation[i], std_deviation[j]) / min(std_deviation[i], std_deviation[j])
			except:
				print(std_deviation)
				print(i, j, len(feature_points))
				exit()

	if num_of_verticle_lines == 2:
		return "K"
	elif max_ratio_of_std_deviation > 2 and num_of_verticle_lines == 1:
		return "T"
	elif max_ratio_of_std_deviation <= 2 and num_of_verticle_lines == 1:
		return "D"
	else:
		return "?"
	


######################################################

######################## MAIN ########################

if __name__ == '__main__':
	# read image from file
	img = cv.imread('pics/held_k.jpg')
	#img = cv.imread('pics/k.png')

	cv.imshow('original', img)

	# convert image to flat
	img_flat = convert_to_flat(img)
	if type(img_flat) != type(1):
		img = img_flat

	img2 = img.copy()
	# image --> gray -- 150~200 --> canny
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	canny = cv.Canny(img, 150, 200)

	# get contour data from canny
	contours, hier = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

	# draw contour
	for cnt in contours:
		cv.drawContours(img2, cnt, -1, (255, 0, 0), 3)
		peri = cv.arcLength(cnt, True)
		vertices = cv.approxPolyDP(cnt, peri * 0.02, True)
		# print(len(vertices))

	mask = np.zeros(img.shape,np.uint8)
	cv.drawContours(mask,contours,-1,255,-1)
	pixelpoints = np.transpose(np.nonzero(mask))

	alphabet = guess_alphabet(pixelpoints, img = img2.copy())
	print("I think it is \'", alphabet, "\'", sep = '')

	cv.imshow('result', img2)
	cv.waitKey(0)

######################################################