"""
Author: Enoc Mena

Description: This is a ps5 bot that checks if BestBuy has any ps5's in stock by checking a
specific URL. If there are ps5's in stock the computer will make a beeping sound.

Notes: Start chromedriver in Terminal before starting this bot.
Make sure you are logged into your BestBuy account as this bot works better if you are
logged into your BestBuy account.

"""

import time
import info
from beepy import beep
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
chromedriver_path = "your path here"
c_driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)
c_driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

#c_driver.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
#c_driver.get('https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728')
c_driver.get('https://www.bestbuy.com/site/marvels-spider-man-miles-morales-standard-launch-edition-playstation-5/6430146.p?skuId=6430146')

#check until ps5 in stock
while True:
    try:
        c_driver.find_element_by_xpath('//button[normalize-space()="Add to Cart"]').click()
        if True:
            beep(sound="ping") #beeps if ps5 is in stock
            break
    except NoSuchElementException:
        c_driver.refresh()

c_driver.get('https://www.bestbuy.com/cart')
c_driver.find_element_by_xpath('//button[normalize-space()="Checkout"]').click()

time.sleep(3)

#xpaths
first_login = ''
login = '/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[3]/button'
email = '//*[@id="fld-e"]'
password = '//*[@id="fld-p1"]'

time.sleep(3)

#login info
c_driver.find_element_by_xpath(email).send_keys("email here")
c_driver.find_element_by_xpath(password).send_keys("password here")
c_driver.find_element_by_xpath(login).click()

time.sleep(2)

#continue to payment info
payment = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span'
c_driver.find_element_by_xpath(payment).click()

time.sleep(2)

continuetopay_button = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'
c_driver.find_element_by_xpath(continuetopay_button).click()

time.sleep(2)

#fill in card cvv
cvvField = WebDriverWait(c_driver, 10).until(
    EC.presence_of_element_located((By.ID, "cvv"))
)
cvvField.send_keys(info.cvv)

place_order = '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/div[2]/button'
c_driver.find_element_by_xpath(place_order).click()
