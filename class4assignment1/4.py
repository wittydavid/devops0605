from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("https://translate.google.com/")
chrome_driver.find_element_by_class_name("er8xn").send_keys("שלום עולם, זה כל כך מגניב!")
sleep(5)
chrome_driver.close()
