# -*- coding: utf-8 -*-
# webScraper v0.1 alpha
# author: laurovici.daniel@gmail.com
# file: spider.py

import scrapy
from scrapy.loader import ItemLoader
from ..items import CrawlerItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://www.emag.ro/laptopuri/p1/c']

    def parse(self, response):
        items = CrawlerItem()
        product_content = response.xpath("//div[@class='card-section-wrapper js-section-wrapper']")

        for product in product_content:
            loader = ItemLoader(item=CrawlerItem(), selector=product)
            loader.add_xpath('product_name', ".//a[@class='product-title js-product-url']/text()")
            loader.add_xpath('product_price', ".//p[@class='product-new-price']/text()")

            yield loader.load_item()
