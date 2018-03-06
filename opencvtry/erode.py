import cv2
import numpy as np
img = cv2.imread('../images/color.png',0)
ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations=1)
while(1):
    cv2.imshow('image',thresh1)
    cv2.imshow('erosion',erosion)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()