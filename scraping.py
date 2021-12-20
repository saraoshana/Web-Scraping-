from  selenium import webdriver

from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("link for the website goes here")

"""try to find element by id first because it is unique,
if not found, try name, if not found, try class name """
search = driver.find_element_by_name("s")
