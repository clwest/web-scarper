import requests
from lxml import html
import re
import json
import csv
import click

def write_to_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

def write_to_csv(filename, data):
    headers = ['title', 'price', 'in_stock', 'description']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerow(data)


@click.command()
@click.option('--bookurl', default='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', help='Please provide a book url from books.toscrape.com')
@click.option('--filename', default='output.json', help='Please provide filename CSV/JSON')
def scrape(bookurl,filename):
    resp = requests.get(url=bookurl, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
})

    tree = html.fromstring(html=resp.text)
    product_main = tree.xpath("//div[contains(@class, 'product_main')]")[0]

    title = product_main.xpath(".//h1/text()")[0]
    price = product_main.xpath(".//p[1]/text()")[0]
    availability = product_main.xpath(".//p[2]/text()")[1].strip()
    in_stock = ''.join(list(filter(lambda x:x.isdigit(), availability)))
    description = tree.xpath("//div[@id='product_description']/following-sibling::p/text()")[0]


    book_information = {
        'title': title,
        'price': price,
        'in_stock': in_stock,
        'description': description
    }

    print(book_information)
    extension = filename.split('.')[1]

    if extension == "json":
        write_to_json(filename, book_information)
    elif extension == 'csv':
        write_to_csv(filename, book_information)
    else:
        click.echo("The extension you provied is not supported please use csv or json")

if __name__ == '__main__':
    scrape()
