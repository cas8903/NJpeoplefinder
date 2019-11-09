import scrapy

class scrapyTut(scrapy.item):
    title = scrapy.Field()
    url = scrapy.Field()
    details = scrapy.Field()
