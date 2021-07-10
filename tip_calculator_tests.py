from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="/Users/daskarian/Documents/chromedriver")
# my_driver.get("https://github.com")
# sleep(5)
# my_driver.refresh()
# sleep(5)

# FULL Xpath /html/body/div/div[1]/form/p[4]/select/option[3]
# Relative Xpath //*[@id="serviceQual"]/option[3]

my_driver.get("file:///Users/daskarian/devopsCourse/devops0605/tip_calc/index.html")
billamt = my_driver.find_element_by_id("billamt")
billamt.send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("music").send_keys("4")
my_driver.find_element_by_id("calculate").click()

actual = my_driver.find_element_by_id("tip").text
expected = "4.01"
print(actual)
if float(expected) == float(actual):
    print("SAME")
else:
    print("DIFF")

# this a good way to write python testings
assert actual == expected
# my_driver.close()
