import cv2
import numpy as np
from matplotlib import pyplot as plt

def change(x):
    print('change:',x)
    s0 = cv2.getTrackbarPos('s0', 'image')
    s1 = cv2.getTrackbarPos('s1', 'image')
    s2 = cv2.getTrackbarPos('s2', 'image')
    bilateralBlur = cv2.bilateralFilter(img, s0, s1, s2)
    cv2.imshow('image', bilateralBlur)
    pass

img = cv2.imread('../images/blur.jpg')
# img = cv2.imread('../images/color.png')
cv2.namedWindow('image')
cv2.createTrackbar('s0','image',0,50,change)
cv2.createTrackbar('s1','image',0,1000,change)
cv2.createTrackbar('s2','image',0,1000,change)
change(0)
while(1):
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()