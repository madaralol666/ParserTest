from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import pickle
import time

# Подмена профиля Firefox + параметры для драйвера
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
service_geck = Service(executable_path=r'drivers/geckodriver.exe', log_path=os.devnull)
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)
# options_user.add_argument('--headless')
driver = webdriver.Firefox(service=service_geck, options=options_user)

db_log_pass = ["madaralol111", "3Er53er5!"]

def log_in_roblox():

    #ссылка сайта 
    driver.get("https://www.roblox.com/Login")

    # Ввод логина
    email_input = driver.find_element(By.ID,'login-username')
    email_input.click()
    email_input.clear()
    email_input.send_keys(db_log_pass[0])
    email_input.send_keys(Keys.ENTER)

    # Ввод пароля
    pass_input = driver.find_element(By.ID,'login-password')
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys(db_log_pass[1])
    pass_input.send_keys(Keys.ENTER)


def dump_cookies():
    # Создаем куки лог/пасса
    pickle.dump(driver.get_cookies(), open(f"{db_log_pass[0]}_cookies", "wb"))


def login_via_cookies():
    # Вход через куки
    driver.get("https://www.roblox.com/Login")
    time.sleep(2)
    cookies = pickle.load(open(f"{db_log_pass[0]}_cookies", "rb"))
    
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()  


login_via_cookies()

def main_pars():

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    robux = soup.find('span', id='nav-robux-amount').text
    href_profile = soup.find('a', class_='text-link dynamic-overflow-container').get('href')
    driver.get(href_profile)

    html_main_profile = driver.page_source
    soup_main_profle = BeautifulSoup(html_main_profile, 'lxml')

    time.sleep(1)
    profile_header = soup_main_profle.find('div', class_='profile-header-top')
    display_name = profile_header.find('h1', class_='profile-name text-overflow').text
    friends = profile_header.find_all(class_='font-header-2 ng-binding')[0].text
    followers = profile_header.find_all(class_='font-header-2 ng-binding')[1].text
    following = profile_header.find_all(class_='font-header-2 ng-binding')[2].text
    profile_stat = soup_main_profle.find('p', class_='text-lead').text # не работает- сделать 

    # Парсинг инвентаря
    count_item = 0
    href_Inventory = soup_main_profle.find('a', class_='btn-min-width btn-secondary-xs btn-more inventory-link see-all-link-icon ng-binding').get('href')
    href_Inventory1 = href_Inventory + '#!/accessories'
    driver.get(href_Inventory1)

    html_inventory = driver.page_source
    soup_inventory = BeautifulSoup(html_inventory, 'lxml')

    # Добавление всех  (str)предметов в List 
    lst_second_item = ['#!/accessories/head']
    for item_second in range(0, 47):
        str_second_item = soup_inventory.find_all('li', class_='menu-secondary-option ng-scope')[item_second].get('href')
        lst_second_item.append(str_second_item)


    # Счет всех предметов(без перехода на другой page(считается только page 1))
    # Работает хорошо, очень долгий(если на акке много предметов) тамй слип можно юзать 3
    # 1. Сделать мега полный чекер
    # 2. доработать имеющийся
    for item_extend_href in lst_second_item:
        time.sleep(0.3)
        pars_href = href_Inventory + item_extend_href
        # pars_href = 'https://www.roblox.com/users/1775781975/inventory/' + item_extend_href
        driver.get(pars_href)
        html_item = driver.page_source
        soup_item = BeautifulSoup(html_item, 'lxml')             
        items = soup_item.find_all('li', class_='list-item item-card ng-scope')
        count_item += len(items)
        print(count_item)
    
        
        
        

    

    # print(
    # f"Display Name: {display_name.strip()}"+
    # f"\nRobux: {robux}"+
    # f"\nFriends: {friends}"+ 
    # f"\nFollowers: {followers}"+
    # f"\nFollowing: {following}"+
    # f"\nJoin Date: {profile_stat}"
    # ) 

main_pars()

