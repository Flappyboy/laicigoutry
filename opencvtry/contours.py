import numpy as np
import cv2
img = cv2.imread('../images/color.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,60,255,0)
thresh=cv2.Canny(imgray,100,200)
image ,contours,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
imag = cv2.drawContours(img,contours,-1,(0,255,0),1)
while(1):
    cv2.imshow('img',img)
    cv2.imshow('imgray',imgray)
    cv2.imshow('image',image)
    cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()