from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("zhangxp")
driver.find_element_by_id("password").send_keys("zhangxp123")
driver.find_element_by_class_name("login_btn").click()
# driver.find_element_by_id("password").submit()