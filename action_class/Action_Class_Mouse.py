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

#Click Operation
act.click(driver.find_element(By.LINK_TEXT,"ACCOUNT")).perform()
#act.click(driver.find_element(By.LINK_TEXT,"Checkout")).perform()
driver.find_element(By.LINK_TEXT,"Checkout").click()

#Double click on a element
act.double_click(driver.find_element(By.LINK_TEXT,"ACCESSORIES").click())

# Hover on a web element
act.move_to_element(driver.find_element(By.LINK_TEXT,"ACCESSORIES")).perform()
driver.find_element(By.LINK_TEXT,"Eyewear").click()

