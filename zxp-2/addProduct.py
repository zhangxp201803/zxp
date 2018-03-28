from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://localhost/admin.php")
driver.find_element_by_name("username").send_keys("admin")

#ActionChains类中封装了所有元素的高级操作方法，可以接多个方法，但必须以perform()结尾
#输入用户名后，按TAB键，输入密码，按TAB键，输入验证码，再按回车，.perform()
ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()