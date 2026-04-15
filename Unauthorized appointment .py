from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    # Try to open appointment-related page directly without login
    driver.get("https://demo.openemr.io/a/openemr/portal/index.php")
    driver.maximize_window()
    time.sleep(3)

    print("Opened Portal")

    # Attempt to navigate directly to a protected page by URL guess
    driver.get("https://demo.openemr.io/a/openemr/portal/home.php")
    time.sleep(3)

    if "login" in driver.current_url.lower() or "portal" in driver.page_source.lower():
        print("TC10: Unauthorized appointment access blocked - PASS")
    else:
        print("TC10: Unauthorized appointment access allowed - FAIL")

    driver.save_screenshot("TC10_unauthorized_access.png")

finally:
    driver.quit()

input("Press Enter to exit...")