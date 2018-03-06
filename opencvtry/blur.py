import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../images/blur.jpg')
# img = cv2.imread('../images/color.png')
blur = cv2.blur(img,(5,5))
# 0是指根据窗口大小（5,5） 来计算高斯函数标准差
gaussBlur = cv2.GaussianBlur(img,(5,5),0)
median =  cv2.medianBlur(img,5)
bilateralBlur = cv2.bilateralFilter(img,9,75,75)
# while(1):
#     cv2.imshow('image',img)
#     cv2.imshow('blur',blur)
#     cv2.imshow('gaussBlur',gaussBlur)
#     k=cv2.waitKey(1)
#     if k == ord('q'):#按q键退出
#         break

images=[img,blur,gaussBlur,median,bilateralBlur,0]
titles =['image','blur','gauss','median','bilateralBLur']
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i]),plt.xticks([]),plt.yticks()
plt.show()