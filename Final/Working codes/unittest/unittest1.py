import unittest
from selenium import webdriver
class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://magento-demo.lexiconn.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("denim")
        self.search_field.submit()
        # get all the anchor elements which have product names
        # #displayed currently on result page using # find_elements_by_xpathmethod
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))
        print(len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)