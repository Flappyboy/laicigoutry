import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/color.png')
hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#设定蓝色的阀值
lower_blue = np.array([110,50,50])
print(lower_blue)
upper_blue = np.array([130,255,255])
#根据阀值构建掩模
mask = cv2.inRange(hsv,lower_blue,upper_blue)
#对原图和掩模进行位运算
res = cv2.bitwise_and(img1,img1,mask=mask)
cv2.imshow('img1',img1)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)