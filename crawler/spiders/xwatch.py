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
            name = "".join(name)
            name = name.strip()
            if name != "":
                list_name.append(name)
        
        for price in prices:
            price = "".join(price)
            price = price.strip()
            price = price.split("\\")[0]
            if price != "":
                list_price.append(price)


        i = 0
        while i < len(list_link):
            yield{  'link' : list_link[i],
                    'price' : list_price[i],
                    'name' : list_name[i],
                }
            i = i+1

       

        


                



        
        


