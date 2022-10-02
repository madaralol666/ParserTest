from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import pickle
import time

# Подмена профиля Firefox + параметры для драйвераЫ
useragent = fake_useragent.UserAgent().random
service_geck = Service(executable_path=r'drivers/geckodriver.exe', log_path=os.devnull)
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)
options_user
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
    pickle.dump(driver.get_cookies(), open(f"{db_log_pass[0]}_cookies", "wb"))


def cookies():

    driver.get("https://www.roblox.com/Login")
    time.sleep(2)
    cookies = pickle.load(open(f"{db_log_pass[0]}_cookies", "rb"))
    
    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()  
