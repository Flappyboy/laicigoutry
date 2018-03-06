import cv2
import numpy as np
def nothing():
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('laplacian')
cv2.createTrackbar('min','laplacian',0,200,nothing)
cv2.createTrackbar('max','laplacian',0,300,nothing)
while(1):
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    min=cv2.getTrackbarPos('min','laplacian')
    max = cv2.getTrackbarPos('max', 'laplacian')
    canny=cv2.Canny(frame,min,max)
    cv2.imshow('frame', frame)
    cv2.imshow('laplacian', canny)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()