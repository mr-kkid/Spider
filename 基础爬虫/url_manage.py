
class url_manage():
    def __init__(self):
        self.old_urls=set()
        self.new_urls=set()

    def has_new_url(self):
        return self.new_url_size()!=0

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
            self.add_new_url(url)

    def get_new_url(self):
        url=self.new_urls.pop()
        self.old_urls.add(url)
        return url;

    def old_url_size(self):
        return len(self.old_urls)

    def new_url_size(self):
        return len(self.new_urls)