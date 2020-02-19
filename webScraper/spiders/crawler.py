# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import WebscraperItem


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    start_urls = ['https://www.emag.ro/laptopuri/c']

    def parse(self, response):
        items = WebscraperItem()
        product_content = response.xpath("//div[@class='card-section-wrapper js-section-wrapper']")

        for product in product_content:
            loader = ItemLoader(item=WebscraperItem(), selector=product)
            loader.add_xpath('product_name', './/a[@class="product-title js-product-url"]/text()')

            yield loader.load_item()


