# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TutorialPipeline(object):
    def process_item(self, item, spider):
        with open('cnblog.txt','w') as z:
            chexing = item['chexing']
            jiage = item['jiage']
            gonglishu = item['gonglishu']
            shoucishangpai = item['shoucishangpai']
            pailiang = item['pailiang']
            biansuxiang = item['biansuxiang']
            for a,b,c,d,e,f in zip(chexing,jiage,gonglishu,shoucishangpai,pailiang,biansuxiang):
                z.write(a + ':' + b + ':' + c + ':' + d + ':' + e + ':' + f + '\n')
        return item
