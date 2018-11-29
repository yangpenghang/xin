#-*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import DayinhuItem

class Dayin(CrawlSpider):
    name = "dayin"
    allowed_domains =[]
    start_urls =[
    "http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF"
    ]

    rules = (
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+", ),follow=True),
        Rule(LinkExtractor(allow="http://www.dayinhu.com/news/\d{6}\.html",restrict_css="h1.entry-title a"),callback="parse_item",follow=False),)
    def parse_item(self, response):
        # print(response.url)
        sel = Selector(response)