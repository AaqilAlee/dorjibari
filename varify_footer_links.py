from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
service = Service(r"F:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open site
driver.get("https://dorjibari.com.bd/")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)

# check facebook link
facebook_page = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="shopify-section-sections--17031397540023__footer-1"]/footer/div[1]/div/div/div[4]/div/div/ul/li[1]/a'))
)
facebook_page.click()
time.sleep(5)
driver.back()

# check instagram link
instagram_page = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="shopify-section-sections--17031397540023__footer-1"]/footer/div[1]/div/div/div[4]/div/div/ul/li[2]/a'))
)
instagram_page.click()
time.sleep(5)
driver.back()

# check youtube link
instagram_page = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="shopify-section-sections--17031397540023__footer-1"]/footer/div[1]/div/div/div[4]/div/div/ul/li[3]/a'))
)
instagram_page.click()
time.sleep(5)
driver.back()

menu_items = ["About Us", "Blog", "Privacy Policy" , "Shipping Policy","Terms & Conditions"]

for item in menu_items:
    # Wait until menu item is clickable
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, item)))
    link.click()


    # Go back and wait for menu to reload
    driver.back()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, item)))





time.sleep(5)
driver.quit()

