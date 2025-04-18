from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import os

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.intervue.io")
print("Browser launched. Please manually perform the login...")

try:
    while True:
        time.sleep(2)
        try:
            error = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid')]")
            print("⚠️ Login failed. Taking screenshot...")
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot("screenshots/login_failed.png")
            break
        except NoSuchElementException:
            pass
except KeyboardInterrupt:
    print("Script stopped manually.")
