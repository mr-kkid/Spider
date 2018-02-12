#encoding=UTF-8
import csv
import codecs
import json

class data_save():
    def data_save(self,datas):
        headers=("URL","标题","解释")
        with open("爬虫数据.csv","w") as f:
            f_csv=csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(datas)
        with open("爬虫数据.json","w",) as fp:
            json.dump(datas,fp=fp,indent=4,ensure_ascii=False,encoding='utf-8')