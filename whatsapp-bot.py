from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from message import format
import time
import codecs

print("*** WhatsApp Bot started ***")
format()
driver = webdriver.Chrome()
print("Login to WhatsApp Web and press ENTER only once logged in.")
time.sleep(3)
whatsapp_url = "https://web.whatsapp.com"
driver.get(whatsapp_url)
input()
with open("numbers.txt", "r") as numbers:
    for number in numbers:
        number = number.strip()
        if len(number) < 11:
            print("Invalid Number")
        else:
            url = "https://web.whatsapp.com/send?phone=" + number
            driver.get(url)
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
            )
            # time.sleep(20)
            input_ = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            file = open("message_formatted.txt", "r", encoding="utf8")
            x = file.read()
            # x = codecs.decode(x, 'unicode_escape')
            for y in x.split(r'\n'):
                try:
                    input_.send_keys(y)
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                        Keys.ENTER).perform()
                except:
                    print("Message format Error")
                    quit()
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            print("Message sent to " + number)
            time.sleep(2)
