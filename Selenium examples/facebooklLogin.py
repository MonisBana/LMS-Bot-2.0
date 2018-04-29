from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("")#Enter your Email
passElem =driver.find_element_by_name("pass")
passElem.clear()
passElem.send_keys("")#Enter your password
elem.send_keys(Keys.RETURN)
