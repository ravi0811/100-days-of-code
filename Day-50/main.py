import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException
from time import sleep

# -------------------Credentials----------------------
email= os.getenv("EMAIL")
password= os.getenv("PASSWORD")
tindog= os.getenv("TINDOG")
# -----------------------------------------------------

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(tindog)
main_window= driver.current_window_handle

wait=WebDriverWait(driver,10)


# -----------------------------Login Module-------------------------------------------
login_btn= driver.find_element(By.CSS_SELECTOR,value=".tindog-nav button")
login_btn.click()

facebark_btn= wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="login-modal"]/div/div/div/button[1]')))
facebark_btn.click()
wait.until(lambda d: len(d.window_handles)>1)
# ---switch the main focus to the pop up----
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

email_box= driver.find_element(By.XPATH,'//*[@id="email"]')
email_box.send_keys(email)
password_box= driver.find_element(By.XPATH,'//*[@id="pass"]')
password_box.send_keys(password)
final_login_btn= driver.find_element(By.XPATH,'/html/body/div[2]/div/form/button')
final_login_btn.click()
# ---------------------------------------------------------------------------------------------
driver.switch_to.window(main_window)
location_allow= wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button')))
location_allow.click()

sleep(1)

notification_btn= wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button[2]')))
notification_btn.click()

sleep(1)

cookie_btn= wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/main/div/div/form/button')))
cookie_btn.click()

for num in range(50):
    sleep(1)
    try:
        like_btn= wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#like-button-container .btn-like')))
        driver.execute_script("arguments[0].scrollIntoView(true);",like_btn)
        sleep(1)
        like_btn.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR,value='.match-popup-link a').click()
        except NoSuchElementException:
            sleep(1)
    except NoSuchElementException:
        sleep(1)

    print(num+1)
    