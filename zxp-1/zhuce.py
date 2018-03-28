from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
# driver.execute_script("document.getElementsByClassName('site-nav-right fr')[0].childNodes[3].click()")
driver.implicitly_wait(3)
driver.find_element_by_name("username").send_keys("zxp123456")
driver.find_element_by_name("password").send_keys("zxp123456")
driver.find_element_by_name("userpassword2").send_keys("zxp123456")
driver.find_element_by_name("mobile_phone").send_keys("13220181234")
driver.find_element_by_name("email").send_keys("zxp123456@163.com")
driver.find_element_by_class_name("reg_btn").click()





