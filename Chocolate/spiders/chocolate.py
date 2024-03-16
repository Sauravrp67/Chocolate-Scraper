import scrapy
from Chocolate.items import ChocolateItem


class chocolateSpider(scrapy.Spider):
    name = 'chocolate'
    start_url = ''
    allowed_url = []
    chocolateItem = ChocolateItem()
    category_index = 1

    def parse(self,response):
        chocolates = response.css('product-item.product-item')
        category_link = response.css('ul.header__linklist.list--unstyled li.header__linklist-item a::attr(href)').getall()

        
        for chocolate in chocolates:
            self.chocolateItem['category'] = category_link[self.category_index].split('/')[2].replace('-',' ').title()
            relative_url = chocolate.css('.product-item__info a').attrib['href']

            chocolate_url = 'https://www.chocolate.co.uk/' + relative_url

            yield response.follow(chocolate_url, callback = self.page_parse)
        self.category_index =+ 1
        if ~((self.category_index != len(category_link))):
            next_category_link = 'https://www.chocolate.co.uk/' + category_link[self.category_index]
        else:
            next_category_link = None

        yield response.follow(next_category_link, callback = self.parse)

    def page_parse(self,response):

        self.chocolateItem['url'] = response.url
        self.chocolateItem['name'] = response.css('h1.product-meta__title.heading.h3::text').get()
        self.chocolateItem['description_array'] = response.xpath('//div[@class="product-form__description rte"]/p/text()').getall()
        self.chocolateItem['Price'] = response.css('span.price.price--large::text').getall()[1]


