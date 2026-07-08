# launch the browser
#open url
# find element by id/class
#perform action (click/type)
# verify result
# close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_web_interaction():
    driver = webdriver.Chrome()
    driver.fullscreen_window()

    try:
        driver.get("https://www.careers-page.com/tanacareers")

        time.sleep(5)

        # Tana Fellowship Program (Technical Roles)

        # REady to go
        ready = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jobs-banner-img"]/a/button'))
        )
        ready.click()
        time.sleep(4)


        #  click on the appy button 
        click_apply = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[5]/ul/li[4]/a/button'))
        )
        click_apply.click()
        time.sleep(4)

         #  click on the appy button 
        apply_position = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[1]/a/button'))
        )
        apply_position.click()
        time.sleep(4)





    finally:
        input("Press Enter to close the browser...")
        driver.quit()


test_web_interaction()
