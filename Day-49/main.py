from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time


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

def retry(func,retries=5,description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i+1}")
        try:
            result=func()
            return result
        except Exception as e:
            if i== retries-1:
                raise
            print(f"Attempt {i+1} failed due to {type(e).__name__}, retrying...")
            time.sleep(1)

wait= WebDriverWait(driver,2)

def login():
    driver.get("https://appbrewery.github.io/gym/")

    join_button= driver.find_element(By.XPATH,value='//*[@id="home-page"]/section[1]/div/div/a[1]/button')
    join_button.click()

    email_input= driver.find_element(By.ID,"email-input")
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input= driver.find_element(By.ID,value="password-input")
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn= driver.find_element(By.ID,"submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

retry(login,description="Login Process")
def book_classes():
    class_card= driver.find_elements(By.CSS_SELECTOR, value="div[id^=class-card-]")

    booked_count=0
    waitlist_count=0
    already_booked_count=0

    processed_classes=[]
    for card in class_card:
        day_group= card.find_element(By.XPATH,value="./ancestor::div[contains(@id,'day-group-')]")
        day_title= day_group.find_element(By.TAG_NAME,value="h2").text

        if "Mon" in day_title or "Thu" in day_title:
            time_text= card.find_element(By.CSS_SELECTOR,value="p[id^=class-time]").text
            if "6:00 PM" in time_text:
                class_name=card.find_element(By.CSS_SELECTOR,value="h3[id^=class-name-]").text
                book_btn= card.find_element(By.CSS_SELECTOR,value="button[id^=book-button-]")

                class_info=f"{class_name} on {day_title}"
                if book_btn.text == "Book Class":
                    book_btn.click()
                    wait.until(lambda d:card.find_element(By.CSS_SELECTOR,value="button[id^=book-button-]").text=="Booked")
                    print(f"✅{class_name} booked on {day_title}")
                    booked_count+=1
                    time.sleep(0.5)
                    processed_classes.append(f"[New Booking] {class_info}")

                elif book_btn.text== "Booked":
                    print("Class already booked")
                    already_booked_count+=1
                    processed_classes.append(f"[Booked] {class_info}")


                elif book_btn.text=="Join Waitlist":
                    book_btn.click()
                    wait.until(lambda d: card.find_element(By.CSS_SELECTOR,value="button[id^=book-button-]").text == "Waitlisted")
                    print(f"✅{class_name} waitlisted on {day_title}")
                    waitlist_count+=1
                    time.sleep(0.5)
                    processed_classes.append(f"[New Waitlist] {class_info}")

                elif book_btn.text=="Waitlisted":
                    print("Already on the waiting list")
                    already_booked_count+=1
                    processed_classes.append(f"[Waitlisted] {class_info}")
    return True
retry(book_classes,description="Class Booking Process")

            
# print("\n---BOOKING SUMMARY---")
# print(f"Classes Booked: {booked_count}")
# print(f"Waitlist Joined: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Monday 6pm classes processed: {booked_count+waitlist_count+already_booked_count}")

# print("\n---DETAILED CLASS LIST---")
# for class_detail in processed_classes:
#     print(f"•{class_detail}")
def get_my_bookings():
    my_bookings_btn= driver.find_element(By.ID,value="my-bookings-link")
    my_bookings_btn.click()
    wait.until(ec.presence_of_element_located((By.ID,"my-bookings-page")))

    print("\n----Verifying on MY Booking Page")
    confirmed_booking= driver.find_elements(By.CSS_SELECTOR,value="#confirmed-bookings-section h3")
    if confirmed_booking:
        cbl= [item.text for item in confirmed_booking]
        print(f"All booked classes: {cbl}")
    else:
        print("Confimed Booking Element Not Found")

    waitlisted= driver.find_elements(By.CSS_SELECTOR,value="#waitlist-section h3")
    if waitlisted:
        wl=[item.text for item in waitlisted]
        print(f"Waitlisted: {wl}")
    else:
        print("Waitlisted Element Not Found")
    return True

retry(get_my_bookings,description="Retrieving My Bookings Page")

driver.quit()
