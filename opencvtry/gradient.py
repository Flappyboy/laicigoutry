import cv2
import numpy as np
img = cv2.imread('../images/color.png',0)
ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
ret , thresh2 = cv2.threshold(gradient,20,255,cv2.THRESH_BINARY)
cv2.namedWindow('image')
cv2.moveWindow('image',0,0)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('image2', gradient)
    cv2.imshow('thresh2', thresh2)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()