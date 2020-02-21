"""
The main goal in scraping is to extract structured data from unstructured sources,
typically, web pages. Scrapy spiders can return the extracted data as Python dicts.
While convenient and familiar, Python dicts lack structure: it is easy to make a
typo in a field name or return inconsistent data, especially in a larger project
with many spiders.

To define common output data format Scrapy provides the Item class.
Item objects are simple containers used to collect the scraped data.
They provide a dictionary-like API with a convenient syntax for declaring
their available fields.

Various Scrapy components use extra information provided by Items:
exporters look at declared fields to figure out columns to export,
serialization can be customized using Item fields metadata, trackref
tracks Item instances to help find memory leaks (see Debugging memory
leaks with trackref), etc.

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
"""

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_unicode(text):
    # strip the unicode product_name
    text = text.replace(u'\u00ae', '').replace(u'\u2122', '')
    return text


class WebscraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #
    # see https://docs.scrapy.org/en/latest/topics/loaders.html
    # to understand why we use loaders
    product_name = Field(
        input_processor=MapCompose(str.strip, remove_unicode),
        output_processor=TakeFirst()
    )
    product_price = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    product_initial_price = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    product_image = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    product_stock = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
