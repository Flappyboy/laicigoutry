import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../../images/equal.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
#stacking images side-by-side
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist,color='b')
plt.xlim([0,256])

hist = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.plot(hist,color='g')
plt.xlim([0,256])


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
hist2=cv2.calcHist([cl1],[0],None,[256],[0,256])
plt.plot(hist2,color='r')
plt.show()