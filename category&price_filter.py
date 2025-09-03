from selenium import webdriver
from selenium.webdriver import ActionChains
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


# category  work
category = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="block-163221535239da03ba-0"]/div/div[2]/h3/a'))
)
category.click()

# Wait for all checkbox labels to appear
checkbox_labels = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[@name='filter.v.availability']/following-sibling::label"))
)

print(f"Number of checkboxes found: {len(checkbox_labels)}")

# Click all labels to select checkboxes
for label in checkbox_labels:
    try:
        label.click()
    except:
        print("Label not clickable:", label)





# price filter Wait for sliders
min_slider = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.filter__price_min"))
)
max_slider = driver.find_element(By.CSS_SELECTOR, "input.filter__price_max")

# Create ActionChains object
actions = ActionChains(driver)

# Move min slider (to right, increase value)
actions.click_and_hold(min_slider).move_by_offset(50, 0).release().perform()

# Move max slider (to left, decrease value)
actions.click_and_hold(max_slider).move_by_offset(-50, 0).release().perform()

# Click Apply Button
apply_button = driver.find_element(By.ID, "filter__price--apply")
driver.execute_script("arguments[0].click();", apply_button)



time.sleep(8)
driver.quit()
