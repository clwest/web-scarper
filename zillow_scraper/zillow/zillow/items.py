# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    building_id = scrapy.Field()
    img_src = scrapy.Field()
    detail_url = scrapy.Field()
    status_type = scrapy.Field()
    status_text = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    min_baths = scrapy.Field()
    min_beds = scrapy.Field()
    id = scrapy.Field()
    id = scrapy.Field()
