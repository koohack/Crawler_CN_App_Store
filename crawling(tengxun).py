import os
import re
import time
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import codecs

def getAppSize(info):
    st = info.find_all('span')[0].text
    length=len(st)

    out=st[:length-1]
    if int(float(out)) > 400:
        return 1
    else:
        return 0

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
    for n in range(1, 29):
        a = str(n) + '.html'
        ############################################## change the file name for
        f = codecs.open(a, 'r', encoding='UTF8')  #
        soup = BeautifulSoup(f, "html.parser")  ##########
        info = soup.find_all('li')  ######################
        ##############################################

        b = str(n) + '.txt'
        ###################### change the file name for
        wf = open(b, 'w', encoding="utf-8")  #
        ######################

        count = 0
        nameAndNum = []
        urlList = []
        for i, item in enumerate(info):
            url = getDownLordURL(item)
            number = getDondLordNum(item)
            name = getAppName(item)

            if getAppSize(item):
                continue

            urlList.append(url)

            temp = []
            temp.append(name)
            temp.append(number)
            nameAndNum.append(temp)

        for i, url in enumerate(urlList):
            print(nameAndNum[i][0] + " is started.")
            fileName = str(n) + '-'
            fileName = fileName + str(i + 1) + 'a.apk'
            try:
                request.urlretrieve(url, fileName)
            except:
                pass

            writestring = str(i) + ". name :" + nameAndNum[i][0] + ", " + nameAndNum[i][1] + "\n"
            wf.write(writestring)
            time.sleep(10)
            print(nameAndNum[i][0] + " was downlorded.")
            print("--------------------------------------")

        wf.close()
        print("\nDownlord was finished!!!!!!!!")






