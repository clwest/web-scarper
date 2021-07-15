from lxml import etree

tree = etree.parse("src/web_page.html")
html = tree.getroot()
title_element = html.cssselect("title")[0]
print(title_element.text)

p_element = html.cssselect("p")[0]
print(p_element.text)

list_items = html.cssselect("li") 
for li in list_items:
    a = li.cssselect("a")
    if len(a) == 0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")