from urllib import request
import numpy as np
cookie = 'SESSIONID_HAP=38e326f8-dabf-4293-87c6-6af9133f4618; loginKey=b931b0bf-ba43-4dfe-9b78-d37577495c94; GUEST_LANGUAGE_ID=zh_CN'
header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
reqQuery = request.Request('http://asc.hand-china.com/hrms/staffquery/staffquery.html')
reqQuery.add_header('User-Agent', header)
reqQuery.add_header('Cookie', cookie)
reqQuery.add_header('Connection', 'keep-alive')
i=0
while i<1000:
    i+=1
    with request.urlopen(reqQuery) as f:
        str=f.read().decode('utf-8')
        if str[:15]!='<!DOCTYPE html>' or len(str)!=28919:
            print('something wrong')
            print(str)
            print('Query Status:', f.status, f.reason)
            break
        else:
            print('正常',i)