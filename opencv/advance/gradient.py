import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    laplacian1=cv2.Laplacian(frame,cv2.CV_64F)
    laplacian=np.absolute(laplacian1)
    laplacian=np.uint8(laplacian)
    kernel=np.ones((5,5),dtype=np.uint8)
    laplacian2=cv2.bilateralFilter(laplacian,1,75,75)
    laplacian2=255-laplacian2
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    cv2.imshow('frame', frame)
    cv2.imshow('laplacian', laplacian1)
    cv2.imshow('laplacian2', laplacian2)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()