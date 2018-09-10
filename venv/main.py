import time
import re
import getpass
import sys, pynput, os
import keyboard
import msvcrt

from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

__author__ = "Chawi_i cod3r"

TIME_OUT=1.0
SCROLL_PAUSE_TIME=0.5

def press_follow(driver):
    follow_button = driver.find_elements(By.CSS_SELECTOR, "button.oW_lN")[0];
    time.sleep(TIME_OUT)
    follow_button.click()
    pass

def press_like(driver):
    like_button = driver.find_elements(By.CSS_SELECTOR, "button.coreSpriteHeartOpen")[0];
    time.sleep(TIME_OUT)
    like_button.click()
    pass

def scroll_to_end_page():
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    pass

if __name__ == "__main__":

    # Enter password and email
    email = input("Email: ")
    password = getpass.getpass()
    instagram_tag = input("Instagram hashtag: ")

    j=40;
    while j>0:

        if j % 4 == 0:
            print("| Connecting ", end="\r", flush=True)
        elif j % 4 == 3:
            print("/ Connecting .", end="\r", flush=True)
        elif j % 4 == 2:
            print("- Connecting ..", end="\r", flush=True)
        elif j % 4 == 1:
            print("\ Connecting ...", end="\r", flush=True)

        time.sleep(0.1)
        print(20*" ", end="\r")
        j-=1

    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    driver.get("https://www.instagram.com")
    facebook_button = driver.find_elements(By.TAG_NAME, "button")[0];
    time.sleep(TIME_OUT)
    facebook_button.click()
    email_input = driver.find_element_by_id("email")
    password_input = driver.find_element_by_id("pass")
    email_input.clear()
    password_input.clear()
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(TIME_OUT*5)

    #search for tags
    search_input = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")[0];
    search_input.send_keys(instagram_tag)

    time.sleep(TIME_OUT*2)

    search_input.send_keys(Keys.RETURN)
    search_input.send_keys(Keys.RETURN)

    time.sleep(TIME_OUT*10)
    scroll_to_end_page()
    time.sleep(TIME_OUT*5)
    a_referances = driver.find_elements_by_tag_name("a")
    time.sleep(TIME_OUT*2)
    i=0
    post_pattern = r'.*/p/.*'

    while True:
        try:
            link = a_referances[i].get_attribute("href")
        except:
            raise ConnectionError("Page exception")
        if re.match(post_pattern, link):
            # Start new tab
            driver.execute_script("window.open('');")
            time.sleep(TIME_OUT)

            # Go to the new tab
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(TIME_OUT)
            driver.get(link)
            # To do here
            press_like(driver)
            time.sleep(TIME_OUT)
            press_follow(driver)
            time.sleep(TIME_OUT)
            driver.close()

            # Return to the first tab
            driver.switch_to_window(driver.window_handles[0])
        else:
            pass
        time.sleep(TIME_OUT)
        i+=1