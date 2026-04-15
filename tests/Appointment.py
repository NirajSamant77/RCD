from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Open correct demo portal
    driver.get("https://demo.openemr.io/a/openemr/portal/index.php")
    driver.maximize_window()
    time.sleep(3)

    print("Opened Demo Portal")

    # Start screenshot
    driver.save_screenshot("appointment_start.png")
    print("Screenshot saved: appointment_start.png")

    # Find fields
    text_inputs = driver.find_elements(By.XPATH, "//input[@type='text' or @type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    login_button = driver.find_element(By.XPATH, "//button[contains(., 'Log In')] | //input[@type='submit']")

    if len(text_inputs) >= 2:
        username_input = text_inputs[0]
        email_input = text_inputs[1]
    else:
        raise Exception("Could not find username/email fields")

    # Demo credentials
    username_input.send_keys("Phil1")
    password_input.send_keys("phil")
    email_input.send_keys("heya@invalid.email.com")

    login_button.click()
    time.sleep(5)

    # Appointment test
    try:
        appointment_link = driver.find_element(
            By.XPATH,
            "//*[contains(text(),'Appointment') or contains(text(),'Appointments')]"
        )
        appointment_link.click()
        time.sleep(3)

        print("TC05: Appointment page opened - PASS")
        driver.save_screenshot("appointment_result.png")
        print("Screenshot saved: appointment_result.png")

    except:
        print("TC05: Appointment navigation failed - FAIL")
        driver.save_screenshot("appointment_fail.png")
        print("Screenshot saved: appointment_fail.png")

except Exception as e:
    print("Error:", e)
    driver.save_screenshot("error_screen.png")
    print("Screenshot saved: error_screen.png")

finally:
    driver.quit()

input("Press Enter to exit...")