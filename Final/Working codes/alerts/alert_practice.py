import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

#browser exposes an executable file

#Through Selenium test we will invoke the executable file which will then #invoke actual browser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://demoqa.com/alerts")
#to refresh the browser
driver.refresh()
#click on submit button

driver.find_element(By.XPATH,"(//*[text()='Click me'])[1]").click()
a1=Alert(driver)
time.sleep(3)
a1.accept()
print("alert accepted")


driver.find_element(By.XPATH,"(//*[text()='Click me'])[2]").click()
a2=Alert(driver)
time.sleep(6)
a2.accept()
print("alert accepted")

driver.find_element(By.XPATH,"(//*[text()='Click me'])[3]").click()
a3=Alert(driver)
time.sleep(3)
a3.dismiss()
print("alert dismissed")

driver.find_element(By.XPATH,"(//*[text()='Click me'])[4]").click()
a4=Alert(driver)
time.sleep(3)
print(a4.text)

a4.send_keys("THis is enetered in alert text box")
time.sleep(3)
a4.accept()
print("alert accepted")