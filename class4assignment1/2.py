from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("http://www.walla.co.il")
website_title = chrome_driver.title
print(f"The title found is {website_title}")
chrome_driver.refresh()
if website_title == chrome_driver.title:
    print("Website title and name are the same after refresh")
else:
    print("Website title and name are different after refresh")
sleep(3)
chrome_driver.close()
