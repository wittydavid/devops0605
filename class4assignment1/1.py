from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
ff_driver = webdriver.Firefox(executable_path="/Users/daskarian/Documents/geckodriver")

chrome_driver.get("http://www.walla.co.il")
sleep(3)
chrome_driver.close()
ff_driver.get("http://www.ynet.co.il")
sleep(3)
ff_driver.close()
