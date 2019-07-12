# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PricePipeline(object):
    def process_item(self, item, spider):
        price = item["price"]
        list_price = []
        for p in price:
            p = p.strip()
            list_price.append(p)
        item["price"] = list_price
        #handle price attribute when its have many space

        return item


class NamePipeline(object):
    def process_item(self,item,spider):
        name = item["name"]
        list_name = []
        for n in name:
            n = n.strip()
            n_split = n.split()
            n = n_split[0]
            list_name.append(n)
        
        item["name"] = list_name
        #handle name attribute when its have many space
        return item