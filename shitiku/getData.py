import xlrd
from urllib import request,parse
import json

def getData(cookie,url):
    header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    reqQuery = request.Request(url)
    reqQuery.add_header('Host','tkkc.hfut.edu.cn')
    # reqQuery.add_header('Referer','http://tkkc.hfut.edu.cn/student/teachingTask/taskhomepage.do?1521680407454&teachingTaskId=34')
    reqQuery.add_header('User-Agent', header)
    reqQuery.add_header('Cookie', cookie)
    reqQuery.add_header('Connection', 'keep-alive')
    data = ''
    with request.urlopen(reqQuery) as f:
        strd=f.read().decode('utf-8')
        index = strd.find("var examStudentExerciseSerialList");
        start = 0;
        end = 0;
        while(index<len(strd)):
            if strd[index]=='[':
                start = index;
            if strd[index]==']':
                end = index;
                break;
            index +=1;
        data = strd[start:end+1];
        strfind = '/student/exam/manageExam.do?'
        index = strd.find(strfind)
        start = index+len(strfind)
        while(index<len(strd)):
            if strd[index]=='&':
                end = index
                break;
            index+=1;
        number = strd[start:end]
    if data == '':
        return None
    return {'data':json.loads(data),'num':number}

def getTopic(cookie,data,num):
    url = 'http://tkkc.hfut.edu.cn/student/exam/manageExam.do?'+num+'+&method=getExerciseInfo&examReplyId=977&exerciseId='+str(data['exerciseId'])+'&examStudentExerciseId='+str(data['examStudentExerciseId'])
    header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    reqQuery = request.Request(url)
    reqQuery.add_header('Host', 'tkkc.hfut.edu.cn')
    # reqQuery.add_header('Referer','http://tkkc.hfut.edu.cn/student/teachingTask/taskhomepage.do?1521680407454&teachingTaskId=34')
    reqQuery.add_header('User-Agent', header)
    reqQuery.add_header('Cookie', cookie)
    reqQuery.add_header('Connection', 'keep-alive')
    reqQuery.add_header('X-Requested-With','XMLHttpRequest')
    with request.urlopen(reqQuery) as f:
        strd = f.read().decode('utf-8')
        return json.loads(strd)

def submit(cookie,topic,num,answer,data):
    url = 'http://tkkc.hfut.edu.cn/student/exam/manageExam.do?'+num+'&method=saveAnswer'
    header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    reqQuery = request.Request(url)
    reqQuery.add_header('Host', 'tkkc.hfut.edu.cn')
    # reqQuery.add_header('Referer','http://tkkc.hfut.edu.cn/student/teachingTask/taskhomepage.do?1521680407454&teachingTaskId=34')
    reqQuery.add_header('User-Agent', header)
    reqQuery.add_header('Cookie', cookie)
    reqQuery.add_header('Connection', 'keep-alive')
    reqQuery.add_header('X-Requested-With', 'XMLHttpRequest')
    postData = parse.urlencode([
    ('examReplyId', 977),
    ('examStudentExerciseId',data['examStudentExerciseId']),
    ('exerciseId', data['exerciseId']),
    ('examId', ''),
    ('teachingTaskId', '1'),
    ('DXanswer', ''),
    ('content', '')
])
    with request.urlopen(reqQuery) as f:
        strd = f.read().decode('utf-8')
        return json.loads(strd)
    pass

def getAnswer(topic,workbook):
    answer = ''
    if topic['type']==1:
        answer = getAnswerForSingle(topic,workbook)
    elif topic['type']==2:
        answer = getAnswerForJudge(topic,workbook)
    elif topic['type']==3:
        print('type==3')
    elif topic['type']==4:
        answer = getAnswerForMultiple(topic,workbook)
    else:
        print('type=='+type)
    return answer

def getAnswerForSingle(topic,workbook):
    options=['optionsA','optionsB','optionsC','optionsD','optionsE']
    sheet = workbook.sheet_by_name('单选题')
    size = len(sheet.col_values(0))
    for i in range(0,size):
        if sheet.cell(i,0).value==topic['title'].replace('&nbsp;',''):
            flag = True;
            for j in range(0,4):
                option = sheet.cell(i,j+2).value
                if topic[options[j]]!=option:
                    flag = False
                    break;
            if(flag):
                answer = sheet.cell(i,7).value;
                return answer
    return ''
def getAnswerForMultiple(topic,workbook):
    options=['optionsA','optionsB','optionsC','optionsD','optionsE']
    sheet = workbook.sheet_by_name('多选题')
    size = len(sheet.col_values(0))
    for i in range(0,size):
        if sheet.cell(i,0).value==topic['title'].replace('&nbsp;',''):
            flag = True;
            for j in range(0,5):
                option = sheet.cell(i,j+2).value
                if topic[options[j]]!=option:
                    flag = False
                    break;
            if(flag):
                answer = sheet.cell(i,7).value;
                return answer
    return ''
def getAnswerForJudge(topic,workbook):
    sheet = workbook.sheet_by_name('判断题')
    size = len(sheet.col_values(0))
    for i in range(0,size):
        if sheet.cell(i,0).value==topic['title'].replace('&nbsp;',''):
            answer = sheet.cell(i,2).value;
            return answer
    return ''