from selenium import webdriver
from time import sleep


def print_cookies():
    cookies = chrome_driver.get_cookies()
    for cookie in cookies:
        print(cookie)


chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
website_test = "https://www.wework.com/"
chrome_driver.get(website_test)
print(f"PRE delete - Here are the cookies that we have for {website_test}")
print_cookies()
print("We will no delete all cookies")
chrome_driver.delete_all_cookies()
print(f"POST delete - Here are the cookies that we have for {website_test}")
print_cookies()
chrome_driver.close()
