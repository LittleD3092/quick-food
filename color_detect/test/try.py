#!usr/bin/python
# -*- coding: utf-8 -*-

########利用三角形相似原理進行簡單單目測距#########
# author：行歌
# email:[email protected]

import numpy as np
import cv2

# initialize the known distance from the camera to the object,
# which in this case is 24 inches
KNOWN_DISTANCE = 24.0

# initialize the known object width, which in this case,
# the piece of paper is 11 inches wide
KNOWN_WIDTH = 11.69
KNOWN_HEIGHT = 8.27

# initialize the list of images that we'll be using
IMAGE_PATHS = ["Picture1.jpg", "Picture2.jpg", "Picture3.jpg"]


def find_marker(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 將彩色圖轉化為灰度圖

    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    # 高斯平滑去噪

    edged_img = cv2.Canny(gray_img, 35, 125)
    # Canny運算元閾值化
    # cv2.imshow("edged_img",edged_img)

    img, countours, hierarchy = cv2.findContours(edged_img.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    # 注意，findcontours函式會“原地”修改輸入的影象。opencv3會返回三個值,分別是img, countours, hierarchy
    # 第二個引數表示輪廓的檢索模式,cv2.RETR_EXTERNAL表示只檢測外輪廓；v2.RETR_LIST檢測的輪廓不建立等級關係
    # cv2.RETR_CCOMP建立兩個等級的輪廓；cv2.RETR_TREE建立一個等級樹結構的輪廓。
    # 第三個引數method為輪廓的近似辦法,cv2.CHAIN_APPROX_NONE儲存所有的輪廓點，
    # 相鄰的兩個點的畫素位置差不超過1，即max（abs（x1 - x2），abs（y2 - y1）） == 1
    # cv2.CHAIN_APPROX_SIMPLE壓縮水平方向，垂直方向，對角線方向的元素，只保留該方向的終點座標，
    # 例如一個矩形輪廓只需4個點來儲存輪廓資訊

    # cv2.drawContours(image,countours,-1,(0,0,255),2,8)
    # # 第三個引數指定繪製輪廓list中的哪條輪廓，如果是-1，則繪製其中的所有輪廓。
    #
    # cv2.imshow('image', image)

    # print(len(countours)),
    # 輸出如下：15，即該圖檢測出15個輪廓

    c = max(countours, key = cv2.contourArea)
    # 提取最大面積矩形對應的點集

    rect = cv2.minAreaRect(c)
    # cv2.minAreaRect()函式返回矩形的中心點座標，長寬，旋轉角度[-90,0)，當矩形水平或豎直時均返回-90
    # c代表點集，返回rect[0]是最小外接矩形中心點座標，
    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度


    # box = cv2.boxPoints(rect)
    # # 但是要繪製這個矩形，我們需要矩形的4個頂點座標box, 通過函式cv2.boxPoints()獲得，
    # # 即得到box：[[x0, y0], [x1, y1], [x2, y2], [x3, y3]]
    # # print(box)，輸出如下：
    # # [[508.09482  382.58597]
    # #  [101.76947  371.29916]
    # #  [109.783356  82.79956]
    # #  [516.1087    94.086365]]
    #
    # # 根據檢測到的矩形的頂點座標box，我們可以將這個矩形繪製出來，如下所示：
    # for i in range(len(box)):
    #     cv2.line(image, (box[i][0],box[i][1]),(box[(i+1)%4][0],box[(i+1)%4][1]),(0,0,255),2,8)
    # cv2.imshow('image', image)

    return rect


def distance_to_camera(knownWidth, focalLength, perWidth):
    return (knownWidth * focalLength) / perWidth


def calculate_focalDistance(img_path):
    first_image = cv2.imread(img_path)
    # cv2.imshow('first image',first_image)

    marker = find_marker(first_image)
    # 得到最小外接矩形的中心點座標，長寬，旋轉角度
    # 其中marker[1][0]是該矩形的寬度，單位為畫素

    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
    # 獲取攝像頭的焦距

    print('焦距（focalLength ）= ',focalLength)
    # 將計算得到的焦距打印出來

    return focalLength


def calculate_Distance(image_path,focalLength_value):
    # 載入每一個影象的路徑，讀取照片，找到A4紙的輪廓
    # 然後計算A4紙到攝像頭的距離

    image = cv2.imread(image_path)
    cv2.imshow("image", image)
    cv2.waitKey(300)

    marker = find_marker(image)
    distance_inches = distance_to_camera(KNOWN_WIDTH,focalLength_value, marker[1][0])
    # 計算得到目標物體到攝像頭的距離，單位為英寸，
    # 注意，英寸與cm之間的單位換算為： 1英寸=2.54cm

    box = cv2.boxPoints(marker)
    # print( box )，輸出類似如下：
    # [[508.09482  382.58597]
    #  [101.76947  371.29916]
    #  [109.783356 82.79956]
    #  [516.1087   94.086365]]

    box =np.int0( box)
    # 將box陣列中的每個座標值都從浮點型轉換為整形
    # print( box )，輸出類似如下：
    # [[508 382]
    #  [101 371]
    #  [109 82]
    #  [516 94]]

    cv2.drawContours(image, [box], -1, (0, 0, 255), 2)
    # 在原圖上繪製出目標物體的輪廓

    cv2.putText(image, "%.2fcm" % (distance_inches * 2.54),
            (image.shape[1] - 300, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            2.0, (0, 0, 255), 3)
    # cv2.putText()函式可以在照片上新增文字
    # cv2.putText(img, txt, (int(x),int(y)), fontFace, fontSize, fontColor, fontThickness)
    # 各參即為：照片/新增的文字/左上角座標/字型/字型大小/顏色/字型粗細

    cv2.imshow("image", image)





if __name__ == "__main__":
    img_path = "Picture1.jpg"
    focalLength = calculate_focalDistance(img_path)
    # 獲得攝像頭焦

    for image_path in IMAGE_PATHS:
        calculate_Distance(image_path,focalLength)
        cv2.waitKey(1000)
    cv2.destroyAllWindows()
