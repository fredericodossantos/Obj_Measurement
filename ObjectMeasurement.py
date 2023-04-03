import cv2
import numpy as np
import utils

webcam = False
path = '2_.jpeg'
cap = cv2.VideoCapture(0)
cap.set(10, 200)
cap.set(3, 1920)
cap.set(4, 1080)
wP = 210
hP = 297

scale = 3


while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)  # Use cv2.imread() to read the image from file   

        img, conts =  utils.getContours(img,minArea=5000,filter=4) 
        if len(conts) != 0:
            biggest = conts[0][2]
            #print(biggest)
            imgWarp = utils.warpImg(img, biggest, wP ,hP)
            cv2.imshow('A4', imgWarp)

        img = cv2.resize(img,(0,0),None,0.5,0.5)
        cv2.imshow('Original', img)

    if cv2.waitKey(1) & 0xFF == 27: 
        break

cv2.destroyAllWindows()
