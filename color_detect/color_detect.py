import cv2
import numpy as np
import rospy
from std_msgs.msg import Int16MutiArray,MultiArrayLayout,MultiArrayDimension

KNOWN_DISTANCE = 59.05
KNOWN_WIDTH = 15.75
KNOWN_HEIGHT = 15.75

LOWER_ORANGE = np.array([10,60,46])
UPPER_ORANGE = np.array([15,255,255])

LOWER_BLUE = np.array([100,90,20])
UPPER_BLUE = np.array([124,255,255])

LOWER_BLACK = np.array([0,0,0])
UPPER_BLACK = np.array([180,100,80])

# Precondition: image is a BGR image in numpy array format.
# Postcondition: return the color (which equals 1) if the orange color is found, otherwise return 0.
def find_orange_object(img):
	image  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask_orange = cv2.inRange(image,LOWER_ORANGE,UPPER_ORANGE) #過濾顏色
	orange = cv2.bitwise_and(img,img,mask=mask_orange) #設定藍色遮罩

	contours, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
	if len(contours) > 20 :
		for contour in contours:
			if cv2.contourArea(contour) > 20000 :
				x,y,w,h = cv2.boundingRect(contour)
				cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
				color = 1
				print(color)
				return color
			else:
				color = 0
				return color,"can't find orange object"
 
# Precondition: image is a BGR image in numpy array format.
# Postcondition: return the color (which equals 2) if the blue color is found, otherwise return 0.
def find_blue_object(img): 
	image  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask_blue = cv2.inRange(image,LOWER_BLUE,UPPER_BLUE) 
	blue = cv2.bitwise_and(img,img,mask=mask_blue) 

	contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
	if len(contours) > 20 :
		for contour in contours:
			if cv2.contourArea(contour) > 20000 :
				x,y,w,h = cv2.boundingRect(contour)
				cv2.rectangle(img, (x,y),(x+w,y+h),(150,160,0),3)
				color = 2
				print(color)
				return color
			else:
				color = 0
				return color,"can't find blue object"
 

# Precondition: image is a BGR image in numpy array format.
# Postcondition: return the color (which equals 3) if the black color is found, otherwise return 0.
def find_black_object(img):
	image  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask_black = cv2.inRange(image,LOWER_BLACK,UPPER_BLACK) 
	black = cv2.bitwise_and(img,img,mask=mask_black) 

	contours, hierarchy = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
	if len(contours) > 20 :
		for contour in contours:
			if cv2.contourArea(contour) > 20000 :
				x,y,w,h = cv2.boundingRect(contour)
				cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,0),3) 
				color = 3
				print(color)
				return color
<<<<<<< HEAD
			else:
				color = 0
				return color,"can't find black object"
 

=======

# Precondition: image is a BGR image in numpy array format.
# Postcondition: return the countour of the rectangle found.
>>>>>>> fa269580c5c93704b7d60bbb4dbc5a8ee67bfc12
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


# 定义距离函数
# Precondition: knownWidth is the width of the object in the image.
#               focalLength is the focal length of the camera.
#               perWidth is the width of the object in the real world.
# Postcondition: return the depth of the object in the image.
def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

# 计算摄像头的焦距（内参）
# Precondition: video is the video stream from the camera.
# Postcondition: return the focal length of the camera.
def calculate_focalDistance(video):    
	success,image = video.read()
	marker = find_marker(image)       
	print("图片中A4纸的宽度：f%", marker[1][0])
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  
	print('焦距 = ', focalLength)        
	return focalLength


# 计算摄像头到物体的距离
# Precondition: focalLength_value is the focalLength in type float.
# Postcondition: return the depth of the object and the horizontal distance 
#                from the object to the middle of the screen.
def calculate_Distance(focalLength_value):
	success,image = video.read()
	# 获取矩形的中心点坐标，长度，宽度和旋转角度， marke[1][0]代表宽度
	marker = find_marker(image)     
	distance_cm = distance_to_camera(KNOWN_WIDTH, focalLength_value, marker[1][0])
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
	cv2.imshow("image", image)
	# waitKey(30)
	print(distance_cm,"cm")
	return distance_cm,x_diff

# Precondition: req is the request from the client. This function is called 
#               only when the client requests the server to do something.
#               This function acts as a callback function.
# Postcondition: Return the message to the client. The message is in Int16MultiArray format.
def main0(req):
	success,image = video.read()
	color = 0
	color = find_blue_object(image)
	color = find_orange_object(image)
	color = find_black_object(image)
	if color == 0 :
		return "color not found" 
	focalLength = calculate_focalDistance(video)  	#測試用 之後要寫死
	distance,x_diff = calculate_Distance(focalLength)
	message = Int16MutiArray(data =[color,distance,x_diff],layout = MultiArrayLayout(
							 dim = [MultiArrayDimension(label = "data",size =3,stride =1)],data_offset = 0))
	
	return message

if __name__ == "__main__":
	video = cv2.VideoCapture("/dev/video4") 

	rospy.init_node = ("color_detect_server")
	s = rospy.service("color_detect",Int16MutiArray,main0)
	rospy.spin()
