import scrapy


class Product(scrapy.Item):
    product_id = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    availability = scrapy.Field()
    currency = scrapy.Field()
    color_code = scrapy.Field()
    color_name = scrapy.Field()
    size = scrapy.Field()
    stock = scrapy.Field()
    old_price = scrapy.Field()
    new_price = scrapy.Field()
    skus = scrapy.Field()
    images = scrapy.Field()
