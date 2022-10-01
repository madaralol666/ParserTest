from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
import os

useragent = fake_useragent.UserAgent().random
service_geck = Service(executable_path=r'drivers/geckodriver.exe', log_path=os.devnull)
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)

driver = webdriver.Firefox(service=service_geck, options=options_user)

# Ссылка + Рефреш
driver.get("https://ratings.tankionline.com/ru/user/Sniper")
driver.get(driver.current_url)

html = driver.page_source

# Парс данных (уменьшить, оптимизировать)
soup = BeautifulSoup(html, 'lxml')
nickname = soup.find('a', class_='user-info-panel__link').text
rank_name = soup.find('span', class_='user-info-panel__rankname').text
progress_one = soup.find_all('bdo', class_='formatted-number')[0].text
progress_two = soup.find_all('bdo', class_='formatted-number')[1].text

# Вывод (мб переделать )
print(f"Nickname: {nickname.strip()}")
print(f"rank: {rank_name.strip()}")
print(f"Exp: {progress_one.strip()} / {progress_two.strip()}")

# сделать нормальную обработку и вывода прогресса
print(f"Exp to rank up: {int(progress_two.strip().replace(' ', ''))-int(progress_one.strip().replace(' ', ''))}")

