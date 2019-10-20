from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as py

driver = webdriver.Chrome("C:\\Users\\Viresh Uberoy\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com")

search = driver.find_element_by_id('search')
search.send_keys("hello" + Keys.RETURN)
py.click(x=300, y=500)
