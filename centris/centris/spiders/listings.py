import scrapy
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
import json


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca']

    position = {
        "startPosition": 0
    }
    
    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.centris.ca/UserContext/Lock',
            method='POST',
            headers={
                'x-requested-with': "f55b6e3a-d12d-4ee8-96e8-cc0945b6d271",
                'Content-Type': 'application/json'
            },
            body=json.dumps({'uc': 0}),
            callback=self.generate_uck
        )

    def generate_uck(self, response):
        uck = response.body
        query = {
            "query": {
                "UseGeographyShapes": 0,
                "Filters": [
                    {
                        "MatchType": "CityDistrictAll",
                        "Text": "Montréal (All boroughs)",
                        "Id": 5
                    }
                    ],
                "FieldsValues": [
                    {
                        "fieldId": "CityDistrictAll",
                        "value": 5,
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "Category",
                        "value": "Residential",
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "SellingType",
                        "value": "Rent",
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "LandArea",
                        "value": "SquareFeet",
                        "fieldConditionId": "IsLandArea",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "RentPrice",
                        "value": 0,
                        "fieldConditionId": "ForRent",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "RentPrice",
                        "value": 1500,
                        "fieldConditionId": "ForRent",
                        "valueConditionId": ""
                    }
                    ]
                },
                    "isHomePage": True
            }      
        yield scrapy.Request(
            url="https://www.centris.ca/property/UpdateQuery",
            method="POST",
            body=json.dumps(query),
            headers={
                'Content-Type': 'application/json',
                'x-requested-with': 'XMLHttpRequest',
                'x-centris-uc': 0,
                'x-centris-uck': uck
            },
            meta = {
                'uck': uck
            },
            callback=self.update_query
        )

    def update_query(self, response):
        uck = response.meta['uck']
        yield scrapy.Request(
            url="https://www.centris.ca/Property/GetInscriptions",
            method="POST",
            body=json.dumps(self.position), 
            headers={
                'content-type': 'application/json',
                'x-centris-uc': 0,
                'x-centris-uck': uck
            },
            callback=self.parse

        )


    def parse(self, response):
        resp_dict = json.loads(response.body)
        html = resp_dict.get('d').get('Result').get('html')

        sel = Selector(text=html)
        listings = sel.xpath("//div[@class= 'property-thumbnail-item thumbnailItem col-12 col-sm-6 col-md-4 col-lg-3']")


        for listing in listings:
            category = listing.xpath("normalize-space(.//span[@class='category']//div/text())").get()
            features = listing.xpath(".//div[@class='cac']/text()").get() #get only number of bedrooms 
            price = listing.xpath("//span[@itemprop='price']/text()").get()
            city = listing.xpath("//span[@class='address']/div[2]//text()").get() # 2 might be a Z
            url = listing.xpath(".//div[@class='shell']//a/@href").get()
            abs_url = f"https://www.centris.ca{url}"

            yield SplashRequest(
                url=abs_url,
                endpoint='execute',
                callback=self.parse_summary,
                args={
                    'lua_source': self.script
                }, 
                meta={
                    'cat': category,
                    'fea': features,
                    'pri': price,
                    'city': city,
                    'url': abs_url
                }
                
            )

        count = resp_dict.get('d').get('Result').get('count')
        increment_number = resp_dict.get('d').get('Result').get('inscNumberPerPage')

        if self.position['startPosition'] <= count:
            self.position['startPosition'] += increment_number
            yield scrapy.Request(
                url="https://www.centris.ca/Property/GetInscriptions",
                method="POST",
                body=json.dumps(self.position),
                headers = {
                    'Content-Type': 'application/json'
                },
                callback=self.parse
            )



    

    def parse_summary(self, response):
        address = response.xpath("//h2[@itemprop='address']/text()").get()
        description = response.xpath("//div[@itemprop= 'description']/text()").get()
        category = response.request.meta['cat']
        features = response.request.meta['fea']
        price = response.request.meta['pri']
        city = response.request.meta['city']
        url = response.request.meta['url']

        yield {
            'address': address,
            'category': category,
            'description': description,
            'features': features,
            'price':    price,
            'city': city,
            'url': url

        }
