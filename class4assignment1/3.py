from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
ff_driver = webdriver.Firefox(executable_path="/Users/daskarian/Documents/geckodriver")
chrome_driver.get("https://www.google.com/")
ff_driver.get("https://www.google.com/")

chrome_element = chrome_driver.find_element_by_class_name("gNO89b")
ff_element = ff_driver.find_element_by_class_name("gNO89b")

sleep(3)

chrome_driver.close()
ff_driver.close()
# As you can see we are accessing the same element using the same locator
# It doesn't matter which browser we are using
