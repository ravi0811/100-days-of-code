import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

email= os.getenv("EMAIL")
password= os.getenv("PASSWORD")
y_link= os.getenv("Y_LINK")
promised_down="100"
promised_up="100"
speedTest="https://www.speedtest.net/"

class InternetTwitterSpeedBot:

    def __init__(self):
        self.up= 0
        self.down= 0

        

        chrome_options= webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.driver=webdriver.Chrome(options= chrome_options)
        self.wait=WebDriverWait(self.driver,10)
        
        


    def get_internet_speed(self):
        
        self.driver.get("https://www.speedtest.net/")
        go_btn= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        go_btn.click()


        time.sleep(45)
        self.down= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        self.up= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text
        

    def twitter_at_provider(self):
        message=f"Hey Interner Provider, why is my {self.down}down/{self.up}up\n when i pay for 150down/10up?"
        self.driver.get(y_link)
        time.sleep(2)

        email_input= self.driver.find_element(By.ID,"email")
        email_input.send_keys(email)
        password_input= self.driver.find_element(By.ID,"password")
        password_input.send_keys(password)

        login_btn= self.driver.find_element(By.XPATH,"/html/body/div/div/form/button")
        login_btn.click()
        
        time.sleep(3)

        tweet_box= self.driver.find_element(By.ID,"tweet-compose")
        tweet_box.send_keys(message)

        post_btn= self.driver.find_element(By.ID,"post-btn")
        post_btn.click()
        
        time.sleep(2)
        self.driver.quit()


bot= InternetTwitterSpeedBot()
bot.get_internet_speed()
bot.twitter_at_provider()



