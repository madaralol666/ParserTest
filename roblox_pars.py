from logging import exception
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
from multiprocessing import Pool
from fake_useragent import UserAgent
import os
import pickle
import time
import lst_link


# Подмена профиля Firefox + параметры для драйвера
# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'


start_time = time.time()
useragent = UserAgent().random
service_geck = Service(log_path=os.devnull,
                       executable_path=r'drivers/geckodriver.exe')
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)
# options_user.add_argument('--headless')
driver = webdriver.Edge(service=service_geck, options=options_user)
driver.get("https://www.roblox.com/Login")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')


def log_in_roblox():

    # ссылка сайта
    driver.get("https://www.roblox.com/Login")

    # Ввод логина
    email_input = driver.find_element(By.ID, 'login-username')
    email_input.click()
    email_input.clear()
    email_input.send_keys(lst_link.db_log_pass[0])
    email_input.send_keys(Keys.ENTER)

    # Ввод пароля
    pass_input = driver.find_element(By.ID, 'login-password')
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys(lst_link.db_log_pass[1])
    pass_input.send_keys(Keys.ENTER)


def dump_cookies():
    # Создаем куки лог/пасса
    pickle.dump(driver.get_cookies(), open(f"{lst_link.db_log_pass[0]}_cookies", "wb"))


def login_via_cookies():
    # Вход через куки
    time.sleep(0.2)
    cookies = pickle.load(open(f"{lst_link.db_log_pass[0]}_cookies", "rb"))

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()


def main_pars():

    robux = soup.find('span', id='nav-robux-amount').text
    href_profile = soup.find('a', class_='text-link dynamic-overflow-container').get('href')
    driver.get(href_profile)

    html_main_profile = driver.page_source
    soup_main_profle = BeautifulSoup(html_main_profile, 'lxml')

    time.sleep(1)
    profile_header = soup_main_profle.find('div', class_='profile-header-top')
    display_name = profile_header.find(
        'h1', class_='profile-name text-overflow').text
    friends = profile_header.find_all(
        class_='font-header-2 ng-binding')[0].text
    followers = profile_header.find_all(
        class_='font-header-2 ng-binding')[1].text
    following = profile_header.find_all(
        class_='font-header-2 ng-binding')[2].text
    profile_stat = soup_main_profle.find(
        'p', class_='text-lead').text  # не работает- сделать

    print(
        f"Display Name: {display_name.strip()}" +
        f"\nRobux: {robux}" +
        f"\nFriends: {friends}" +
        f"\nFollowers: {followers}" +
        f"\nFollowing: {following}" +
        f"\nJoin Date: {profile_stat}"
    )
    

def inventory_pars():
    # Парсинг инвентаря
    soup_inventory = driver.page_source
    bs_soup_inventory = BeautifulSoup(soup_inventory, 'lxml')
    href_Inventory = bs_soup_inventory.find('a', id='nav-inventory').get('href')


    count_item = 0
    count_item_page = 0
    # for item_extend_href in lst_link.lst_main_item:
        # pars_href = href_Inventory + '/' + item_extend_href
    pars_href = 'https://www.roblox.com/users/1775781975/inventory/#!/models'
    driver.get(pars_href)
    time.sleep(3)
    html_item = driver.page_source
    soup_item = BeautifulSoup(html_item, 'lxml')
    items = soup_item.find_all('li', class_='list-item item-card ng-scope')
    count_item += len(items)
    print(f'Всего вещей: {count_item}')
    

# def inventory2():

#     # Заход в профиль
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'lxml')
#     href_profile = soup.find('a', class_='text-link dynamic-overflow-container').get('href')
#     driver.get(href_profile)

#     # Парсинг инвентаря
#     soup_inventory = driver.page_source
#     bs_soup_inventory = BeautifulSoup(soup_inventory, 'lxml')
#     href_Inventory = bs_soup_inventory.find('a', id='nav-inventory').get('href')


#     count_item = 0
#     for item_extend_href in lst_link.lst_first_item:
#         time.sleep(0.2)
#         pars_href = href_Inventory + '/' + item_extend_href
#         # pars_href = 'https://www.roblox.com/users/1775781975/inventory/' + item_extend_href
#         driver.get(pars_href)
#         html_item = driver.page_source
#         soup_item = BeautifulSoup(html_item, 'lxml')
#         items = soup_item.find_all('li', class_='list-item item-card ng-scope')
#         count_item += len(items)
#     print(f'Всего вещей: {count_item}')
#     driver.close
#     driver.quit


login_via_cookies()
inventory_pars()
print("--- %s seconds ---" % (time.time() - start_time))
