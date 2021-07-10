from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("https://www.youtube.com/")
chrome_driver.find_element_by_id("search").send_keys("tomorrowland 2015 aftermovie")
sleep(3)
chrome_driver.find_element_by_id("search-icon-legacy").click()
sleep(3)
chrome_driver.close()
