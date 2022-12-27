import time

from selenium import webdriver
# create a new Firefox session
driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://magento-demo.lexiconn.com/")
# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()
# enter search keyword and submit
search_field.send_keys("denim")
search_field.submit()
time.sleep(2)
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")
# get the number of anchor elements found
print(f"Found  {str(len(products))}  products")
# iterate through each anchor element and print the text that is # name of the product
for product in products:
    print (product.text)
# close the browser window
driver.quit()
