# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChocolateItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
class ChocolateItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    description_array = scrapy.Field()
    price = scrapy.Field()
    weight = scrapy.Field()

