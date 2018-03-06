import cv2
from matplotlib import pyplot as plt
#opencv bgr
#plt    rgb
img = cv2.imread('../../images/color.png')

plt.subplot(2,3,1)
plt.imshow(img)

b,g,r=cv2.split(img)
img2=img[:-1]
plt.subplot(2,3,2)
plt.imshow(img2)

img3=img[::-1]
plt.subplot(2,3,3)
plt.imshow(img3)

img4=img[:,::-1]
plt.subplot(2,3,4)
plt.imshow(img4)

img6=img[:,:,::-1]
plt.subplot(2,3,5)
plt.imshow(img6)

plt.show()