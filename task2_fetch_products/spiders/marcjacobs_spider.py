import scrapy
import ast


class MarcjacobsSpider(scrapy.Spider):
    name = 'marcjacobs'
    start_urls = ['https://www.marcjacobs.com/']

    def parse(self, response):
        for href in response.css('a.nav-link'):
            yield response.follow(href, self.parse_categories)

    def parse_categories(self, response):
        for a in response.css('a.link'):
            yield response.follow(a, self.parse_product)

    def parse_product(self, response):
        product_data = ast.literal_eval(response.css('div::attr(data-qubit-product-data)').get())
        details = product_data['product']
        old_price = details['price']
        new_price = details['originalPrice']

        yield {
            'product_id': details['productId'],
            'name': details['name'],
            'description': details['description'],
            'currency': response.css('meta[itemprop*=priceCurrency]::attr(content)').get(),
            'old_price': old_price['value'],
            'new_price': new_price['value'],
            'images': response.css('picture img::attr(src)').getall(),
            'color_names': response.css('a::attr(data-attr-display-value)').getall(),
            'color_codes': response.css('span.color-value::attr(data-attr-value)').get(),
            'sizes':  response.css('span.size-value::text').getall()

            # 'name': response.css('span.clearfix::text').get(),
            # 'price': response.css('span.value::attr(content)').get(),
            # 'images': response.css('picture img::attr(src)').getall(),
            # 'currency': response.css('meta[itemprop*=priceCurrency]::attr(content)').get(),
            # 'color_names': response.css('a::attr(data-attr-display-value)').getall(),
            # 'color_codes': response.css('span.color-value::attr(data-attr-value)').get(),
        }

