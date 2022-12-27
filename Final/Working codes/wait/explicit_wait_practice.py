#Site : http://magento-demo.lexiconn.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# initiate chrome browser and navigate to URL
driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com/")
driver.maximize_window()

# check numbewr of web elements matching img tag
img=driver.find_elements(By.XPATH,"//img")
print(len(img))

#Loop with all elements and print 'alt' and src properties
for item in img:
   print(item.get_property("alt"))
   print(item.get_property("src"))

# click action
driver.find_element(By.XPATH,"//img[@alt='Physical & Virtual Gift Cards']").click()

#back action on a driver(browser)
driver.back()

#wait with time
import time
time.sleep(2)

#Printing the title
print(driver.title)

#working on drop down
language=Select(driver.find_element(By.XPATH,"//select[@title='Your Language']"))
print(language)
for item in language.options:
    print(item.text)

#Select drop down based on index
#language.select_by_index(1)

#save _screenshot
driver.save_screenshot("Screenshots/French.png")

#select drop down values with visible text
#language.select_by_visible_text("German")

#implicit wait
driver.implicitly_wait(3)

#Explicit wait - Expected conditions with presence of element
element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//select[@title='Your Language']")))
print(element)

#Explicit Wait - Excpected conditions with Visibility of element
language.select_by_index(1)
element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(By.XPATH,"//select[@title='Votre Langue']")))
print(element.get_property("id"))

print("Code successfully executed")
driver.close()