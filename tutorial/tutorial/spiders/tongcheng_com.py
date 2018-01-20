#coding=utf-8
import scrapy
from tutorial.items import tongcheng_com

class tongcheng_com_Spider(scrapy.Spider):

    name = "tongcheng_com"
    allowed_domains = ["58.com"]
    start_urls = [
     'http://qd.58.com/ershouche/32545738041658x.shtml',
    ]

    def parse(self, response):
        item = tongcheng_com()
        item['chexing'] = response.xpath('//p[@class="title_p"]/text()').extract()
        item['jiage'] = response.xpath('//span[@class="price_span"]/span[@class="jiage"]/text()').extract()
        item['gonglishu'] = response.xpath(u"//span[text()='本车排量']/../../li[2]/span[2]/text()").extract()
        item['shoucishangpai'] = response.xpath(u"//span[text()='上牌时间']/../span[2]/text()").extract()
        item['pailiang'] = response.xpath(u"//span[text()='本车排量']/../span[2]/text()").extract()
        item['biansuxiang'] = response.xpath(u"//span[text()='变速箱']/../span[2]/text()").extract()
        return item
        #yield item
