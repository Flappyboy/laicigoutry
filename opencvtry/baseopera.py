import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../test2.png')
# fig = plt.figure()
# plt.imshow(img)
# plt.show()
# px=img[100,100]
# print(px)
# blue = img[100,100,0]
# print(blue)
# img[101,101]=[255,255,255]
# print(img[101,101])

# print(img.shape)
# print(img.size)
# print(img.dtype)
# print(img.item(10,10,2))
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

#
# cv2.namedWindow("img")
# cv2.imshow("img",img)
#
# ball =img[290:315,560:600]
# print(ball)
# img[290:315,600:640]=ball
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# r,g,b=cv2.split(img)
# img=cv2.merge([r,g,b])
#
# cv2.imshow('imgr',r)
# cv2.imshow('imgg',g)
# cv2.imshow('imgb',b)
# img=img[:,:,0]
img[:,:,1]=0
img[:,:,2]=0
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()