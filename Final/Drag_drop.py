import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
"""
Drag and drop 

In the previous Drag.py, we are dragging and dropping items.

Here in this code, we shall count the number of items in trash to validate if the count is increased by 1 after we drop the new item in the trash can

"""

class TestDraggable():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Documents\\E2E_POM\\Driver\\chromedriver.exe")

    def teardown_method(self, method):
        #self.driver.quit()
        pass

    def test_draggable(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        print(self.driver.title)
        time.sleep(3)
        assert self.driver.title == "Drag and Drop Demo Sites | Testing Site - GlobalSQA"
        time.sleep(3)

        # Identify the tab for switching (Photo manager tab)
        img_icon="//*[@data-src = '../../demoSite/practice/droppable/photo-manager.html']"
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,img_icon))

        time.sleep(3)

        #identify the element for dragging
        element = self.driver.find_element(By.XPATH, "//*[@alt='The peaks of High Tatras']")

        # identify the element for dropping location
        target=self.driver.find_element(By.XPATH, "//*[@id='trash']")

        #validate the number of items present in trash location
        no_of_items="//*[@id='trash']//li"

        #provide the trash count or return the number of items as zero if no location found
        try:
            item=self.driver.find_elements(By.XPATH, no_of_items)
            print(len(item))
        except:
            print("Zero Items")

        #Actions class to drag and drop the items
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().move_to_element(target).release().perform()
        time.sleep(2)

        # provide the trash count or return the number of items as zero if no location found
        try:
            item=self.driver.find_elements(By.XPATH, no_of_items)
            print(len(item))
            print(item.__len__())
        except:
            print("Zero Items")
        self.driver.switch_to.default_content()