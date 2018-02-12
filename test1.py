#encoding=UTF-8
import requests
import json
from bs4 import BeautifulSoup
import csv
from collections import namedtuple
import codecs

url='http://seputu.com/'

req=requests.get(url=url)
soup=BeautifulSoup(req.content,'lxml',from_encoding='utf-8')
content=[]


for mulu in soup.find_all(class_='mulu'):
    h2=mulu.find('h2')
    if h2 != None:
        h2_title=h2.string
        list=[]
        for a in soup.find(class_='box').find_all('a'):
            href=a.get('href')
            box_title=a.string
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_title,'content':list})

with open("盗墓笔记.json",'wb') as fp:
    json.dump(content,fp=fp,indent=4)


with open("盗墓笔记.json",'rb') as fp:
    print json.load(fp)
    print '\n'

content=[]
for mulu in soup.find_all(class_='mulu'):
    h2=mulu.find('h2')
    if h2 != None:
        h2_title=h2.string.encode('UTF-8')
        for a in soup.find(class_='box').find_all('a'):
            href=a.get('href').encode('UTF-8')
            box_title=a.string.encode('UTF-8')
            list=(h2_title,href,box_title)
            content.append(list)

headers=["title",'href','real_title']

with open("盗墓笔记.csv","w") as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(content)

with open("盗墓笔记.csv","r") as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    Row=namedtuple('Row',headers);
    for row in f_csv:
        print Row(*row)

file=codecs.open("盗墓笔记.csv","r",'UTF-8')
lines=file.readlines()
for line in lines:
    print line.encode('utf-8')
file.close()