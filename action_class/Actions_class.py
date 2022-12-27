"""

Actions Class (Action Chains)
Keyboard Operations
    Ex: Tab,Ctrl + A (keyboard operations)

Mouse operations
    Right click,double click,Mouse Hover

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com/customer/account/create/")
driver.maximize_window()

driver.find_element(By.ID,"firstname").send_keys("First Name")
act=ActionChains(driver)
act.send_keys(Keys.TAB).perform()


act.send_keys("Last Name")
time.sleep(2)

act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(2)
print("Hi")
act.key_down(Keys.CONTROL).send_keys('c').perform()
time.sleep(2)
act.send_keys(Keys.RIGHT).perform()
time.sleep(6)
act.send_keys(Keys.TAB).perform()
driver.save_screenshot("max.png")
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys('v').perform()
