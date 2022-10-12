from turtle import width
import cv2
import numpy as np

def sharpen(img, sigma=100):    
	# sigma = 5、15、25
	blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
	usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)

	return usm

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
		return img

def get_contours(img):
	rec_contour=[]
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	canny = cv2.Canny(gray, 50, 150)
	contours, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	print("all contours:", len(contours))
	# contours_img = cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
	# cv2.imwrite("/home/itron/quick-food/pics/test-all-contours.jpg", contours_img)
	for contour in contours:
		#find width/height=39/29=1.34
		x,y,w,h = cv2.boundingRect(contour)

		aspect_ratio = float(w)/h
		rect_area = w*h
		
		if (aspect_ratio<2 and 1<aspect_ratio and rect_area > 500):
			rec_contour.append(contour)
	imgs = []
	count = 0
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
		imgs.append(dst)
	print("contours filtered:", len(rec_contour))
	return imgs, rec_contour

img = cv2.imread("/home/itron/quick-food/pics/dot-scene-using-c310.jpg")

# crop process.
# if you use other camera, 
# please change the value and test here.
x = 100
y = 300
width = 400
height = 100
img = img[y:y+height, x:x+width]
cv2.imwrite("/home/itron/quick-food/pics/test-crop.jpg", img)

# get the rectangle contours
imgs, recContours = get_contours(img)
for i in range(len(imgs)):
	cv2.imwrite("/home/itron/quick-food/pics/test-contours-" + str(i) + ".jpg", imgs[i])
	cv2.imshow("contours-" + str(i), cv2.Canny(imgs[i], 1, 150))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# get the circle contours for each rectangle contour
circleImgs = []
for i in range(len(imgs)):
	imgs[i] = cv2.Canny(imgs[i], 50, 150)
	dotContours, _ = cv2.findContours(imgs[i].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	circleImgs.append(cv2.drawContours(imgs[i], dotContours, -1, (0, 0, 255), 1))
	cv2.imwrite("/home/itron/quick-food/pics/test-circle-" + str(i) + ".jpg", circleImgs[i])