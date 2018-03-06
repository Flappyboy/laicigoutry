import cv2
import numpy as np
img=cv2.imread('/home/duan/workspace/opencv/images/roi.jpg')
b,g,r=cv2.split(img)
img=cv2.merge(b,g,r)