import scrapy
from ..items import CrawlerItem
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags
from scrapy.loader.processors import MapCompose

class XwatchSpider(scrapy.Spider):
    name = 'xwatch'
    allowed_domains = ['xwatch.vn']
    start_urls = ['https://xwatch.vn/dong-ho-nam-pc85.html']
    
    def parse(self, response):
        result = ItemLoader(item= CrawlerItem(),response= response)
        result.default_input_processor = MapCompose(remove_tags)   
        result.add_xpath("name","//div[@class = 'item']/div[@class = 'frame_inner']/h2")
        result.add_xpath("price","//div[@class = 'frame_inner']/div[@class = 'price_arae']/div[@class = 'price_current']")
        result.add_xpath("link","//div[@class = 'frame_inner']//img/@src")
        result.add_xpath("link","//div[@class = 'frame_inner']//img/@data-src")
        yield result.load_item()



        
        


