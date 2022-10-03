import requests
from bs4 import BeautifulSoup
from multiprocessing import pool

date = {
    'name':'madaralol111',
    'name':'3Er53er5!'
}

# Sign In
logging = requests.get('https://www.roblox.com/login', auth =('madaralol111', '3Er53er5!'))
# bs4
soup_main_html = BeautifulSoup(logging, 'lxml')
robux = soup_main_html.find('span', id='nav-robux-amount').text

print(robux)