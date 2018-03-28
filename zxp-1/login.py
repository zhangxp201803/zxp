import time
from selenium  import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("zhangxp")
driver.find_element_by_id("password").send_keys("zhangxp123")
driver.find_element_by_class_name("login_btn").click()

# driver = webdriver.Chrome()
# driver.get("http://localhost/")
# driver.find_element_by_link_text("登录").click()  #点击登录，打开的是一新窗口

#所有窗口集合
# all_windows = driver.window_handles
# print(all_windows)
# print(all_windows[0])
# current_window = driver.current_window_handle
# print(current_window)
#窗口切换
# driver.switch_to.window(all_windows[1])
# for item in all_windows:
#     if item != current_window:
#         driver.switch_to.window(item)

#在页面标签中，target="_blank"为打开一个新标签页，target="_self"为在原窗口打开
#selenium没有办法删除target,但是可以用javascript实现，在点击“登录”操作之前去掉target属性，则不会再打开新标签页
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')

# time.sleep(3)  只能选择一个固定的时间的等待
# driver.implicitly_wait(3)  比较智能，可以在一个时间范围内智能等待
# driver.quit()

