#!/usr/bin/env python
from __future__ import print_function
#from subprocess import call
import cv2
import rospy
from cv_bridge import CvBridge,CvBridgeError
from std_msgs.msg import Int16
import numpy as np



def calculate_circle(cv_image):
    n=[]
    gray=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    (a,b,c)=cv_image.shape

    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20, param1=100, param2=30, minRadius=1, maxRadius=300)

    if circles is None:
        return 0
    else:
        for circle in circles[0]:
            # 座標行列
            X = int(circle[0])
            Y = int(circle[1])
		    # 半徑
            r = int(circle[2])
		    # 在原圖用指定顏色標記出圓的位置
            cv_image = cv2.circle(cv_image, (X, Y), r, (0, 0, 255), 3)
            return (len(circles[0])) 

def get_result(cv_image):
    number=1
    for i in range(4):
        (a,b,c)=cv_image.shape
        x=int(b*0.5)
        y=int(b*0.73)   
        p=int(a*0.36)
        q=int(a*0.8)

        if number == 1:
            img1 =cv_image [0:a,x:y]
            area1=calculate_circle(img1)

        elif number == 2:
            img2 =cv_image[0:a,y:b]
            area2=calculate_circle(img2)
        elif number == 3:
            img3 = cv_image[0:p,x:b]
            area3=calculate_circle(img3)
        elif number==4:
            img4 = cv_image[p:q,x:b]
            area4=calculate_circle(img4)
        else:
            print("get_result function wrong")
            break
        number=number+1

    if area2 ==0:
        if area1==1:
            print("此點字為1")
            return 1
        else:
            print("此點字為2")
            return 2
    elif area2 ==1:
        if area1==2:
            print("此點字為6")
            return 6
        elif area1==1 and area3==1:
            print("此點字為5")
            return 5
        else:
            print("此點字為3")
            return 3
    else:
        print("此點字為4")
        return 4


def find_circle(cv_image,rec_contour):
    contours, _ = cv2.findContours(
		cv_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if i==0:
            i=1
            continue
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
                        contour, 0.01 * cv2.arcLength(contour, True), True)

        #find width/height=39/29=1.34
        x,y,w,h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
		#find area
        area=cv2.contourArea(contour)
        extent=float(area)/(w*h)
        if len(approx) == 4 and aspect_ratio<1.345 and 1.335<aspect_ratio and extent>0.9:
            rec_contour.append(contour)
            print(len(rec_contour))
            cv2.drawContours(cv_image, [contour], 0, (0, 0, 255), 2)
    if rec_contour is not None:
        for contour in rec_contour:
	
			# using drawContours() function
            #cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)
            #cv2.putText(img, 'Q', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)
		
			# displaying the image after drawing contours
			#cv2.imshow('shapes', img)
            x,y,w,h = cv2.boundingRect(contour)
			
			#img after cutting
            pts1 = np.float32([[x,y],[x+w,y],[x,y+h],[x+w,y+h]])
            pts2 = np.float32([[0,0],[390,0],[0,290],[390,290]])
            M=cv2.getPerspectiveTransform(pts1,pts2)
            dst=cv2.warpPerspective(cv_image.copy(),M,(390,290))
            cv2.imshow('result',dst)
    return (get_result(dst))
        


    
def numbercallback(self,data):
    try:
            #same as data form
        rec_contour=[]
        cv_image =self.bridge.imgmsg_to_cv2(data,"passthrough")
        self.__init__
        number=find_circle(cv_image,rec_contour)
        return number
    except CvBridgeError as e:
        print(e)


if __name__ == '__main__':
    bridge=CvBridge()
    cap =cv2.VideoCapture(2)
    bridge=CvBridge()
    ret, frame=cap.read()
    webcam = bridge.cv2_to_imgmsg(frame,"bgr8")
    rospy.init_node('point_number_pub')
    s=rospy.Service('dot_recognize',Int16,numbercallback)
    rospy.spin()
