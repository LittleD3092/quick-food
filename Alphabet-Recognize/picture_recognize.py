import cv2

# read image from file
#img = cv2.imread('T.jpeg')
img = cv2.imread('k.png')
img2 = img.copy()

# image --> gray -- 150~200 --> canny
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)

# get contour data from canny
binary, contours, hier = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# draw contour
for cnt in contours:
	cv2.drawContours(img2, cnt, -1, (255, 0, 0), 4)
	peri = cv2.arcLength(cnt, True)
	vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
	print(len(vertices))
cv2.imshow('canny', canny)
cv2.imshow('img2', img2)
cv2.waitKey(0)
