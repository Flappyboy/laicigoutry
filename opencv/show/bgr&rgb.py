import cv2
from matplotlib import pyplot as plt
#opencv bgr
#plt    rgb
img = cv2.imread('../../images/color.png')
cv2.imshow('image',img)

plt.subplot(2,2,1)
plt.imshow(img)

#method1
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])
plt.subplot(2,2,2)
plt.imshow(img2)

#method2
img3=img[:,:,::-1]
plt.subplot(2,2,3)
plt.imshow(img3)

#method3
img4=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(2,2,4)
plt.imshow(img4)
plt.show()