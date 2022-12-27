import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def test_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/")
    #driver.maximize_window()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 100);")

def test_second_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("https://www.youtube.com/watch?v=OsLCY3vz3t8&list=RDOsLCY3vz3t8&start_radio=1")
    driver.maximize_window()
    time.sleep(2)

@pytest.mark.skip(reason='No execution required in UAT env')
def test_third_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/")
    driver.maximize_window()
    time.sleep(2)

a=1
@pytest.mark.skipif(a>100,reason='No execution required in UAT env')
@pytest.mark.regression
def test_fourth_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/")
    driver.maximize_window()
    time.sleep(2)