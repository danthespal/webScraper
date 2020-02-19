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
    def parse(self, response):
        # initialization of item instance
        items = WebscraperItem()
        product_content = response.xpath("//div[@class='card-section-wrapper js-section-wrapper']")

        # simple loop
        for product in product_content:
            loader = ItemLoader(item=WebscraperItem(), selector=product)
            loader.add_xpath('product_name', './/a[@class="product-title js-product-url"]/text()')
            loader.add_css('product_price', '.product-new-price::text')
            loader.add_css('product_initial_price', 's::text')
            loader.add_css('product_image', '.lozad::attr(data-src)')

            # build a list with scraped items
            yield loader.load_item()

            # extract data from multiple pages
            next_page = response.css('#listing-paginator li:last-child a::attr(href)').get()
            if next_page is not None and next_page != "javascript:void(0)":
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)




