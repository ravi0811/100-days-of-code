from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

ACCOUNT_EMAIL= "ravi@test.com"
ACCOUNT_PASSWORD="anything"
GYM_URL="https://appbrewery.github.io/gym/"

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


user_data_dir= os.path.join(os.getcwd(),"chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")
driver.implicitly_wait(10)

join_button= driver.find_element(By.XPATH,value='//*[@id="home-page"]/section[1]/div/div/a[1]/button')
join_button.click()

email_input= driver.find_element(By.ID,"email-input")
email_input.send_keys(ACCOUNT_EMAIL)

password_input= driver.find_element(By.ID,value="password-input")
password_input.send_keys(ACCOUNT_PASSWORD)

submit_btn= driver.find_element(By.ID,"submit-button")
submit_btn.click()

class_card= driver.find_elements(By.CSS_SELECTOR, value="div[id^=class-card-]")
for card in class_card:
    day_group= card.find_element(By.XPATH,value="./ancestor::div[contains(@id,'day-group-')]")
    day_title= day_group.find_element(By.TAG_NAME,value="h2").text

    if "Tue" in day_title:
        time_text= card.find_element(By.CSS_SELECTOR,value="p[id^=class-time]").text
        if "6:00 PM" in time_text:
            class_name=card.find_element(By.CSS_SELECTOR,value="h3[id^=class-name-]").text
            book_btn= card.find_element(By.CSS_SELECTOR,value="button[id^=book-button-]")
            book_btn.click()

            print(f"✅{class_name} booked on {day_title}")

driver.quit()
