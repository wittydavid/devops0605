from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("https://translate.google.com/")
# 1. Class locator
translate_text_field = chrome_driver.find_element_by_class_name("er8xn")
translate_text_field.send_keys("Class locator")
print(f"Class locator WebElement {translate_text_field}")

sleep(4)
translate_text_field.clear()

# 2. XPath locator
translate_text_field = chrome_driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
translate_text_field.send_keys("using Relative Xpath")
print(f"XPath locator WebElement {translate_text_field}")
sleep(4)
translate_text_field.clear()

# 3. Tag name locator
translate_text_field = chrome_driver.find_element_by_tag_name("textarea")
translate_text_field.send_keys("using Tag name locator")
print(f"XPath Tag name locator WebElement {translate_text_field}")
sleep(4)

chrome_driver.close()
