import requests


class html_download():

    def html_download(self,url):
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
            }
        if url is None:
            return
        res=requests.get(url=url,headers=headers)
        if res.status_code==200:
            return res.content
        return None

