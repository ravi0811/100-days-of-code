from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

targetUrl= "https://appbrewery.github.io/Zillow-Clone/"

response= requests.get(targetUrl)

zillow= response.text

soup= BeautifulSoup(zillow,"html.parser")

rate= soup.findAll(name="span",class_="PropertyCardWrapper__StyledPriceLine")
rate_list=[item.getText() for item in rate]
clean_ratelist= [item.split("+")[0] for item in rate_list]


address= soup.findAll(name="address")
address_list= [item.getText(strip=True) for item in address]


property_link=soup.findAll(name="a",class_="property-card-link")
property_link_list= [item.get("href") for item in property_link]
print(property_link_list)

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)


for n in range(len(property_link_list)):
    driver.get(os.getenv("LINK"))
    time.sleep(2)
    address= driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price= driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link= driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit= driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address.send_keys(address_list[n])
    price.send_keys(clean_ratelist[n])
    link.send_keys(property_link_list[n])
    submit.click()
