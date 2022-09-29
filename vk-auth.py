from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import fake_useragent
import time
import os
from selenium.webdriver.common.by import By

auth_data = '89531945840'

# options
useragent = fake_useragent.UserAgent().random
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent)
# user-agent

driver = webdriver.Firefox(firefox_profile=profile, service_log_path=os.devnull, executable_path=r'geck/geckodriver.exe')

try:
    driver.get("https://vk.com/")
    time.sleep(2.3)

#Ввод логина
    email_input = driver.find_element(By.ID,'index_email')
    email_input.click()
    email_input.clear()
    email_input.send_keys("email")
    email_input.send_keys(Keys.ENTER)

    time.sleep(3.5)

#Ввод пароля
    pass_input = driver.find_element(By.ID,'index_pass')
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys("password")
    pass_input.send_keys(Keys.ENTER)

    time.sleep(2)

#мега мув 3000
    driver.get('https://m.vk.com')
    
except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()