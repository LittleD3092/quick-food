from tokenize import Number
from unittest import result
from urllib import response
import rospy
from braille_recognize.srv import braille_request,braille_requestResponse
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

def calculate_circle(img):
	n=[]
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	(a,b,c)=img.shape
	
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20, param1=100, param2=30, minRadius=1, maxRadius=100)
	
	if circles is None:
		return 0
		
	else :
		for circle in circles[0]:
			# 座標行列
			x = int(circle[0])
			y = int(circle[1])
			# 半徑
			r = int(circle[2])
			# 在原圖用指定顏色標記出圓的位置
			img = cv2.circle(img, (x, y), r, (0, 0, 255), 3)
			return (len(circles[0]))


def get_result(img):
	
	(a,b,c)=img.shape #get (列，行，3通道）
	x=int(b*0.5) #右半邊圖的初始座標
	y=int(b*0.73)
	p=int(a*0.36)
	q=int(a*0.8)
	
	img1 = img[0:a,x:y] #表示方式[列：列，行：行]
	area1=calculate_circle(img1)
	# print("left=",area1)
			
	img2 = img[0:a,y:b]
	area2=calculate_circle(img2)
	# print("right=",area2)
				
	img3 = img[0:p,x:b]
	area3=calculate_circle(img3)
	# print("up=",area3)

	img4 = img[p:q,x:b]
	area4=calculate_circle(img4)
	# print("middle=",area4)
		
	img5 = img[0:a,x:b]
	area5=calculate_circle(img5)
	# print("all=",area5)

			
	if(area5 == 0):
		return None
	
		
	if area2==0:
		if area1==1:
			# print("此點字為1")
			return 1
		else:
			# print("此點字為2")
			return 2

	elif area2==1:
		if area1==2 :
			# print("此點字為6")
			return 6
		elif area1==1 and area3==1:
			# print("此點字為5")
			return 5
		else:
			# print("此點字為3")
			return 3
	else:
		# print("此點字為4")
		return 4
		
def braille_callback(request):
	
	print("---------------",end="\n\n")
	_ , img = cap.read()

	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	rec_contour=[]
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# cv2.imshow('gray', gray)
	# cv2.waitKey(0)
	# cv2.destroyWindow('gray')
	
	# setting threshold of gra		# displaying the image after drawing contours
			#cv2.imshow('shapes', img)y image
	#_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	#blurred
	
	kernel = np.ones((5,5),np.float32)/25
	blur = cv2.filter2D(gray.copy(),-1,kernel)
	
	
	# blur_origin = cv2.GaussianBlur(gray,(5,5), 0)
	# _ , blur = cv2.threshold(blur_origin, 130, 255, cv2.THRESH_BINARY)
	
	# cv2.imshow("blur", blur)
	# cv2.waitKey(0)
	# cv2.destroyWindow('blur')
	
	#canny
	canny_img = cv2.Canny(blur, 20, 160)

	# cv2.imshow('canny', canny_img)
	# cv2.waitKey(0)
	# cv2.destroyWindow('canny')
	
	# using a findContours() function
	contours, _ = cv2.findContours(canny_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	print("contours number :")
	print(len(contours))

	# cv2.drawContours(img, contours, -1, (0,0,255), 2)
	# cv2.imshow('contours', img)
	# cv2.waitKey(0)
	# cv2.destroyWindow('contours')
	
	for contour in contours:
		#find width/height=39/29=1.34
		x,y,w,h = cv2.boundingRect(contour)

		aspect_ratio = float(w)/h
		rect_area = w*h
		
		if (aspect_ratio<2 and 1<aspect_ratio and rect_area > 10000):
			rec_contour.append(contour)


	print(f"number of rec_contour {len(rec_contour)}")

	count = 0
	recognize_result = [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1]]

	

	if rec_contour is not None:

		for contour in rec_contour:
			count += 1
			# using drawContours() function
			# img_copy = img.copy()
			# cv2.drawContours(img_copy, rec_contour, (count - 1), (0, 0, 255), 2)


			x,y,w,h = cv2.boundingRect(contour)
			
			#img after cutting
			pts1 = np.float32([[x,y],[x+w,y],[x,y+h],[x+w,y+h]])
			pts2 = np.float32([[0,0],[390,0],[0,290],[390,290]])
			M=cv2.getPerspectiveTransform(pts1,pts2)
			dst=cv2.warpPerspective(img.copy(),M,(390,290))

			# cv2.imshow('dst', dst)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

			dot_number = get_result(dst)
			dot_position = x+(w/2)
			
			print(f"{dot_number} {dot_position}")

			if(dot_number != None):
				if(recognize_result[dot_number - 1][1] == -1):
					recognize_result[dot_number - 1][1] = dot_position
				elif(recognize_result[dot_number - 1][1] > dot_position):
					recognize_result[dot_number - 1][1] = dot_position
					
	result_number = []
	result_position = []
	count = 0

	for i in recognize_result:
		if(i[1] != -1):
			count += 1
			result_number.append(int(i[0]))
			result_position.append(int(i[1]))

	for i in range(len(result_number)):
		for j in range(len(result_number) - 1):
			if(result_position[j] > result_position[j+1]):
				temp = result_position[j+1]
				result_position[j+1] = result_position[j]
				result_position[j] = temp

				temp = result_number[j+1]
				result_number[j+1] = result_number[j]
				result_number[j] = temp

	response_msg = braille_requestResponse()
	response_msg.array_length = count
	response_msg.number = result_number
	response_msg.position = result_position



	return response_msg

		
if __name__ == "__main__":
	rospy.init_node('braille_recognize')
	braille_server = rospy.Service('braille_recognize', braille_request, braille_callback)
	rospy.spin()
	cap.release()


		
		

