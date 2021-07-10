from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


def throw_error(err_msg):
    print(f"ERROR: {err_msg}")
    exit(1)


def get_clickable_element_if_exist_by_class(class_name):
    try:
        element = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
    except NoSuchElementException as e:
        print(e.args)
        chrome_driver.quit()
        throw_error("The element doesn't exist")
    except BaseException as e:
        print(e.args)
        chrome_driver.quit()
        throw_error("Finding an element has failed")
    return element


def get_clickable_element_if_exist_by_xpath(xpath_str):
    try:
        element = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_str))
        )
    except NoSuchElementException as e:
        print(e.args)
        chrome_driver.quit()
        throw_error("The element doesn't exist")
    except BaseException as e:
        print(e.args)
        chrome_driver.quit()
        throw_error("Finding an element has failed")
    return element


chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
chrome_driver.get("https://buyme.co.il/")

clickable_web_element = get_clickable_element_if_exist_by_class("seperator-link")
clickable_web_element.click()
print("Hello")

clickable_web_element2 = get_clickable_element_if_exist_by_xpath(
    "/html/body/div[3]/div/div[1]/div/div/div[3]/div[1]/span")
print(clickable_web_element2.text)
# clickable_web_element2.click()

# sleep(5)
# blabla = chrome_driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[3]/div[1]/span")
# print(blabla.text)
# clickable_web_element = get_clickable_element_if_exist_by_class("text-link theme")
# print(clickable_web_element.text)


# clickable_web_element.click()

# print(clickable_web_element)
# print(type(clickable_web_element))
# print(clickable_web_element.text)
