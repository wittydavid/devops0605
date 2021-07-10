from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
website_test = "https://github.com/"
chrome_driver.get(website_test)
# Option 1
# chrome_driver.find_element_by_name("q").send_keys("Selenium\n")
# Option 2
chrome_driver.find_element_by_name("q").send_keys("Selenium")
chrome_driver.find_element_by_name("q").submit()
sleep(4)
chrome_driver.close()
