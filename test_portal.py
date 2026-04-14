from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://one.openemr.io/openemr/portal/index.php")
    driver.maximize_window()
    time.sleep(3)

    print("Opened Portal")

    # TC01
    if "Portal" in driver.page_source:
        print("TC01: Page Loaded - PASS")
    else:
        print("TC01: Page Loaded - FAIL")

    # TC02
    try:
        driver.find_element(By.NAME, "authUser")
        driver.find_element(By.NAME, "clearPass")
        driver.find_element(By.NAME, "login_email")
        print("TC02: Fields Present - PASS")
    except:
        print("TC02: Fields Missing - FAIL")

    # TC03
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(2)
    print("TC03: Empty login test executed")

    # Screenshot
    driver.save_screenshot("portal_test.png")

finally:
    driver.quit()