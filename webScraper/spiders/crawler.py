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
        self.logger.info('Parse function called on {}'.format(response.url))
        # initialization of item instance
        product_content = response.xpath("//div[@class='card-section-wrapper js-section-wrapper']")

        # simple loop
        for product in product_content:
            loader = ItemLoader(item=WebscraperItem(), selector=product)
            """
            XPath offers more features than pure CSS selection (the Wikipedia article gives a nice overview), 
            at the cost of being harder to learn. Scrapy converts CSS selectors to XPath internally, 
            so the .css() function is basically syntactic sugar for .xpath().
            * use xpath selector for better performance in the future
            """
            loader.add_xpath('product_name', './/a[@class="product-title js-product-url"]/text()')
            loader.add_xpath('product_price', './/p[@class="product-new-price"]/text()')
            loader.add_xpath('product_initial_price', './/s/text()')
            loader.add_xpath('product_image', './/img[@class="lozad"]/@data-src')

            # build a list with scraped items
            yield loader.load_item()

            # extract data from multiple pages
            next_page = response.css('#listing-paginator li:last-child a::attr(href)').get()
            if next_page is not None and next_page != "javascript:void(0)":
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
