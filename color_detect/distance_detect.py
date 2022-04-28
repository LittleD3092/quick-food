import numpy as np
import cv2
import time
import sys

class detect():
	def __init__(self):
		###### camera stream ######


		### debug ###
		#self.cap = cv2.imread('japan.png')
		#self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		#self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

		###### Bonding Object ######
		self.lower_orange = np.array([11, 101, 191])
		self.upper_orange = np.array([25, 255, 255])
		self.lower_blue = np.array([100, 43, 46])
		self.upper_blue = np.array([124, 255, 255])
		self.lower_black = np.array([0, 0, 0])
		self.upper_black = np.array([180, 255, 46])
		
		self.contour_area = 0
		self.kernel = np.ones((9,9), np.uint8)

		###### Logi C310 camera intrinsics parameters #######
		self.fx = 2338.288579
		self.fy = 2541.176562
		self.cx = 360.603613
		self.cy = 329.567096
		self.obj_real_width = 39.84
		self.intrinsic_matrix = np.array([[self.fx,       0, self.cx],
										  [      0, self.fy, self.cy],
										  [      0,       0,       1]])
		try :
			self.inverse_intrinsic_matrix = np.linalg.inv(self.intrinsic_matrix)
		except:
			sys.exit("intrinsic matrix doesn't have a inverse matrix.")
			print("intrinsic matrix doesn't have a inverse matrix.")

	def cv_update(self):    
		self.cap = cv2.VideoCapture('/dev/video4')
		self.cap.set(cv2.CAP_PROP_FPS,30)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
		self.time1 = time.time()
		self.time2 = time.time()

	def find_contours(self):
		ret, self.frame = self.cap.read()
		#self.frame = self.cap
		hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
		self.mask = cv2.inRange(hsv, self.lower_orange, self.upper_orange) ##
		self.denoise_mask = cv2.morphologyEx(self.mask, cv2.MORPH_OPEN, self.kernel)
		self.res = cv2.bitwise_and(self.frame, self.frame, mask = self.denoise_mask)
		gray = cv2.cvtColor(self.res, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (5, 5), 0)
		self.binary_img = cv2.Canny(blur, 20, 160)
		self.contours = cv2.findContours(self.binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	
	def bound_contours(self):
		#find the biggist obj
		for c in self.contours:
			area = cv2.contourArea(c)
			if area > self.contour_area:
				self.contour_area = area
				contour = c
				
		# if target is found by camera, draw the position information on frame.
		if len(self.contours) > 0 :
			(x, y, self.w, self.h) = cv2.boundingRect(contour)
			cv2.rectangle(self.frame, (x,y), (x+self.w, y+self.h), (0, 255, 0), 2)
			self.x = x + self.w / 2
			self.y = y + self.h / 2
			cv2.circle(self.frame, (int(self.x), int(self.y)), 10, (1, 277, 254), -1)
			print("object's (x, y) in pixel = ({x}, {y})".format(x = self.x, y = self.y))	

		# zero the contour_area
		self.contour_area = 0

	def show_result(self):
		cv2.imshow('frame', self.frame)

	def real_coordinate(self):
		try:
			rz = (self.fx / self.w) * self.obj_real_width
			rx = (self.x - self.cx) * rz / self.fx
			ry = (self.y - self.cy) * rz / self.fy
			print(rx, ry, rz)
		except:
			print("line 87:no contour found")

	def check(self):
		if len(self.contours) > 0:
			return True
		else:
			return False

	def object_camera_coordinate(self):
		# calculate the camera coordinate by triangle similarity theorem
		camera_coordinate_z = (self.fx / self.w) * self.obj_real_width
		camera_coordinate_x = (self.x - self.cx) * camera_coordinate_z / self.fx
		camera_coordinate_y = (self.y - self.cy) * camera_coordinate_z / self.fy

		# record position information
		# data = Point()
		# data.x = camera_coordinate_x
		# data.y = camera_coordinate_y
		# data.z = camera_coordinate_z
		# return data
	
	def object_detect(self):
		self.find_contours()
		self.bound_contours()
		self.show_result()
		self.real_coordinate()

	def caprel(self):
		self.cap.release()

	def FPS_estimator(self):
		self.time1 = self.time2
		self.time2 = time.time()
		duration = self.time2 - self.time1
		print("FPS : %f" %(1 / duration))

if __name__ == "__main__":
	d = detect()
	while True:
		d.cv_update()
		d.object_detect()
		#d.show_result()
		d.FPS_estimator()
		if cv2.waitKey(50) & 0xFF == ord('q'):
			break
		d.caprel()