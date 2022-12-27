"""
Practice 1:
Topics covered : Xpath, Dropdown selection, Asserts Usage

Test case:
0) Verify the Account link text
Hint: Use assert to verify the text of Account link on right side of the page

1) Find the drop down list for language selection

2) Verify if the language drop down has expected values - English,French,German
Hint : Use Asserts to verify the language options

3) Validate the default selected language after opening site.Default site language is 'English'
Hint: Use Asserts and Check if the default selected option in drop down is English

4) Select French language from drop down
Hint : Use "select by Index" and select French option

5) verify the page url
Hint: Page url should contain 'store=french' after selecting the french in drop down. Use Assert to verify the content

"""
#Site : http://magento-demo.lexiconn.com/
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# initiate chrome browser and navigate to URL
driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com/")
driver.maximize_window()


#Assertions

#Step 0
account_links=driver.find_element(By.LINK_TEXT,"ACCOUNT")
print(account_links.text)
assert account_links.text=='ACCOUNT',"The account link text is not matching"

def language_options(driver):
    #exec_options=['ENGLISH','FRENCH','GERMAN']
    exec_options=['English','French','German']
    act_options=[]

    #Printing the expected list
    print(exec_options)

    #Step 1
    language = Select(driver.find_element(By.XPATH, "//select[@title='Your Language']"))
    time.sleep(2)
    #print(language)

    #Step 2
    for item in language.options:
        act_options.append(item.text)
    print(act_options)
    assert exec_options==act_options, "Values are not match ...as per the expected list"

    #Step 3
    default_selection=language.first_selected_option.text

    #assert if the langue is equal to english
    assert default_selection =='English'
    print("default selection is English")

    #assert if the language is present in expected list
    assert default_selection in exec_options

    time.sleep(2)
    #Step 4
    language.select_by_index(1)

    # Step 5
    print(driver.current_url)
    assert 'store=french' in driver.current_url
    print("pass")

language_options(driver=driver)

