import cv2
import numpy as np
import operator

def dealImg(img):
    ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    kernel1 = np.ones((2,2),np.uint8)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel1)
    kernel2 = np.ones((2, 2), np.uint8)
    erodeimg = cv2.morphologyEx(thresh1, cv2.MORPH_ERODE, kernel2)

    cv2.imshow('open',erodeimg)
    # cv2.waitKey(0)
    image, contours, hierarchy = cv2.findContours(erodeimg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    erodeimg = cv2.cvtColor(erodeimg,cv2.COLOR_GRAY2BGR)

    class cObj:
        c = None
        cx = 0

        def __init__(self, c, cx):
            self.c =c
            self.cx = cx
    clist=[]
    for c in contours:
        area = cv2.contourArea(c)
        if area>100:
            M = cv2.moments(c)
            cx = int(M['m10'] / M['m00'])
            clist.append(cObj(c,cx))
        else:
            for i in range(len(c)):
                erodeimg[c[i,0,1],c[i,0,0]]=[0,0,0]

    cmpfun = operator.attrgetter('cx') #按照docId进行排序
    clist.sort(key=cmpfun)

    roiList=[]
    for d in clist:
        x, y, w, h = cv2.boundingRect(d.c)
        # re = cv2.rectangle(erodeimg, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi=erodeimg[y:y+h,x:x+w]
        dilateImg = cv2.morphologyEx(roi, cv2.MORPH_DILATE, kernel1)
        roiList.append(roi)

    return roiList