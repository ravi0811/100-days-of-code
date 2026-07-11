from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import time,sleep

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

go= False

while go == False:
    try:
        lang_btn= driver.find_element(By.ID,value="langSelect-EN")
        lang_btn.click()
        go= True
        
    except:
        print("No Lang element found")
        sleep(2)
        

game_on = True
sleep(3)
wait_time= 5
time_out= time()+wait_time
five_min= time()+ 60*5
bigCookie= driver.find_element(By.ID,value="bigCookie")


while game_on:
    bigCookie.click()
    if time()>time_out:
        try:
            products= driver.find_elements(By.CSS_SELECTOR,value="#products .product.enabled")
            
            if products:
            
                best_buy= products[-1]
                best_buy.click()
                
        except:
            print("Error")
            

        time_out=time()+ wait_time


    if time()> five_min:
        driver.quit()
        game_on= False