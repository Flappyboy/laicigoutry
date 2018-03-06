import cv2
import numpy as np
img=cv2.imread('../../images/dog.jpg')
hist = cv2.calcHist([img],[0],None,[256],[0,256])