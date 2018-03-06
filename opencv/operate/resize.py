# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:25:00 2014
@author: duan
"""
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    res1 = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    # OR
    # 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
    height, width = frame.shape[:2]
    res2 = cv2.resize(frame, (2 * width, 1 * height), interpolation=cv2.INTER_CUBIC)

    rows, cols = frame.shape[:2]
    # 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
    # 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    # 第三个参数是输出图像的尺寸中心
    res3 = cv2.warpAffine(frame, M, (1 * cols, 1 * rows))

    cv2.imshow('frame',frame)
    cv2.imshow('1',res1)
    cv2.imshow('2',res2)
    cv2.imshow('3', res3)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关闭窗口
cv2.destroyAllWindows()