"""
After an item has been scraped by a spider, it is sent to the Item Pipeline
 which processes it through several components that are executed sequentially.

Each item pipeline component (sometimes referred as just “Item Pipeline”)
is a Python class that implements a simple method. They receive an item and
perform an action over it, also deciding if the item should continue through
the pipeline or be dropped and no longer processed.

Typical uses of item pipelines are:

cleansing HTML data
validating scraped data (checking that the items contain certain fields)
checking for duplicates (and dropping them)
storing the scraped item in a database

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
"""

from sqlalchemy.orm import sessionmaker
from .models import Product, db_connect, create_table
from scrapy.exceptions import DropItem
import logging


class DuplicatesScraperPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****DuplicatesScraperPipeline: database connected****")

    def process_item(self, item, spider):
        session = self.Session()
        exist_product_name = session.query(Product).filter_by(product_name=item["product_name"]).first()
        if exist_product_name is not None:  # the current product_name exists
            raise DropItem("Duplicate item found: %s" % item["product_name"])
            session.close()
        else:
            return item
            session.close()


class SaveWebscraperPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveWebscraperPipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        product = Product()
        item.setdefault('product_initial_price', 'NULL')

        product.product_name = item["product_name"]
        product.product_price = item["product_price"]
        product.product_initial_price = item["product_initial_price"]
        product.product_image = item["product_image"]

        session.add(product)
        session.commit()

        session.close()

        return item
