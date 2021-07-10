from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeops
from selenium.webdriver.firefox.options import Options as ffops
from time import sleep

chrome_options = chromeops()
chrome_options.add_argument("--disable-extensions")
chrome_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver",
                                 options=chrome_options)
chrome_driver.get("https://www.google.com/")

ff_options = ffops()
ff_options.add_argument("--disable-extensions")
ff_driver = webdriver.Firefox(executable_path="/Users/daskarian/Documents/geckodriver",
                              options=ff_options)

ff_driver.get("https://www.google.com/")

sleep(10)
chrome_driver.close()
ff_driver.close()
