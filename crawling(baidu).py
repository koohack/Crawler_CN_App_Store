import os
import re
import time
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import codecs
import sys

def getDondLordNum(info):
    st=info.find_all('span')[1].text
    length=len(st)

    out=''
    if st[length-4:length-2]=="万次":
        downLordNum=st[3:length-4]
        temp='만회'
        out=downLordNum+temp
    elif st[length-4:length-2]=="亿次":
        downLordNum=st[3:length-4]
        temp='억회'
        out=downLordNum+temp
        out=out[2:]
    elif st[length-2:length]=="万次":
        downLordNum=st[2:length-2]
        temp='만회'
        out=downLordNum+temp
    elif st[length-2:length]=="亿次":
        downLordNum=st[2:length-2]
        temp='억회'
        out=downLordNum+temp

    return out

def getDownLordURL(info):
    st=info.find_all('a')[2]
    url=st['ex_url']

    return url

def getAppName(info):
    st=info.find_all('a')[2]
    name=st['appname']

    return name

if __name__=='__main__':
    for i in range(1, 10):
        count=1
        pagecount=str(i)
        pageurl = 'https://shouji.baidu.com/software/50' + pagecount + '/'
        if i>=10:
            pageurl='https://shouji.baidu.com/software/5' + pagecount + '/'


        writeTXT=pagecount+'-1.txt'

        for j in range(1, 9):
            pageinpagecount='list_'+str(j)+'.html'
            pageinpageurl=pageurl+pageinpagecount
            r=requests.get(pageinpageurl)
            r.encoding='urf-8'
            s=BeautifulSoup(r.text, 'html.parser')
            info=s.find_all('span', 'inst-btn-big quickdown')
            info1=s.find_all('span', 'down')


            for j, item in enumerate(info):

                wf = open(writeTXT, 'a', encoding="utf-8")
                downloadURL=item['data_url']
                name=str(item['data_name'].encode('utf-8').decode('utf-8'))


                downloadCount=info1[j].text
                length=len(downloadCount)

                if downloadCount[length-3:length-2] == '万':
                    downloadCount=downloadCount[:length-3]+'만회'
                else:
                    downloadCount=downloadCount[:length-3]+'억회'

                writeString = str(count) + '. ' + name + ', '+ downloadCount + '\n'
                wf.write(writeString)

                apkName=str(i)+'-'+str(count)+'.apk'
                print('start downlord '+name)
                request.urlretrieve(downloadURL, apkName)
                print(name+' was downlorded!!!!!!!!!!!')
                print('--------------------------------------------')
                time.sleep(14)
                count+=1
                wf.close()











