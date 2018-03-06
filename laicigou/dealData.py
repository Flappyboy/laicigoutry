import os
import laicigou.dealImg as dealImg
import cv2
import uuid
def file_name(file_dir):
   for root, dirs, files in os.walk(file_dir):
       return files
def inputWord(img,word):
    path='./word'
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
    cv2.imwrite('./word/'+word+'_'+str(uuid.uuid1())+'.jpg',img)
files = file_name('./captcha_dataset')
print(files)
for file in files:
    img=cv2.imread('./captcha_dataset/'+file,0)
    imgs = dealImg.dealImg(img)
    if len(imgs)!=4:
        continue
    i=0
    for im in imgs:
        if i>3:
            continue
        inputWord(im,file.split('.')[0][i])
        i+=1