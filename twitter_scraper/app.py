import requests
from lxml import html
from fake_useragent import UserAgent


s = requests.Session()
ua = UserAgent
s.headers.update({
    'User-Agent': ua.RANDOM
})

login_resp = s.get(url='https://twitter')