from time import sleep
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Подмена UserAgent
useragent = fake_useragent.UserAgent().random
options = Options()
options.add_argument(f'user-agent={useragent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chrome/chromedriver.exe')

#Ссылка + Рефреш
driver.get("https://ratings.tankionline.com/ru/user/Sniper")
driver.get(driver.current_url)

html = driver.page_source

#Парс данных (уменьшить, оптимизировать)
soup = BeautifulSoup(html, 'lxml')
nickname = soup.find('a', class_='user-info-panel__link').text
head_div = soup.find('div', class_='user-info-panel__head').text
rank_name = soup.find('span', class_='user-info-panel__rankname').text
progress_one = soup.find_all('bdo', class_='formatted-number')[0].text
progress_two = soup.find_all('bdo', class_='formatted-number')[1].text

#Вывод (мб переделать )
print(f"Nickname: {nickname.strip()}")
print(f"rank: {rank_name.strip()}")
print(f"Exp: {progress_one.strip()} / {progress_two.strip()}")

# сделать нормальную обработку и вывода прогресса
print(f"Exp to rank up: {int(progress_two.strip().replace(' ', ''))-int(progress_one.strip().replace(' ', ''))}")
