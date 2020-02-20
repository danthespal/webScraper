'''
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper
that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns,
designed for efficient and high-performing database access, adapted into
a simple and Pythonic domain language.
See: https://www.sqlalchemy.org/

Here, I use Object-Relational Mapping (ORM) to query and manipulate data
from the database using the object-oriented paradigm. In particular, I use SQLAlchemy.
I won’t cover the details of ORM and please refer to this article for some Pros and Cons.
See: https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a
'''

from scrapy.utils.project import get_project_settings
from sqlalchemy import (
    Integer, String, Text)
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class Product(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    product_name = Column('product_name', String(200), unique=True)
    product_price = Column('product_price', String(10))
    product_initial_price = Column('product_initial_price', String(10))
    product_image = Column('product_image', Text())