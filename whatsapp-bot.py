import functools
import codecs
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys          import Keys
from selenium.webdriver.common.by            import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC

from selenium import webdriver


open_file = functools.partial(open, encoding='utf8')

def format():
    message = open_file('message.txt', 'r').readlines()
    formatted = ''

    for i in range(len(message)):
        formatted += message[i].rstrip('\n') + " " + "\\n"

    with open_file("message_formatted.txt", "w") as final:
        final.writelines(formatted)

    print("Message formating complete")

print("*** WhatsApp Bot started ***")
format()

driver = webdriver.Firefox()

time.sleep(3)
driver.get("https://web.whatsapp.com")

with open("numbers.txt", "r") as numbers:
    for number in numbers:
        number = number.strip()
        if len(number) < 11:
            print("Invalid Number")
        else:
            driver.get("https://web.whatsapp.com/send?phone=" + number)
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                )
            )
            message_box = driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
            )
            for line in open_file(
                "message_formatted.txt",
                "r",
            ).read().split(r'\n'):
                try:
                    message_box.send_keys(line)
                    ActionChains(driver)  \
                    .key_down(Keys.SHIFT) \
                    .key_down(Keys.ENTER) \
                    .key_up(Keys.SHIFT)   \
                    .key_up(Keys.ENTER)   \
                    .perform()
                except:
                    print("Message format Error")
                    quit()
            driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[3]/button'
            ).click()
            print("Message sent to " + number)
            time.sleep(2)
