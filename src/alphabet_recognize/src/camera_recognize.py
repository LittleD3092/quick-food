import cv2
import numpy as np
import time
import os
import rospy
import sys
import pytesseract
from PIL import Image
from alphabet_recognize.srv import alphabetSrv,alphabetSrvResponse

KNOWN_DISTANCE = 59.05
KNOWN_WIDTH = 15.75
KNOWN_HEIGHT = 15.75

#################### SCAN FOR BOARD ##################

def nothing(a):
	pass

# from contours, get biggest
def get_biggest_contour(contours, mode = "paper"):
	biggest_contour = np.array([])
	max_area = 0
	if mode == "paper":
		for i in contours:
			area = cv2.contourArea(i)
			peri = cv2.arcLength(i, True)
			approx = cv2.approxPolyDP(i, 0.02 * peri, True)
			if area > max_area and len(approx) == 4 and area > 2000:
				biggest_contour = approx
				max_area = area
	else:
		for i in contours:
			area = cv2.contourArea(i)
			peri = cv2.arcLength(i, True)
			approx = cv2.approxPolyDP(i, 0.02 * peri, True)
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
	cv2.line(img, (points[0][0][0], points[0][0][1]), (points[1][0][0], points[1][0][1]), (0, 255, 0), thickness)
	cv2.line(img, (points[0][0][0], points[0][0][1]), (points[2][0][0], points[2][0][1]), (0, 255, 0), thickness)
	cv2.line(img, (points[3][0][0], points[3][0][1]), (points[2][0][0], points[2][0][1]), (0, 255, 0), thickness)
	cv2.line(img, (points[3][0][0], points[3][0][1]), (points[1][0][0], points[1][0][1]), (0, 255, 0), thickness)
 
	return img

# convert img to scanned document
def convert_to_flat(img):
	# print("function convert_to_flat called.")
	img_height, img_width, img_channel = img.shape

	# print("function convert_to_flat: flag 1")

	# pre processing
	# only white left
	img_white_left = img.copy()

	# print("function convert_to_flat: flag 2")

	# Threshold of blue in HSV space
	lower_black = np.array([0, 0, 0])
	upper_black = np.array([359, 128, 100])
	
	# print("function convert_to_flat: flag 3")

	# preparing the mask to overlay
	hsv = cv2.cvtColor(img_white_left, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_black, upper_black)
	mask = np.where(mask >= 128, 0, 255)
	mask = mask.astype(np.uint8)
	# cv2.imshow("convert_to_flat", mask)
	 
	# print("function convert_to_flat: flag 4")


	# The black region in the mask has the value of 0,
	# so when multiplied with original image removes all non-white regions
	img_white_left = cv2.bitwise_and(img_white_left, img_white_left, mask = mask)

	# print("function convert_to_flat: flag 5")

	# gray
	img_gray = cv2.cvtColor(img_white_left, cv2.COLOR_BGR2GRAY)
	# blur
	img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
	# canny
	threshold1, threshold2 = 200, 200
	img_canny = cv2.Canny(img_blur, threshold1, threshold2)
	kernel = np.ones((5, 5))
	img_dial = cv2.dilate(img_canny, kernel, iterations = 2)
	img_canny = cv2.erode(img_dial, kernel, iterations = 1)

	# print("function convert_to_flat: flag 6")

	# find contours
	# for display purposes
	img_contours = img.copy()
	contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

	# print("function convert_to_flat: flag 7")

	# cv2.imshow('contours', img_contours)
	# cv2.waitKey(0)

	# get biggest contour
	# for display purposes
	img_biggest_contour = img.copy()
	biggest_contour, max_area = get_biggest_contour(contours)

	# print("function convert_to_flat: flag 8")

	# get warp perspective image
	if biggest_contour.size == 0:
		# print("no document found")
		return 1
	
	# print("function convert_to_flat: flag 9")

	biggest_contour = reorder_contour(biggest_contour)
	cv2.drawContours(img_biggest_contour, biggest_contour, -1, (0, 255, 0), 20)
	img_biggest_contour = drawRectangle(img_biggest_contour, biggest_contour, 2)
	pts1 = np.float32(biggest_contour) # PREPARE POINTS FOR WARP
	pts2 = np.float32([[0, 0],[img_width, 0], [0, img_height],[img_width, img_height]]) # PREPARE POINTS FOR WARP
	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	img_warp_colored = cv2.warpPerspective(img, matrix, (img_width, img_height))

	# print("function convert_to_flat: flag 10")

	# get scanned paper
	# remove 20 pixels from each side
	img_warp_colored = img_warp_colored[20:img_warp_colored.shape[0] - 20, 20:img_warp_colored.shape[1] - 20]
	img_warp_colored = cv2.resize(img_warp_colored,(img_width, img_height))
	# # apply adaptive threshold
	# imgWarpGray = cv2.cvtColor(img_warp_colored,cv2.COLOR_BGR2GRAY)
	# imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
	# imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
	# imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre,3)

	# print("function convert_to_flat: flag 11")

	img_blank = np.zeros((img_height, img_width, 3))

	# print("function convert_to_flat: flag 12")

	img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
	img_blur = cv2.cvtColor(img_blur, cv2.COLOR_GRAY2BGR)
	img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2BGR)
	images = np.hstack([img_white_left, img_gray, img_blur, img_canny,	img_contours, img_biggest_contour, img_warp_colored])
	images = cv2.resize(images, (img_width * 7 // 3, img_height // 3))

	# cv2.imshow('flaten process', images)

	# return result
	# print("function convert_to_flat returned.")
	return img_warp_colored

######################################################

#################### GET ALPHABET ####################

def guess_alphabet(img):
	lastresult = ''

	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	kernel = np.ones((1, 1), np.uint8)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)
	tessdata_dir_config = ""
	if sys.platform.startswith('linux'):
		tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata/" --psm 10  --oem 3 '
	elif sys.platform.startswith('win32'):
		tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata" --psm 10  --oem 3 '
	arr = Image.fromarray(img)
	raw_result = pytesseract.image_to_string(arr, config = tessdata_dir_config)
	# print(result)
	result = ""
	for ch in raw_result:
		if ch.isalpha() and (ch == "T" or ch == 'D' or ch == 'K'):
			result += ch
	return result

######################################################

def detectpicture(send_message):
# read from camera
#     ret: whether capture is successful or not
#     frame: picture captured
	# print("function detectpicture called.")
	ret, frame = cap.read()
	# print("function detectpicture: picture read successfully.")
	# copy the frame
	img_flat = convert_to_flat(frame.copy())
	# print("function detectpicture: converted to flat.")
	alphabetRecognize = 0
	if type(img_flat) != type(int()):
		alphabetRecognize = guess_alphabet(img_flat)
		# print("I think it is \'", alphabetRecognize, "\'", sep='')
		if alphabetRecognize == 'T':
			send_message.alphabet_srv = 1
		elif alphabetRecognize == 'D':
			send_message.alphabet_srv = 2
		elif alphabetRecognize == 'K':
			send_message.alphabet_srv = 3
		else:
			send_message.alphabet_srv = 0
	else:
		# print("I can't recognize this alphabet")
		send_message.alphabet_srv = 0
	# print("function detectpicture: finish detection.")
	# print("function detectpictrue return with value: \n", send_message)
	return send_message


def alphabet_dict(var):
	return {
	'T': 1,
	'D': 2,
	'K': 3}.get(var,0)

# Precondition: image is a numpy array containing a picture with 3 channel.
# Postcondition: A countour of the detected square is returned.
def find_marker(image):
	gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将彩色图转化为灰度图
	gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)    # 高斯平滑去噪
	edged_img = cv2.Canny(gray_img, 35, 125)     # Canny算子阈值化
	# 获取纸张的轮廓数据
	countours, hierarchy = cv2.findContours(edged_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	# print(len(countours))
	# 获取最大面积对应的点集
	c = max(countours, key=cv2.contourArea)    
	# 最小外接矩形
	
	rect = cv2.minAreaRect(c)      
	return rect

def calculate_Distance(focalLength_value):
	# print("function calculate_Distance called with paramter focalLength_value =", focalLength_value)
	success,image = cap.read()
	# 获取矩形的中心点坐标，长度，宽度和旋转角度， marke[1][0]代表宽度
	marker = find_marker(image)     
	distance_cm = distance_to_camera(KNOWN_WIDTH, focalLength_value, marker[1][0])
	box = cv2.boxPoints(marker)
	# print("Box = ", box)
	
	center_x = (box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
	center_y = (box[0][1]+box[1][1]+box[2][1]+box[3][1])/4
	# print("x_diff:",center_x-320)
	x_diff = center_x-320
	box = np.int0(box)
	# print("Box = ", box)
	cv2.circle(image, (int(center_x),int(center_y)), 3, (1, 227, 254), -1)
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fcm" % (distance_cm),
			(image.shape[1] - 300, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
			2.0, (0, 0, 255), 3)          
#    cv.imshow("image", image)
#    waitKey(30)
#    print(distance_cm,"cm")

	# print("function calculate_Distance returned with value", distance_cm, x_diff)
	return distance_cm,x_diff


def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

# 计算摄像头的焦距（内参）
def calculate_focalDistance(video):
	# print("function calculate_focalDistance called.")    
	success,image = video.read()
	marker = find_marker(image)       
	# print("图片中A4纸的宽度：f%", marker[1][0])
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  
	# print('焦距 = ', focalLength)
	# print("function calculate_focalDistance has return value", focalLength)
	return focalLength

def main0(req):
	print("server called with argument", req)
	send_message = alphabetSrvResponse(alphabet_srv = 0, distance_srv = 0, x_diff_srv = 0)
	send_message = detectpicture(send_message)
	focalLength = calculate_focalDistance(cap)
	distance_cm, x_diff = calculate_Distance(focalLength)

	send_message.distance_srv = int(distance_cm)
	send_message.x_diff_srv = int(x_diff)

	if send_message.alphabet_srv not in range(1, 4):
		print("server responded with value: \n", alphabetSrvResponse(alphabet_srv = 0, distance_srv = 0, x_diff_srv = 0), end = "\n\n")
		return alphabetSrvResponse(alphabet_srv = 0, distance_srv = 0, x_diff_srv = 0)
	else:
		print("server responded with value: \n", send_message, end = "\n\n")
		return send_message

if __name__ == '__main__':
	# capture from camera, 0 means first camera attached
	cap = cv2.VideoCapture("/dev/video4")
	rospy.init_node('camera_recognize_services')
	s=rospy.Service('alphabet_recognize',alphabetSrv,main0)
	rospy.spin()