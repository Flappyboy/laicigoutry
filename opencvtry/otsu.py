import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../images/color.png',0)
ret1,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#(5,5)为高斯核的大小， 0为标准差
blur= cv2.GaussianBlur(img,(5,5),0)
#阀值一定要设为0
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
images=[img,0,th1,img,0,th2,img,0,th3]
titles =['original noisy image','histogram','global thresholding(v=127','original noisy image','histogram',"otsu's thresholding",'gaussian giltered image','histogram',"otus's thresholding"]
#这里使用了pyplot中画直方图的方法， plt.hist要注意的是他的参数是一维数组
#所以这里使用了（numpy） ravel方法， 将多维数组转换成一维， 也可以使用flatten方法
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
plt.show()