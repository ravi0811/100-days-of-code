import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


username= os.getenv("USERNAME")
password= os.getenv("PASSWORD")
web_url= os.getenv("WEB_URL")
SIMILAR_ACCOUNT = "chefsteps"
base_url= os.getenv("BASE_URL")  
class InstaFollower:

    def __init__(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.driver=webdriver.Chrome(options=chrome_options)
        self.wait=WebDriverWait(self.driver,10)

    def login(self):

        decline = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Decline')]")
        if decline:
            decline[0].click()


        self.driver.get(web_url)
        time.sleep(2)
        username_box= self.driver.find_element(By.XPATH,'/html/body/div/aside/div/form/input[1]')
        username_box.send_keys(username)

        password_box= self.driver.find_element(By.XPATH,'/html/body/div/aside/div/form/input[2]')
        password_box.send_keys(password)

        login_btn= self.driver.find_element(By.XPATH,'/html/body/div/aside/div/form/button')
        login_btn.click()

        save_info_btn= self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="popup-save-login"]/div/div[2]')))
        save_info_btn.click()
        time.sleep(1)
        notification_btn= self.wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="popup-notifications"]/div/button[2]')))
        notification_btn.click()
        


    def find_follower(self):
        self.driver.get(f"{base_url}/u/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)

        modal= self.driver.find_element(By.CSS_SELECTOR,".followers-scroll")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        follow_list= self.driver.find_elements(By.CSS_SELECTOR,'.followers-scroll button')
        for i in range(len(follow_list)):
            if follow_list[i].text == "Follow":
                follow_list[i].click()
            time.sleep(1)

        # or
        '''all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()'''
bot= InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
