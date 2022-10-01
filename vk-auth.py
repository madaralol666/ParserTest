from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import fake_useragent
import pickle
import time
import os

# тему с устаревшим браузером невозможно пофиксить, вчера мы нашли абуз
# в стары бразуерах можно сразу login/pass
# в новых динамические ссылки то есть SMS код

db_log_pass = ["89646810694", "zxc123457"]

# Подмена профиля firefox
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
service_geck = Service(executable_path=r'drivers/geckodriver.exe', log_path=os.devnull)
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)


driver = webdriver.Firefox(service=service_geck, options=options_user)


def input_data():
    
    driver.get("https://vk.com/")
    time.sleep(2.3)

    # Ввод логина
    email_input = driver.find_element(By.ID, 'index_email')
    email_input.click()
    email_input.clear()
    email_input.send_keys(db_log_pass[0])
    email_input.send_keys(Keys.ENTER)

    time.sleep(3.5)

    driver.current_url

    # Ввод пароля
    pass_input_by_name = driver.find_element(By.NAME, 'password')

    pass_input_by_name.click()
    pass_input_by_name.clear()
    pass_input_by_name.send_keys(db_log_pass[1])
    pass_input_by_name.send_keys(Keys.ENTER)


def dumb_cookies():
    pickle.dump(driver.get_cookies(), open(f"{db_log_pass[0]}_cookies_vk", "wb"))


# у вк траблы с кукисами 
def cookies():

    driver.get("https://vk.com/")
    time.sleep(2)
    
    for cookie in pickle.load(open(f"{db_log_pass[0]}_cookies_vk", "rb")):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
