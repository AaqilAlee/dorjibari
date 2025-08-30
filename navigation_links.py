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

menu_items = ["SUMMER COLLECTION 2025", "MEN TOP", "MEN BOTTOM" , "OUTERWARE","FRAGRANCE 30% OFF",
              "ACCESSORIES", "BIG SAVING","Contact Us"]

for item in menu_items:
    # Wait until menu item is clickable
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, item)))
    link.click()


    # Go back and wait for menu to reload
    driver.back()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, item)))

time.sleep(5)
driver.quit()

