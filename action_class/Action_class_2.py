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

#Right Click
act.context_click(driver.find_element(By.LINK_TEXT,"SALE")).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
