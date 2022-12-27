"""

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.refresh()
driver.find_element_by_link_text("Click Here").click()

#prints the window handle in focus
main_window=driver.current_window_handle

print(driver.window_handles)
#to fetch the first child window handle
chwnd = driver.window_handles[1]
#to switch focus the first child window handle
driver.switch_to.window(chwnd)
print(driver.title)
driver.close()
driver.switch_to.window(main_window)
print(driver.title)

"""
#Program -2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.refresh()

driver.find_element_by_link_text("Click Here").click()
driver.find_element_by_link_text("Elemental Selenium").click()

#prints the window handle in focus
print(driver.current_window_handle)


#chwnd = driver.window_handles[1]
#to switch focus the first child window handle
#driver.switch_to.window(chwnd)
#print(driver.title)

for item in driver.window_handles:
    driver.switch_to.window(item)
    print(driver.title)
    if "Elemental Selenium" in driver.title:
        driver.find_element(By.LINK_TEXT,"Sauce Labs")





