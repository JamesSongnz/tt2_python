import os
from sys import intern

import numpy as np
import cv2
from matplotlib import pyplot as plt


# img = cv2.imread('.//imgs/face2.jpg', cv2.IMREAD_GRAYSCALE)
#
# plt.imshow(img, cmap= 'gray',interpolation='bicubic' )
# plt.xticks([]), plt.yticks([])
# plt.show()


# face detection
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
# https://github.com/opencv/opencv/tree/master/samples/python/tutorial_code
from openCvTestFunc import faceDetection, recordCamera


def extractColorObject():
    cap = cv2.VideoCapture(0)
    while (1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 앞서 설명한 파랑색 계열의 범위
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_or(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

def imageBasicProcessing2():
    img1 = cv2.imread('./imgs/JaeokSong.jpg')
    img2 = cv2.imread('./imgs/face3.jpg')
    dst = cv2.resize(img2, dsize=(640, 480), interpolation=cv2.INTER_LINEAR)
    src = cv2.resize(img1, dsize=(640, 480), interpolation=cv2.INTER_LINEAR)

    dst = cv2.addWeighted(dst, 0.7, src, 0.3, 0)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imageBasicProcessing():
    img = cv2.imread('./imgs/JaeokSong.jpg')

    px = img[0,100] # row, col
    print(px) # b g, r

    blue = img[0, 100, 0] #  row, col, channel
    print(blue) #

    img[0,100] = [255,255,255]
    img[0,100,0] = 0 # B channel <- 0

    px = img.item(0,100,0)
    print(px)

    print(img.shape)
    print(img.size)
    print(img.dtype)

    # co0y
    roi = img[280:340, 330:390]
    img[273:333, 100:160] = roi

    cv2.rectangle(img, (330,280), (390,340), (0,0,255), 1)
    cv2.rectangle(img, (100,273), (160,333), (255,0,0), 1)

    cv2.imshow('img', img)
    cv2.waitKey()

    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))

    b = img[:, :, 0]
    cv2.imshow('img', b)
    cv2.waitKey()

    img[:, :, 2] = 0

    cv2.imshow('img', img)
    cv2.waitKey()

    cv2.destroyAllWindows()


    RED = [255,0,0]


    img1 = cv2.imread('./imgs/face3.jpg')

    e1 = cv2.getTickCount()
    img2 = cv2.medianBlur(img1, 5)
    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()
    print(time)
    cv2.imshow('blur', img2)
    cv2.waitKey()

    replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
    constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=RED)

    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

    plt.show()



if __name__ == '__main__':
    extractColorObject()
    # imageBasicProcessing2()
    # drawWithCV()
    # mouseEventInCV()
    # recordCamera()
    # cameraCapture()

# channel division
# src = cv2.imread('./imgs/JaeokSong.jpg')
# cv2.imshow('src', src)
#
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
#
# v2 = cv2.equalizeHist(v)
# hsv2 = cv2.merge([h, s, v2])
# dst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
# cv2.imshow('dst', dst)
#
# cv2.waitKey()
# cv2.destroyAllWindows()





# cv2.imshow('image', img)
#
# k = cv2.waitKey()
#
# if k ==  ord('s'):
#     cv2.imwrite('./testout.jpg', img)
#
# cv2.destroyAllWindows()