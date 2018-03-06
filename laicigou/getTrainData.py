from urllib import request
import json
import time
import cv2
import base64
import numpy as np
from matplotlib import pyplot as plt
from threading import Thread
from multiprocessing import Process,Queue,Pipe,Manager,Pool
import matplotlib.animation as animation
from PIL import Image
from PIL import ImageFile

def show(q):
    imgWinName = 'image'
    cv2.namedWindow(imgWinName)
    while(True):
        pass
        if(q.empty()):
            time.sleep(0.5)
        else:
            imageCode = q.get()
            cv2.imshow(imgWinName, imageCode)
            cv2.waitKey(1)

if __name__ == '__main__':
    cookie = 'BAIDUID=E5BAFE8ABF32A20B4005ABBE7B985EFB:FG=1; BIDUPSID=E5BAFE8ABF32A20B4005ABBE7B985EFB; PSTM=1506846931; BDUSS=3FDQXAzbDU3R3pCZjhrVldnVWFUOGlHUGlPQmpOYzFSaGM1OFZ-QVk3bkl-UVJhTVFBQUFBJCQAAAAAAAAAAAEAAACaGRpPwcvIu9Pq1tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhw3VnIcN1ZV; BDSFRCVID=8oKsJeC626aTBf3AfZDx2QBa5e5rbsOTH6aI-DpZUBMCS9gu41H6EG0PDU8g0Kub-mPZogKK0eOTHkrP; H_BDCLCKID_SF=tR32Wn7a5TrDHJTg5DTjhPrMBnbmbMT-027OKK8XX-jGEJQ9MxbRXfkrWxDqeRTWWa6k-bv-thF0hCKlD5DMjjjMKUoLeJ3KajQ3W-5H5PK_Hn7zeT7oyntpbt-qJj5KQgrhohjDyqbWhxjt-joqjJDVKPnnBT5KW4jRQUcG0q6TVITT5j8ay5KkQN3T0pLO5bRiLR_EaxJADn3oyT3qXp0nMp5TqtJHKbDeoKL5tUK; PSINO=5; H_PS_PSSID=25641_1465_21101_18559_22160; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
    header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    reqQuery = request.Request('https://pet-chain.baidu.com/data/market/queryPetsOnSale')
    reqQuery.add_header('User-Agent', header)
    reqQuery.add_header('Cookie', cookie)
    reqQuery.add_header('content-type', 'application/json')
    reqQuery.add_header('Connection', 'keep-alive')
    dataQuery = {"pageNo": 1, "pageSize": 20, "querySortType": "AMOUNT_ASC", "petIds": [], "lastAmount": None,
                 "lastRareDegree": None, "requestId": 1517995669610, "appId": 1, "tpl": ""}
    errorTime = 2;

    reqVerify = request.Request('https://pet-chain.baidu.com/data/captcha/gen')
    reqVerify.add_header('User-Agent', header)
    reqVerify.add_header('Cookie', cookie)
    reqVerify.add_header('content-type', 'application/json')
    reqVerify.add_header('Connection', 'keep-alive')
    dataVerify = {"requestId": 1518055039055, "appId": 1, "tpl": ""}

    reqJump = request.Request('https://pet-chain.baidu.com/data/market/shouldJump2JianDan')
    reqJump.add_header('User-Agent', header)
    reqJump.add_header('Cookie', cookie)
    reqJump.add_header('content-type', 'application/json')
    reqJump.add_header('Connection', 'keep-alive')
    dataJump = {"requestId": 1518055039055, "appId": 1, "tpl": ""}

    reqBuy = request.Request('https://pet-chain.baidu.com/data/txn/create')
    reqBuy.add_header('User-Agent', header)
    reqBuy.add_header('Cookie', cookie)
    reqBuy.add_header('content-type', 'application/json')
    reqBuy.add_header('Connection', 'keep-alive')
    dataBuy = {"petId": "1864796253564751589", "amount": "1959.00", "seed": "390571068", "captcha": "4xgy",
               "validCode": "b22240d0e6db401ac24be606d8019373", "requestId": 1518056989078, "appId": 1, "tpl": ""}

    def buy(pet, data):
        try:
            dataBuy['petId'] = pet['petId']
            dataBuy['amount'] = pet['amount']
            dataBuy['seed'] = data['seed']
            dataBuy['captcha'] = data['captcha']
            dataBuy['validCode'] = pet['validCode']
            dataBuy['requestId'] = (int(round(time.time() * 1000)))
            # print(dataBuy)
            dataStr = json.dumps(dataBuy)
            reqBuy.add_header('Referer', 'https://pet-chain.baidu.com/chain/detail?channel=market&petId=' + pet[
                'petId'] + '&appId=1&validCode=' + pet['validCode'])
            with request.urlopen(reqBuy, data=dataStr.encode('utf-8')) as f:
                # print('Buy Status:', f.status, f.reason)
                fdata = json.loads(f.read().decode('utf-8'))
                print('buymsg: ', fdata["errorMsg"])
        except Exception as e:
            print('error buy:', e)
        else:
            pass
            # print(fdata)
            print('buy ok')


    def jump(pet, data):
        try:
            dataJump['requestId'] = (int(round(time.time() * 1000)))
            dataStr = json.dumps(dataJump)
            # print(dataStr)
            reqVerify.add_header('Referer', 'https://pet-chain.baidu.com/chain/detail?channel=market&petId=' + pet[
                'petId'] + '&appId=1&validCode=' + pet['validCode'])
            with request.urlopen(reqJump, data=dataStr.encode('utf-8')) as f:
                # print('Jump Status:', f.status, f.reason)
                buy(pet, data)
        except Exception as e:
            print("jump ", e)
        else:
            pass
            # print("jump ok")

    q = Queue(maxsize=1)
    process = Process(target=show,args=(q,))
    process.start()

    def recognizeCode(img):
        codeStr=''
        imgData = base64.b64decode(img)
        nparr = np.fromstring(imgData, np.uint8)
        img_np = cv2.imdecode(nparr, 0)
        if(q.full()):
            q.get()
        q.put(img_np)
        # cv2.imshow(imgWinName, img_np)
        # cv2.waitKey(1)
        codeStr = input("captcha:")
        if(len(codeStr)>0):
            cv2.imwrite('./captcha_dataset/'+codeStr+'.jpg',img_np)
        # print("captcha: ")
        # for i in range(4):
        #     key=cv2.waitKey(0)
        #     if key==27:
        #         pass
        #         cv2.destroyAllWindows()
        #         exit()
        #     elif (key in range(48,59))or(key in range(65,90))or(key in range(97,122)):
        #         codeStr += chr(key)
        #         print(codeStr)
        #         font = cv2.FONT_HERSHEY_SIMPLEX
        #         cv2.putText(img_np,codeStr,(0,10), font, 0.5,(0,0,0),2,cv2.LINE_AA)
        #         cv2.imshow(imgWinName, img_np)


        return codeStr

    def verify(pet):
        #print(pet)
        try:
            dataVerify['requestId'] = (int(round(time.time() * 1000)))
            dataStr = json.dumps(dataVerify)
            #print(dataStr)
            reqVerify.add_header('Referer','https://pet-chain.baidu.com/chain/detail?channel=market&petId='+pet['petId']+'&appId=1&validCode='+pet['validCode'])
            with request.urlopen(reqVerify, data=dataStr.encode('utf-8')) as f:
                #print('verify Status:', f.status, f.reason)
                fdata = json.loads(f.read().decode('utf-8'))
                #print(fdata)
                codeStr = recognizeCode(fdata['data']['img'])
                if(len(codeStr)>0):
                    print('已保存 ',codeStr)
                else:
                    print('取消')
                verify(pet)
        except Exception as e:
            print('error verify',e)
        else:
            pass
            #print('verify ok')

    def queryPets(selectAmount):
        while(True):
            try:
                dataQuery['requestId'] = (int(round( time.time() * 1000)))
                dataStr = json.dumps(dataQuery)
                #print(dataStr)
                with request.urlopen(reqQuery, data=dataStr.encode('utf-8')) as f:
                    print('Query Status:', f.status, f.reason)
                    # for k, v in f.getheaders():
                    #     print('%s: %s' % (k, v))
                    fdata = json.loads(f.read().decode('utf-8'))
                    #print('Query Data:', fdata)
                    #print('Query Data len:', len(fdata['data']['petsOnSale']))
                    selectData = []
                    print('money:',end=' ')
                    for d in fdata['data']['petsOnSale']:
                        print(d['amount'], end=' ')
                        if selectAmount>=float(d['amount']):
                            selectData.append(d)
                    print()
                    if len(selectData)==0:
                        print('no select data')
                    else:
                        print()
                        verify(selectData[0])
            except Exception:

                errorTime += 1
                print('error ',errorTime)
                time.sleep(errorTime)
                continue;
            else:
                errorTime = 2
                time.sleep(1)

    queryPets(15000)