#encoding=UTF-8
from  multiprocessing.managers import BaseManager #多进程管理器
from multiprocessing import Process,Queue #多进程---启动进程，队列
import time
from UrlManage import UrlManage
from OutputData import OutputData

class NodeManage():

    def start_manage(self,url_q,res_q):
        #注册网络通讯
        BaseManager.register("get_url_queue",callable=lambda :url_q)
        BaseManager.register("get_res_queue",callable=lambda :res_q)
        manage=BaseManager(address=("127.0.0.1",8001),authkey="baike")
        return manage


    def url_manage_pro(self,url_q,con_q,root_url):
        url_manage=UrlManage()
        url_manage.add_new_url(root_url)
        while(True):
            while(url_manage.has_new_url()):
                new_url=url_manage.get_new_url()
                url_q.put(new_url)
                print "The size of old_urls is %d" % (url_manage.old_urls_size())
                if(url_manage.old_urls_size()>200):
                    url_q.put("end")
                    print "爬虫结束，通知子节点"
                    #存储节点状态，晚点写
                    url_manage.save_process("new_urls.txt",url_manage.new_urls)
                    url_manage.save_process("old_urls.txt",url_manage.old_urls)
                    return

            try:
                if not con_q.empty():
                    new_urls=con_q.get()
                    url_manage.add_new_urls(new_urls)

            except BaseException as e:
                print e
                time.sleep(0.1)

    def result_solve_pro(self,res_q,con_q,sto_q):
        while(True):
            try:
                if not res_q.empty():
                    content=res_q.get()
                    if content['new_urls'] == "end":
                        #通知存储进程结束
                        sto_q.put("end")
                        return
                    #print content['new_urls']
                    con_q.put(content["new_urls"])
                    sto_q.put(content["data"])
                else:
                    time.sleep(0.1)

            except BaseException as e:
                time.sleep(0.1)


    def store_save_pro(self,sto_q):
        Output=OutputData()
        while(True):
            if not sto_q.empty():
                datas=sto_q.get()
                if datas=="end":
                    #通知存储进程结束
                    Output.Output_end()
                    return
                Output.Output_store(datas=datas)
            else:
                time.sleep(0.1)


if __name__=="__main__":

    #创建四个通讯队列
    url_q=Queue()  #URL派发队列
    res_q=Queue()  #结果返回队列
    con_q=Queue()  #URL返回队列
    sto_q=Queue()  #结果存储队列

    node=NodeManage()
    manage=node.start_manage(url_q=url_q,res_q=res_q)

    root_url='http://baike.baidu.com/view/284853.htm'
    url_manage_pro=Process(target=node.url_manage_pro,args=(url_q,con_q,root_url,))
    result_solve_pro=Process(target=node.result_solve_pro,args=(res_q,con_q,sto_q,))
    store_save_pro=Process(target=node.store_save_pro,args=(sto_q,))


    url_manage_pro.start()
    result_solve_pro.start()
    store_save_pro.start()
    manage.get_server().serve_forever()