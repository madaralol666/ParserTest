import requests
from bs4 import BeautifulSoup
from multiprocessing import pool
from fake_useragent import UserAgent
date = {
    'name':'madaralol111',
    'name':'3Er53er5!'
}
useragent = UserAgent().chrome
header = {
    'User-Agent': useragent
}

# Sign In
session = requests.Session()
response = session.get('https://www.gismeteo.ru/weather-novomoskovsk-11474/', headers=header)
print(response.json)