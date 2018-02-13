#encoding=UTF-8
from html_download import html_download
from html_parse import html_parse
from url_manage import url_manage
from data_save import data_save


class spider_manage():
    def __init__(self):
        self.manage=url_manage()
        self.data_save=data_save()
        self.html_download=html_download()
        self.html_parse=html_parse()

    def crawl(self,root_url):
        self.manage.add_new_url(root_url)
        datas=[]
        while(self.manage.has_new_url() and self.manage.old_url_size()<100):
            try:
                url=self.manage.get_new_url()
                content=self.html_download.html_download(url=url)
                urls,data=self.html_parse.parser(content=content,url=url)
                self.manage.add_new_urls(urls)
                if data is not None:
                    datas.append(data)
                print "已经抓了%d个网页" % (self.manage.old_url_size())
            except Exception as e:
                print "Crawl Failed"
        self.data_save.data_save(datas=datas)


if __name__=="__main__":
    root_url='http://baike.baidu.com/view/284853.htm'
    spider_man=spider_manage()
    spider_man.crawl(root_url=root_url)