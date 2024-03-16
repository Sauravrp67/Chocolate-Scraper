import scrapy
from Chocolate.items import ChocolateItem


class chocolateSpider(scrapy.Spider):
    name = 'chocolate'
    start_url = ''
    allowed_url = []
    chocolateItem = ChocolateItem()

    def parse(self,response):
        chocolates = response.css('product-item.product-item')

        self.chocolateItem['category'] = response.css('').get()
        for chocolate in chocolates:
            relative_url = chocolate.css('.product-item__info a').attrib['href']

            chocolate_url = 'https://www.chocolate.co.uk/' + relative_url

            yield response.follow(chocolate_url, callback = self.page_parse)

        next_category_link = ''

        yield response.follow(next_category_link, callback = self.parse)

    def page_parse(self,response):

        self.chocolateItem['url'] = ''
        self.chocolateItem['description'] = ''
        self.chocolateItem['Price'] = ''

