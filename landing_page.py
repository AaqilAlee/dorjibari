
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time

# Setup
service = Service(r"F:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#open site
driver.get("https://dorjibari.com.bd/")
driver.maximize_window()

# Wait until menu is visible (use a stable locator, not li[10])
wait = WebDriverWait(driver, 10)

# Check if title contains Dorjibari
assert "Dorjibari" in driver.title

# Or check if logo is present
logo = driver.find_element(By.XPATH, "//img[@alt='Dorjibari']")
assert logo.is_displayed()

time.sleep(8)
driver.quit()

