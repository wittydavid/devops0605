import getpass
from selenium import webdriver
from time import sleep

print("Let me help you log on Facebook :)")
fb_email = input("Email: ")
fb_password = getpass.getpass()
chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("https://www.facebook.com/")
chrome_driver.find_element_by_id("email").send_keys(fb_email)
sleep(1)
chrome_driver.find_element_by_id("pass").send_keys(fb_password)
sleep(1)
chrome_driver.find_element_by_name("login").click()
sleep(3)
chrome_driver.close()
