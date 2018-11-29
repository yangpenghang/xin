# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
from ..items import WangyiItem
class Keji(CrawlSpider):
    name = 'keji'
    # allowed_domains = ['']
    # start_urls = ['http://tech.163.com/']
    def start_requests(self):
        for i in range(1,10):
            url='http://tech.163.com/special/00097UHL/tech_datalist_0'+str(i)+'.js?callback=data_callback'
            yield scrapy.Request(url,self.parse_item)
    def parse_item(self, response):
        detail_url = re.findall('"docurl":"(.*?)"', response.text)
        for url in detail_url:
            yield scrapy.Request(url, self.parse)
    def parse(self, response):
        if response.xpath("//div[@id='epContentLeft']/h1/text()").extract_first():
            title=response.xpath("//title/text()").extract_first()
            print(title)
        else:
            raise Exception('title is null')

        if response.xpath("//div[@id='epContentLeft']/h1/text()").extract_first():
            laiyuan=response.xpath('//*[@id="ne_article_source"]/text()').extract_first()
            print(laiyuan)
        else:
            raise Exception('laiyuan is null')

        if response.xpath("//div[@id='endText']/p/text()").extract():
            zhengwen=response.xpath("//div[@id='endText']/p/text()").extract()
            print(zhengwen)
        else:
            raise Exception('zhengwen is null')

        if response.xpath('//*[@id="endText"]/div/span[2]/text()').extract_first()[5::]:
            zuozhe=response.xpath('//*[@id="endText"]/div/span[2]/text()').extract_first()[5::]
            print(zuozhe)
        else:
            raise Exception('zuozhe is null')

        if response.xpath("//p[@class='f_center']/img/@src").extract_first():
            tupian=response.xpath("//p[@class='f_center']/img/@src").extract_first()
            print(tupian)
        else:
            raise Exception('tupian is null')

        if response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract_first()[:36]:
            shijian=response.xpath('//*[@id="epContentLeft"]/div[1]/text()').extract_first()[:36]
            print(shijian)
        else:
            raise Exception('shijian is null')
        item = WangyiItem()
        item['title'] = title
        item['laiyuan'] = laiyuan
        item['zhengwen'] = zhengwen
        item['zuozhe'] = zuozhe
        item['tupian'] = tupian
        item['shijian'] = shijian
        yield item