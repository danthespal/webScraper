
![enter image description here](https://scrapy.org/img/scrapylogo.png)
# webScraper
webScraper is a application made in python by community with love, the purpose of this project is purely educational, all those who have contributed to this project, we do this to learn, and most importantly to improve the quality of the internet in the environment we live in. By mining, exploiting / manipulating and distributing the data that the application manages, it does not want to do harm or good to a particular company.
If, however, you choose to use this program for malicious purposes, we as a community or as an individual, do not assume any risk of a legal nature.

# webScraper requirements:
- Scrapy framework 1.8.0
- scrapy-user-agents 0.1.1
- scrapy-proxy-pool 0.1.6
- SQLAlchemy 1.3.13
- Build Tools (C++)
- PyCharm (Optional IDE but recommended)

If you use Pycharm, the following libraries will be detected as missing and installed automatically
if not, you can manually install them by:
```
foo@bar:~$ pip install -r requirements.txt
```

# USAGE

see the output in terminal
```
foo@bar:~$ scrapy crawl crawler
```
drop items into file, you can use xml and csv types
```
foo@bar:~$ scrapy crawl crawler -o items.json
```

# TODOS
 - ~~base structure for downloading items~~
 - ~~user agent~~
 - ~~download_delay and auto_throttle for better scraping~~
 - ~~download from multiple pages~~
 - ~~database to store the scraped data~~
 - ~~check for duplicates product_name~~
 - establish list of sites
 - remove unicode from product names
 - customization for product items
 - ... more will come
