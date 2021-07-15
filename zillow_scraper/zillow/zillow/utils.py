from http.cookies import SimpleCookie

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.36209991088865%2C%22east%22%3A-80.1399700891113%2C%22south%22%3A25.63872197154642%2C%22north%22%3A25.906464012835883%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=6'

def cookie_parser():
    cookie_string = '''zguid=23|%2407ef1bd6-39f5-4ac4-ac6c-5f2a4d4f6e0d; zgsession=1|d3ecd6ba-feee-4056-a234-4ede7a2ec3ea; _ga=GA1.2.198932056.1614180440; _gid=GA1.2.1312042356.1614180440; zjs_user_id=null; zjs_anonymous_id=%2207ef1bd6-39f5-4ac4-ac6c-5f2a4d4f6e0d%22; _pxvid=c93b73b5-76b4-11eb-9933-0242ac12000f; _gcl_au=1.1.588337040.1614180441; KruxPixel=true; DoubleClickSession=true; _fbp=fb.1.1614180442100.722946559; _pin_unauth=dWlkPVl6a3lPRFUyT1RndFlUaGxNQzAwTnpOakxUZ3haR010WW1abE5EbGxaakU0TkRKaA; g_state={"i_p":1614187645353,"i_l":1}; KruxAddition=true; _gac_UA-21174015-56=1.1614180476.Cj0KCQiAj9iBBhCJARIsAE9qRtDqWwKhMVWK9RSxfMPUEILhJjoX6kNVUBqCi2ZtU7E1l1Vl5agEf6IaApIeEALw_wcB; _gcl_aw=GCL.1614180476.Cj0KCQiAj9iBBhCJARIsAE9qRtDqWwKhMVWK9RSxfMPUEILhJjoX6kNVUBqCi2ZtU7E1l1Vl5agEf6IaApIeEALw_wcB; ki_r=; __gads=ID=d0dee6576ed35664:T=1614180483:S=ALNI_MaOTbQfRmW40p8FNkWusNh_AcnzOw; ki_s=; _gat=1; JSESSIONID=20B1896C4642EB16F043B1625CDB7D1F; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_bsco=1; _px3=309d657612d6526608f30b7640c1bbda0eeee101bc783f6d6d7670a19e43bf97:xfwSfj6IAz20Z8bDlY8FK/GaojGCY/dUHraMKK0d1fwPpxnL4wLoKDYy9Sj+bLL8N8ZrlemMx/b91//mbXCDDQ==:1000:yOde+aCwq24ovJ2WtF6xAnaHisVNm2+wYGHH0dA3g3sgA92bLMoyuXpjISK9gZvhC7BkJN/uM1ckBZeonB5x/TCYxwoz1hy+wW2b4x7KZdHjNCY719vUgc2sgTtFGkPUVt+DaKroFXrfNDyUJdEoBfk+DHA4hUmk+pXweTpr47U=; _uetsid=c982b1d076b411eb9a7499600d9cf953; _uetvid=c982fce076b411eb8f8e95d354f07d60; AWSALB=EnDSN71p7bHmBrSxi8rSyIwonuCDSbPzcba9z3IIdFKsAda/dmY+0YL/FNi52ttBKDy3wXzE9GU5rOmIzPStXaiib1XxngO+1EtO8t0K7w72WgSo5/w70ogXp/pV; AWSALBCORS=EnDSN71p7bHmBrSxi8rSyIwonuCDSbPzcba9z3IIdFKsAda/dmY+0YL/FNi52ttBKDy3wXzE9GU5rOmIzPStXaiib1XxngO+1EtO8t0K7w72WgSo5/w70ogXp/pV; search=6|1616780541506%7Crect%3D25.906464012835883%252C-80.1399700891113%252C25.63872197154642%252C-80.36209991088865%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0912700%09%09%09%09%09%09; ki_t=1614180483175%3B1614180483175%3B1614188542375%3B1%3B30
'''
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies

