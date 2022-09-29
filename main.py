from unittest import main
import requests
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
brw = webdriver.Firefox()
brw.get("https://ratings.tankionline.com/ru/user/Sniper")
brw.get(brw.current_url)
html = brw.page_source
soup = BeautifulSoup(html, 'lxml')
nickname = soup.find('a', class_='user-info-panel__link').text
head_div = soup.find('div', class_='user-info-panel__head').text
rank_name = soup.find('span', class_='user-info-panel__rankname').text
progress_one = soup.find_all('bdo', class_='formatted-number')[0].text
progress_two = soup.find_all('bdo', class_='formatted-number')[1].text

print(f"Nickname: {nickname.strip()}")
print(f"rank: {rank_name.strip()}")
print(f"Exp: {progress_one.strip()} / {progress_two.strip()}")
# сделать нормальную обработку и вывода прогресса
print(f"Exp to rank up: {int(progress_two.strip().replace(' ', ''))-int(progress_one.strip().replace(' ', ''))}")








































# user = fake_useragent.UserAgent().random
# header = {'user-agent': user}

# link = "https://browser-info.ru/"
# response = requests.get(link, headers = header).text
# soup = BeautifulSoup(response, 'lxml')
# block = soup.find('div', id="tool_padding")

#     # Check JavaScript
# check_js = block.find('div', id='javascript_check')
# status_js = check_js.find_all('span')[1].text
# result_js = f"JavaScript: {status_js}"
# print(result_js)

#     # Check Cookie
# check_cookie = block.find('div', id = 'cookie_check')
# status_cookie = check_cookie.find_all('span')[1].text
# result_cookie = f"Cookie: {status_cookie}"

#     # Check Flash
# check_flash = block.find('div', id = 'flash_version')
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f"Flash: {status_flash}"

#     # Check User-agent
# check_user = block.find('div', id = 'user_agent').text
# print(result_js)
# print(result_cookie)
# print(result_flash)
# print(check_user)