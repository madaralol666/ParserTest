import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = "https://browser-info.ru/"
response = requests.get(link, headers = header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id="tool_padding")

    # Check JavaScript
check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f"JavaScript: {status_js}"
print(result_js)

    # Check Cookie
check_cookie = block.find('div', id = 'cookie_check')
status_cookie = check_cookie.find_all('span')[1].text
result_cookie = f"Cookie: {status_cookie}"

    # Check Flash
check_flash = block.find('div', id = 'flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f"Flash: {status_flash}"

    # Check User-agent
check_user = block.find('div', id = 'user_agent').text
print(result_js)
print(result_cookie)
print(result_flash)
print(check_user)
