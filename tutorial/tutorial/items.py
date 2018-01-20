# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   # pass
class tongcheng_com(scrapy.Item):
    chexing = scrapy.Field()
    jiage = scrapy.Field()
    gonglishu = scrapy.Field()
    shoucishangpai = scrapy.Field()
    pailiang = scrapy.Field()
    biansuxiang = scrapy.Field()
