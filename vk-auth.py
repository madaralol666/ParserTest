from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import fake_useragent
import time
import os

# тему с устаревшим браузером невозможно пофиксить, вчера мы нашли абуз
# в стары бразуерах можно сразу login/pass
# в новых динамические ссылки то есть SMS код

# Подмена профиля firefox
useragent = fake_useragent.UserAgent().firefox
service_geck = Service(executable_path=r'drivers/geckodriver.exe', log_path=os.devnull)
options_user = Options()
options_user.set_preference("general.useragent.override", useragent)
options_user.set_preference("javascript.enabled", True)

driver = webdriver.Firefox(service=service_geck, options=options_user)

try:
    driver.get("https://vk.com/")
    time.sleep(2.3)

# Ввод логина
    email_input = driver.find_element(By.ID,'index_email')
    email_input.click()
    email_input.clear()
    email_input.send_keys("89646810694")
    email_input.send_keys(Keys.ENTER)

    time.sleep(3.5)

# Ввод пароля
    pass_input = driver.find_element(By.ID,'index_pass')
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys("zxc123457")
    pass_input.send_keys(Keys.ENTER)

    time.sleep(2)

    driver.get('https://m.vk.com')
    
except Exception as ex:
    print(ex)
