import cv2
import numpy as np
import pic_demo
import time
import os
import rospy
from alphabet_recognize.srv import alphabetSrv,alphabetSrvResponse

KNOWN_DISTANCE = 59.05
KNOWN_WIDTH = 15.75
KNOWN_HEIGHT = 15.75

def detectpicture(send_message):
# read from camera
#     ret: whether capture is successful or not
#     frame: picture captured

	ret, frame = cap.read()
	# copy the frame
	img_flat = pic_demo.convert_to_flat(frame.copy())
	alphabetRecognize = 0
	if type(img_flat) != type(int()):
		alphabetRecognize = pic_demo.guess_alphabet(img_flat)
		print("I think it is \'", alphabetRecognize, "\'", sep='')
		if alphabetRecognize == 'T':
			send_message.alphabet_srv = 1
		elif alphabetRecognize == 'D':
			send_message.alphabet_srv = 2
		elif alphabetRecognize == 'K':
			send_message.alphabet_srv = 3
		else:
			send_message.alphabet_srv = 0
	else:
		print("I can't recognize this alphabet")
		send_message.alphabet_srv = 0
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

def calculate_Distance(focalLength_value,send_message):
	success,image = cap.read()
	# 获取矩形的中心点坐标，长度，宽度和旋转角度， marke[1][0]代表宽度
	marker = find_marker(image)     
	distance_cm = distance_to_camera(KNOWN_WIDTH, focalLength_value, marker[1][0])
	send_message.data[1] = distance_cm
	box = cv2.boxPoints(marker)
	# print("Box = ", box)
	
	center_x = (box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
	center_y = (box[0][1]+box[1][1]+box[2][1]+box[3][1])/4
	print("x_diff:",center_x-320)
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
	return distance_cm,x_diff


def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

# 计算摄像头的焦距（内参）
def calculate_focalDistance(video):    
	success,image = video.read()
	marker = find_marker(image)       
	print("图片中A4纸的宽度：f%", marker[1][0])
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  
	print('焦距 = ', focalLength)        
	return focalLength

def main0(req):
	send_message = alphabetSrvResponse(alphabet_srv = 0, distance_srv = 0, x_diff_srv = 0)
	send_message = detectpicture(send_message)
	focalLength = calculate_focalDistance(cap)
	distance_cm, x_diff = calculate_Distance(focalLength,send_message)

	send_message.distance_srv = int(distance_cm)
	send_message.x_diff_srv = int(x_diff)

	return send_message


if __name__ == '__main__':
	# capture from camera, 0 means first camera attached
	cap = cv2.VideoCapture(2)
	rospy.init_node('camera_recognize_services')
	s=rospy.Service('alphabet_recognize',alphabetSrv,main0)
	rospy.spin()