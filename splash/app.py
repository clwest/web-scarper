import requests
from lxml import html

extracted_data = []


script = '''
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(1))
    return splash:html()
'''

resp = requests.post(url='http://localhost:8050/run', json={
    'lua_source': script,
    'url': 'https://www.gearbest.com/flash-sale.html'
})

tree = html.fromstring(html=resp.content)

deals = tree.xpath("//li[contains(@class, 'goodsItem')]/div[@class='goodsItem_content']")
for deal in deals:
    product = {
        'name': deal.xpath(".//div[@class='goodsItem_title']/a/text()")[0].strip(),
        'url': deal.xpath(".//div[@class='goodsItem_title']/a/@href")[0],
        'original_price': deal.xpath(".//div[@class='goodsItem_delete']/del/@data-currency"),
        'discounted_price': deal.xpath(".//div[@class='goodsItem_detail']/span/@data-currency")[0]
    }
    extracted_data.append(product)

print(extracted_data)