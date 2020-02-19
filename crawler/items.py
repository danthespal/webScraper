# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def remove_trash(text):
    text = text.strip(u'\u2122')
    return text

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field(
        input_processor=MapCompose(remove_trash, str.strip),
        output_processor=TakeFirst()
    )
    product_price = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )