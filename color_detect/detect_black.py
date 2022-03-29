import cv2
import numpy as np

lower_black = np.array([0,0,0])
upper_black = np.array([180,255,30])

video = cv2.VideoCapture(0) #抓取畫面

while True:
    success,img = video.read()

    image  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask_black = cv2.inRange(image,lower_black,upper_black) #過濾顏色
    black = cv2.bitwise_and(img,img,mask=mask_black) #設定藍色遮罩

    contours, hierarchy = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
    if len(contours) != 0 :
        for contour in contours:
            if cv2.contourArea(contour) >500 :
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow("black",black)
    cv2.imshow("webcam",img)
    cv2.waitKey(1)