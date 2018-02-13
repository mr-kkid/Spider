#encoding=UTF-8
import requests
import urllib
from bs4 import BeautifulSoup
import time

num=1;

for page in range(2):
    url='http://www.ivsky.com/search.php?q=saber'+str('&PageNo=')+str(page+1)
    print url
    headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }

    res=requests.get(url=url,headers=headers)
    print res.status_code
    text=res.content
    soup=BeautifulSoup(text,'lxml',from_encoding='UTF-8')
    urls=[]


    for a in soup.find_all('img'):
        title=a.get('alt')
        url=a.get('src')
        urls.append([title,url])
        print url

    def Schedule(blocknum,blocksize,totalsize):
        per=100*blocknum*blocksize/totalsize
        if per>100:
            per=100
        print "当前的下载进度是%d%%" % (per)


    for title,url in urls:
        print title+':'+url
        urllib.urlretrieve(url,'/home/liwenshi/saber/'+title.encode('utf-8')+str(num)+'.jpg',Schedule)
        num=num+1
    print 'first %d '%(page+1)
    print 'page end\n'
