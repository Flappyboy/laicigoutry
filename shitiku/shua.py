import shitiku.getData as gd
import xlrd
import json
cookie = 'UM_distinctid=15f66b2128f357-0bf709102ae6de-293e1d4e-100200-15f66b21290245; JSESSIONID=3A3FEFF3DE0F56418602200B60A2AB4F.tomcat2; loginedMsg=77546`1523438290138`c526d3909cd2ffa5d199760eacd5d4d2; CNZZDATA5938897=cnzz_eid%3D1317697267-1520901406-%26ntime%3D1523434654'
url = 'http://tkkc.hfut.edu.cn/student/exam/manageExam.do?1523438317875&method=doExam&examId=134&taskId=175&history=false'

data = gd.getData(cookie,url)
# for d in data:
#     print(d['examStudentExerciseId'])
workbook = xlrd.open_workbook(r'./answer.xls')
i=1
for d in data['data']:
    topic = gd.getTopic(cookie,d,data['num'])
    answer = gd.getAnswer(topic,workbook)
    if (answer==''):
        answer='*'
    print('%02d' % i+' '+answer+'\t'+topic['title'])
    i+=1
    #gd.submit(cookie,topic,data['num'],answer,d)