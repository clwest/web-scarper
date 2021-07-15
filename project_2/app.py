import requests
from lxml import html  
from urllib.parse import urljoin
from pymongo import MongoClient

def insert_to_db(list_currencies):
    client = MongoClient("mongodb://Chris:Parker$dog2@cluster0-shard-00-00.en2gs.mongodb.net:27017,cluster0-shard-00-01.en2gs.mongodb.net:27017,cluster0-shard-00-02.en2gs.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-m8j3h2-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["currencies"]
    collection = db["price"]
    for currencies in list_currencies:
        exists = collection.find_one({'_id': currencies['_id']})
        if exists:
            if exists['name'] == currency['name'] and (exists['price'] != currency['price'] or exists['market cap'] != currency['market cap'] or exists['change(24)'] != currency['change(24)']):
                collection.replace_one({'_id': exists['_id']}, currency)
                print(f"Old item: {exists} New Item: {currency}")
        else:
            collection.insert_one(currency)
    client.close()


def get(list_elements):
    try:
        return list_elements.pop(0)
    except:
        return ''

all_currencies = []

def scrape(url):
    resp = requests.get(url=url, headers={
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        })

    tree = html.fromstring(html=resp.content)

    currencies = tree.xpath("//div[@class= 'sc-16r8icm-0 sc-1teo54s-1 lgwUsc']")
    for currency in currencies:
        c = {
            '_id': int(get(currency.xpath(".//td[1]/text()"))),
            'name': get(currency.xpath(".//td[contains(@class, 'currency-name')]/a/text()")),
            'market cap': get(currency.xpath(".//td[contains(@class, 'market-cap')]/@data-usd")),
            'price': get(currency.xpath("./td[4]/a[@class='price']/@data-usd")),
            'change(24)': get(currency.xpath("//td[contains(@class, 'percent-change')]/@data-percentusd"))
        }

        all_currencies.append(c)

    next_page = tree.xpath("//ul[contains(@class, 'pagination')]/li/a[contains(text(), 'Next')")

    if len(next_page) != 0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scrape(url=next_page_url)
    
scrape(url="https://coinmarketcap.com")
insert_to_db(all_currencies)
    
print(len(all_currencies))
