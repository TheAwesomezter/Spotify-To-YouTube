from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
import csv
import pyautogui as py

options = Options()
options.add_argument("user-data-dir=/tmp/Viresh Uberoy")

driver = webdriver.Chrome("C:\\Users\\Viresh Uberoy\\Downloads\\chromedriver_win32\\chromedriver.exe", options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 7)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

songs = []

with open("modified_list.csv") as file:
    fileLine = csv.reader(file)
    for value in fileLine:
        songs.append(value)

songs = [" ".join(song) for song in songs]

songs = [song.replace("(", "") for song in songs]
songs = [song.replace(")", "") for song in songs]
songs = [song.replace(" ", "+") for song in songs]

for song in songs:
    driver.get("https://www.youtube.com/results?search_query=" + str(song))
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    try:
        wait.until(visible((By.ID, "owner-sub-count")))
        # save_buttons = driver.find_elements_by_id("button")
        py.click(x=1300, y=970)
        wait.until(visible((By.ID, "label")))
        py.click(x=975, y=570)
    except:
        print(song)
        continue
