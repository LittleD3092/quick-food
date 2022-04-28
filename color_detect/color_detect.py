from re import A
import cv2
import numpy as np

lower_orange = np.array([10,60,46])
upper_orange = np.array([15,255,255])

lower_black = np.array([0,0,0])
upper_black = np.array([180,100,80])

lower_blue = np.array([100,90,20])
upper_blue = np.array([124,255,255])

video = cv2.VideoCapture('/dev/video4') #抓取畫面
color = []
while True:
    success,img = video.read()

    image  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask_orange = cv2.inRange(image,lower_orange,upper_orange) #過濾顏色
    orange = cv2.bitwise_and(img,img,mask=mask_orange) #設定藍色遮罩

    contours, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
    if len(contours) > 450 :
        for contour in contours:
            if cv2.contourArea(contour) > 20000 :
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
        color.append(1)           
    else : color.append(0)

    mask_black = cv2.inRange(image,lower_black,upper_black) 
    black = cv2.bitwise_and(img,img,mask=mask_black) 

    contours, hierarchy = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
    if len(contours) > 450 :
        for contour in contours:
            if cv2.contourArea(contour) > 20000 :
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,0),3) 
        color.append(1)   
    else : color.append(0)

    mask_blue = cv2.inRange(image,lower_blue,upper_blue) 
    blue = cv2.bitwise_and(img,img,mask=mask_blue) 

    contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #畫出物體邊框
    if len(contours) > 450 :
        for contour in contours:
            if cv2.contourArea(contour) > 20000 :
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y),(x+w,y+h),(150,160,0),3)
        color.append(1)        
    else : color.append(0)

    # cv2.imshow("black",black)
    # cv2.imshow("orange",orange)
    # cv2.imshow("blue",blue)
    cv2.imshow("webcam",img)
    print(color)
    cv2.waitKey(20)
    color.clear()
