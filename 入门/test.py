import requests
from bs4 import BeautifulSoup

url='https://www.qiushibaike.com/'
req=requests.get(url=url)
content=req.content

soup=BeautifulSoup(content,'lxml',from_encoding='utf-8')
#print soup.prettify()
print soup.name
print soup.title