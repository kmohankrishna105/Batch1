import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.fixture(scope="class")
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    yield
    print("\nSuccess: TC success")
    driver.close()


def test_registration(setup):
    # initiate chrome browser and navigate to URL
    driver.get("http://magento-demo.lexiconn.com/")
    #driver.maximize_window()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 100);")

@pytest.mark.xfail
def test_second_registration(setup):
    # initiate chrome browser and navigate to URL
    driver.get("https://www.youtube.com/watch?v=OsLCY3vz3t8&list=RDOsLCY3vz3t8&start_radio=1")
    driver.maximize_window()
    assert "tube" in driver.title
    time.sleep(2)

def test_third_registration(setup):
    # initiate chrome browser and navigate to URL
    driver.get("http://magento-demo.lexiconn.com/")
    driver.maximize_window()
    time.sleep(2)