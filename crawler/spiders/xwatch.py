import scrapy,re
from ..items import CrawlerItem
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
from scrapy import Selector

class XwatchSpider(scrapy.Spider):
    name = 'xwatch'
    allowed_domains = ['xwatch.vn']
    start_urls = ['https://xwatch.vn/dong-ho-nam-pc85.html']
    
    def parse(self, response):
        result = CrawlerItem()

        names = response.xpath("//div[@class = 'frame_inner']/h2/a[@class = 'name']/text()").getall()
        prices = response.xpath("//div[@class = 'price_arae']/div[@class = 'price_current']/text()").getall()
        # links = response.xpath("//div[@class = 'item']/div[@class = 'frame_inner']").css("img::attr(src)").getall()
        links_first = response.xpath("//div[@class = 'frame_inner']").css("a img::attr(src)").getall()
        links_second = response.xpath("//div[@class = 'frame_inner']").css("a img::attr(data-src)").getall()
        list_name = []
        list_price = []
        list_link = []
        for l in links_first:
            list_link.append(l)
        for l in links_second:
            list_link.append(l)
        # import pdb 
        # pdb.set_trace()

        for name in names:
            index = 0
            s = ""
            while index < len(name):
                if (65 <= ord(name[index]) <= 90) or (97 <= ord(name[index]) <= 122) or (48 <= ord(name[index]) <= 57) :
                    s = s + name[index]
                index = index + 1
            if s != "":
                list_name.append(s)

        for price in prices:
            index = 0
            s = ""
            while index < len(price):
                if (65 <= ord(price[index]) <= 90) or (97 <= ord(price[index]) <= 122) or (48 <= ord(price[index]) <= 57) :
                    s = s + price[index]
                index = index + 1
            if s != "":
                list_price.append(s)
                 
        i = 0
        while i < len(list_link):
            yield{  'link' : list_link[i],
                    'price' : list_price[i],
                    'name' : list_name[i],
                }
            i = i+1

       

        


                



        
        


