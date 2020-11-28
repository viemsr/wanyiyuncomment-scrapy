# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    total = scrapy.Field()
    # file_urls = scrapy.Field()
    # file = scrapy.Field()
    # descrion = scrapy.Field()
    # company = scrapy.Field()
    
