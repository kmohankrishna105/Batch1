import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestDraggable():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Documents\\E2E_POM\\Driver\\chromedriver.exe")

    def teardown_method(self, method):
        #self.driver.quit()
        pass

    def test_draggable(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        time.sleep(3)

        # Identify the tab for switching (Photo manager tab - driver focus needs to be changed)
        img_icon="//*[@data-src = '../../demoSite/practice/droppable/photo-manager.html']"
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,img_icon))
        time.sleep(3)

        #identify the element for dragging
        element = self.driver.find_element(By.XPATH, "//*[@alt='The peaks of High Tatras']")

        # identify the element for dropping location
        target=self.driver.find_element(By.XPATH, "//*[@id='trash']")

        #Actions class to drag and drop the items
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().move_to_element(target).release().perform()
        time.sleep(2)

        self.driver.switch_to.default_content()