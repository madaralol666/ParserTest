from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import fake_useragent
import time

auth_data = '89531945840'

# options
useragent = fake_useragent.UserAgent().random
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent)
# user-agent

driver = webdriver.Firefox(firefox_profile=profile,executable_path=r'geck/geckodriver.exe')

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.click()
    email_input.clear()
    email_input.send_keys("89531945840")
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()