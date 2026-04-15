from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Open portal
    driver.get("https://one.openemr.io/openemr/portal/index.php")
    driver.maximize_window()
    time.sleep(3)

    print("Opened Portal")

    # Login (use real credentials if available)
    driver.find_element(By.NAME, "authUser").send_keys("your_username")
    driver.find_element(By.NAME, "clearPass").send_keys("your_password")
    driver.find_element(By.NAME, "login_email").send_keys("your_email@example.com")
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(5)

    # TC05 - Appointment navigation test
    try:
        driver.find_element(By.XPATH, "//*[contains(text(),'Appointment')]").click()
        time.sleep(5)

        print("TC05: Appointment page opened - PASS")

        # ✅ Screenshot for PASS
        driver.save_screenshot(r"C:\Users\Niraj\Desktop\appointment_PASS.png")
        print("Screenshot saved: appointment_PASS.png")

    except:
        print("TC05: Appointment navigation failed - FAIL")

        # ✅ Screenshot for FAIL
        driver.save_screenshot(r"C:\Users\Niraj\Desktop\appointment_FAIL.png")
        print("Screenshot saved: appointment_FAIL.png")

finally:
    driver.quit()

input("Press Enter to exit...")