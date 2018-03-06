import cv2
import numpy as np

x=np.uint8([250])
y=np.uint8([10])
print(cv2.add(x,y))
print(x+y)

cv2.namedWindow('img')
cv2.moveWindow('img',0,0)
cv2.namedWindow('img2')
cv2.moveWindow('img2',300,0)
cv2.namedWindow('img3')
cv2.moveWindow('img3',600,0)
img1 = cv2.imread('../anwb.jpg')
img2 = cv2.imread('../atht.jpg')
img3 = cv2.add(img1,img2)
img4 = img1+img2
img5 = cv2.addWeighted(img1,0.7,img2,0.3,50)
cv2.imshow('img',img3)
cv2.imshow('img2',img4)
cv2.imshow('img3',img5)
cv2.waitKey(0)