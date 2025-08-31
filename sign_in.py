

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
service = Service(r"F:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#open site
driver.get("https://dorjibari.com.bd")
driver.maximize_window()

# Wait until menu is visible (use a stable locator, not li[10])
wait = WebDriverWait(driver, 10)

# click sign in
sign_in = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="shopify-section-sections--17031397605559__header-classic"]/header/div/div/div[3]/div/div/a[1]'))  # replace with actual checkbox id
)
sign_in.click()

# set email
email = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="customer_email"]'))
)
email.send_keys("hacelepula@mailinator.com")

# set password
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME,'customer[password]'))
)
password.send_keys("123456")


#submit the form
submit = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="halo-auth-sidebar"]/div[2]/form/div[3]/input'))
)
submit.click()



time.sleep(8)
driver.quit()

