import scrapy
from ..utils import URL, cookie_parser

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    

    def start_request(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse, 
            cookies = cookie_parser()
        )

    def parse(self, response):
        with open('initial_response.json', 'wb') as f:
            f.write(response.body)
