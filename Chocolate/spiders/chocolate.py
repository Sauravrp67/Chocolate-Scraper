import scrapy
from Chocolate.items import ChocolateItem


class chocolateSpider(scrapy.Spider):
    name = 'chocolate'
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/easter-2020"]
    chocolateItem = ChocolateItem()
    category_index = 1

    def parse(self,response):
        category_link = response.css('ul.header__linklist.list--unstyled li.header__linklist-item a::attr(href)').getall()





      

    # def page_parse(self,response):

    #     self.chocolateItem['url'] = response.url
    #     self.chocolateItem['name'] = response.css('h1.product-meta__title.heading.h3::text').get()
    #     self.chocolateItem['description_array'] = response.xpath('//div[@class="product-form__description rte"]/p/text()').getall()
    #     self.chocolateItem['price'] = response.css('span.price.price--large::text').getall()[1]
    #     print("*******Name*********")
    #     print(self.chocolateItem['name'])


