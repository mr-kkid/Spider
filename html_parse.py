from bs4 import BeautifulSoup
import re
import urlparse

class html_parse():
    def parser(self,content,url):
        self.url=url
        self.soup=BeautifulSoup(content,'lxml',from_encoding='utf-8')
        self.urls=self.get_urls()
        self.datas=self.get_datas()
        return self.urls,self.datas

    def get_datas(self):
        url=self.url
        title=self.soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        summary=self.soup.find('div',class_='lemma-summary').get_text()
        url=url.encode("utf-8")
        title=title.encode("utf-8")
        summary=summary.encode("utf-8")
        data = (url, title, summary)
        return data

    def get_urls(self):
        urls=set()
        all=self.soup.find_all('a',href=re.compile(r'/item/.*'))
        for a in all:
            url=a['href']
            urls.add(urlparse.urljoin(self.url,url))
        return urls