#导入cv模块
import cv2
import numpy as np
from matplotlib import pyplot as plt
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
# img = cv2.imread("D:/opencvtest/test2.png",0)
#创建窗口并显示图像
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# cv2.imshow("Image",img)
# k = cv2.waitKey(0)
# if k==27:
#     cv2.destroyAllWindows()
# elif k==ord('s'):
#     cv2.imwrite('testwrite.png',img)
#     cv2.destroyAllWindows()

# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()
# 'E:\downloads\迅雷下载\STAR-46511\STAR-465.avi'
# cap = cv2.VideoCapture(0)
# cap.set(3,320)
# cap.set(4,240)
# while(True):
#     ret , frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(25) &0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame',frame)
        key = cv2.waitKey(25)

        if key&0xFF==ord('q'):
            break
        elif key==37:
            break
        elif key==40:
            for i in range(1,100000):
                print(i)
                cap.read()
            break
    else:
        print('ret false')
        break
cap.release()
out.release()
cv2.destroyAllWindows()