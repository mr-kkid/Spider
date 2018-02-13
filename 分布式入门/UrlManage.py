#encoding=UTF-8
import cPickle

class UrlManage():
    def __init__(self):
        self.new_urls=self.load_process("new_urls.txt")
        self.old_urls=self.load_process("old_urls.txt")


    def add_new_url(self,url):
        if url is None:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url=url)

    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


    def has_new_url(self):
        return self.new_urls_size()

    def new_urls_size(self):
        return len(self.new_urls)

    def old_urls_size(self):
        return len(self.old_urls)

    def save_process(self,path,urls):
        with open(path,"wb") as f:
            cPickle.dump(urls,f)

    def load_process(self,path):
        print "加载的文件%s"%(path)
        try:
            with open(path,"rb") as f:
                file=cPickle.load(f)
            return file
        except Exception as e:
            print e
        return set()
