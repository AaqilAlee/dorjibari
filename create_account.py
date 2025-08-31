

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
driver.get("https://dorjibari.com.bd/account/register")
driver.maximize_window()

# Wait until menu is visible (use a stable locator, not li[10])
wait = WebDriverWait(driver, 10)

# set username
username = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID,'RegisterForm-FirstName'))
)
username.send_keys("Chelsea")

# set lastname
lastname = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID,'RegisterForm-LastName'))
)
lastname.send_keys("Holder")

# set email
email = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID,'RegisterForm-email'))
)
email.send_keys("hacelepula@mailinator.com")

# set password
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID,'RegisterForm-password'))
)
password.send_keys("123456")

checkbox = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="create_customer"]/div[5]/label'))  # replace with actual checkbox id
)
checkbox.click()


#submit the form
submit = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="create_customer"]/div[6]/input'))
)
submit.click()



time.sleep(8)
driver.quit()

