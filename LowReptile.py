from urllib import request
from urllib import error
import os
import re
import time
from http.client import IncompleteRead
from random import randint

#下载页面
def getall(URL, FileName):  

    req_news = request.Request(URL,headers={'Connection':'close'})

    #请求详细页面
    response = request.urlopen(req_news)
    content = response.read()
    response.close()
    content = content.decode('UTF-8')

    #打开fie_name路径下的news.html文件,采用写入模式
    #若文件不存在,创建，若存在，清空并写入
    my_open = open(FileName + '.html', 'w', encoding="utf-8")

    #在文件中写入内容
    my_open.write(content)
    my_open.close()
    print('------------')
    print("\033[1;31;40m" + FileName +" download over !\033[0m")
    time.sleep(1)


#根据详细页面url获取目标字符串
def geturl(URL):
    req_news = request.Request(URL,headers={'Connection':'close'})

    #请求详细页面
    response = request.urlopen(req_news)
    content = response.read()
    response.close()

    #获取完整超链接
    res = r"<a href=.\./.*?.html.>.*?</a>"
    resUrl = r"(?<=\".).*?(?=\")"
    resStr = r"(?<=>).*?(?=<)"
    urls = re.findall(res, content.decode('utf-8'))
    result = []
    for u in urls:
        result.append([re.findall(resUrl, u)[0],re.findall(resStr, u)[0]])
    return result

if __name__ == "__main__":
    result = geturl("https://www.felixcloutier.com/x86/")
    for i in range(len(result)):
        getall("https://www.felixcloutier.com/x86" + result[i][0],result[i][1])
    print("\033[1;31;40m Success! \033[0m")