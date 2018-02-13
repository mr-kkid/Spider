#encoding=UTF-8

from multiprocessing.managers import BaseManager
from HtmlParser import html_parse
from HtmlDownload import html_download

class SpiderWork():
    def __init__(self):

        BaseManager.register("get_url_queue")
        BaseManager.register("get_res_queue")
        server_addr='127.0.0.1'
        self.num=0
        self.manage=BaseManager(address=(server_addr,8001),authkey="baike")
        self.manage.connect()
        self.url_queue=self.manage.get_url_queue()
        self.res_queue = self.manage.get_res_queue()
        self.htmlparse=html_parse()
        self.htmldownload=html_download()

    def Crawl(self):
        while(True):
            try:
                if  not self.url_queue.empty():
                    url=self.url_queue.get()
                    print url
                    if url =="end":
                        self.res_queue.put({"new_urls":"end","data":"end"})
                        return
                    print self.num+1
                    self.num=self.num+1
                    content=self.htmldownload.html_download(url)
                    urls,datas=self.htmlparse.parser(url=url,content=content)
                    self.res_queue.put({"new_urls":urls,"data":datas})
            except EOFError as e:
                print "连接失败"

            except Exception as e:
                print e
                print "爬虫失败"



if __name__=="__main__":
    spider_man=SpiderWork()
    spider_man.Crawl()