"""
Practice 2
Topics covered :
    Class implementation ,Constructor
    Calling a method with created instance

Please note that Practice:1 code is used for class implementation
Hint: Constructor is used to open the browser and navigate to url
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Option:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
        self.driver.get("http://magento-demo.lexiconn.com/")
        self.driver.maximize_window()

    def test_language_options(self):
        self.exec_options = ['ENGLISH', 'FRENCH', 'GERMAN']
        self.act_options = []
        # working on drop down
        self.language = Select(self.driver.find_element(By.XPATH, "//select[@title='Your Language']"))
        print(self.language)
        for item in self.language.options:
            self.act_options.append(item.text)
        # assert exec_options==act_options
        self.default_selectoion = self.language.first_selected_option.text
        assert self.default_selectoion == 'English'
        # assert default_selection in exec_options
        self.language.select_by_index(1)
        print(self.driver.current_url)
        assert 'store=french' in self.driver.current_url
        print("Success")

#class_obj=Option()
#class_obj.test_language_options()