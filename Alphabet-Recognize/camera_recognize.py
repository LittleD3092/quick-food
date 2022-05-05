import cv2

# capture from camera, 0 means first camera attached
cap = cv2.VideoCapture(1)

while True:
	# read from camera
	#     ret: whether capture is successful or not
	#     frame: picture captured
	ret, frame = cap.read()

	# copy the frame
	img2 = frame.copy()

	# full color --> gray
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

	# gray -- 150 ~ 200 --> canny
	cny = cv2.Canny(gray ,150 ,200)

	# get contour data from canny
	contours, hier = cv2.findContours(cny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	
	# draw contour
	for cnt in contours:
		cv2.drawContours(img2, cnt, -1, (255, 0, 0), 4)
	cv2.imshow('img2', img2)
	cv2.waitKey(1)