# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import WebscraperItem


class CrawlerSpider(scrapy.Spider):
    # do not change name variables
    # from next 2 lines
    name = 'crawler'
    start_urls = ['https://www.emag.ro/laptopuri/c']

    # custom definitions
    page_number = 2

    def parse(self, response):
        # initialization of item instance
        items = WebscraperItem()
        product_content = response.xpath("//div[@class='card-section-wrapper js-section-wrapper']")

        # simple loop
        for product in product_content:
            loader = ItemLoader(item=WebscraperItem(), selector=product)
            loader.add_xpath('product_name', './/a[@class="product-title js-product-url"]/text()')

            # build a list with scraped items
            yield loader.load_item()

            # extract data from multiple pages
            next_page = 'https://www.emag.ro/laptopuri/p' + str(CrawlerSpider.page_number) + '/c'
            if CrawlerSpider.page_number <= 10:
                CrawlerSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse)


