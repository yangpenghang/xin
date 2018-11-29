# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
# from ..items import WurenjiItem
class Wrj(CrawlSpider):
    name = "wrj"
    allowed_domains =[]
    start_urls =[
        "http://www.81uav.cn/uav-news/4.html",
    ]
    rules=(
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/4_\d+.html", ), follow=True),
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html",restrict_css="div.news_left a"),callback="parse_item",follow=False),
        )

    def parse_item(self, response):
        # print(response.url)
        # title=response.xpath("//div[@class='news-list-box']/dl/ul/li/h5/a/text()").extract()
        sel=Selector(response)
        if sel.xpath("//h1/text()").extract_first():
            title=sel.xpath("//h1/text()").extract_first()
            print(title)
        else:
            title=''
            print(response.url)


        if sel.xpath("//div[3]/div[1]/div[1]/text()").extract()[-2]:
            laiyuan=sel.xpath("//div[3]/div[1]/div[1]/text()").extract()[-2]
            print(laiyuan)
        else:
            laiyuan=''


        # content=sel.xpath("//div[@id='article']/p/text()").extract()

        # if sel.xpath("//h1/text()").extract_first():
        #     title=sel.xpath("//h1/text()").extract_first()
        #     print(title)
        # else:
        #     title=''
        #     print(response.url)
        #
        # items=WurenjiItem()
        # items['title']=title
        # items['time']=time
        # items['content']=content
        # return items

