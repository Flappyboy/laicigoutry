# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
import cv2
from time import clock
import sys
# import video
#video 模块也是 opencv 官方文档中自带的
if __name__ == '__main__':
    # 构建 HSV 颜色地图
    hsv_map = np.zeros((180, 256, 3), np.uint8)
    # np.indices 可以返回由数组索引构建的新数组。
    # 例如： np.indices（（3,2））；其中（3,2）为原来数组的维度：行和列。
    # 返回值首先看输入的参数有几维：（3,2）有 2 维，所以从输出的结果应该是
    # [[a],[b]], 其中包含两个 3 行， 2 列数组。
    # 第二看每一维的大小，第一维为 3, 所以 a 中的值就 0 到 2（最大索引数），
    # a 中的每一个值就是它的行索引；同样的方法得到 b（列索引）
    # 结果就是
    # array([[[0, 0],
    # [1, 1],
    # [2, 2]],
    #
    # [[0, 1],
    # [0, 1],
    # [0, 1]]])
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map', hsv_map)
    cv2.namedWindow('hist', 0)
    hist_scale = 10
    def set_scale(val):
        global hist_scale
        hist_scale = val
    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)
    try: fn = sys.argv[1]
    except: fn = 0
    # cam = video.create_capture(fn, fallback='synth:bg=../cpp/baboon.jpg:class=chess:noise=0.05')
    cam = cv2.VideoCapture(fn)
    while True:
        flag, frame = cam.read()
        cv2.imshow('camera', frame)
        # 图像金字塔
        # 通过图像金字塔降低分辨率，但不会对直方图有太大影响。
        # 但这种低分辨率，可以很好抑制噪声，从而去除孤立的小点对直方图的影响。
        small = cv2.pyrDown(frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 取 v 通道 (亮度) 的值。
        # 没有用过这种写法，还是改用最常见的用法。
        #dark = hsv[...,2] < 32
        # 此步操作得到的是一个布尔矩阵，小于 32 的为真，大于 32 的为假。
        dark = hsv[:,:,2] < 32
        hsv[dark] = 0
        h = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
        #numpy.clip(a, a_min, a_max, out=None)[source]
        #Given an interval, values outside the interval are clipped to the interval edges.
        #For example, if an interval of [0, 1] is specified, values smaller
        #than 0 become 0, and values larger than 1 become 1.
        #>>> a = np.arange(10)
        #>>> np.clip(a, 1, 8)
        #array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
        h = np.clip(h*0.005*hist_scale, 0, 1)
        #In numpy one can use the 'newaxis' object in the slicing syntax to create an
        #axis of length one. one can also use None instead of newaxis,
        #the effect is exactly the same
        #h 从一维变成 3 维
        vis = hsv_map*h[:,:,np.newaxis] / 255.0
        cv2.imshow('hist', vis)
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
    cv2.destroyAllWindows()