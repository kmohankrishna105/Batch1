"""Pytest cases

Group Test cases together
Execute specific grp - Progression,Regression,Smoke,Sanity,shakedown
Execute all others other than Specific grp

pytest -m regression -v

"""


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.lexiconn
def test_registration_tc002():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 400)")
    time.sleep(2)

@pytest.mark.youtube
def test_second_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("https://www.youtube.com/watch?v=OsLCY3vz3t8&list=RDOsLCY3vz3t8&start_radio=1")
    driver.maximize_window()
    time.sleep(2)


@pytest.mark.wikipedia
def test_third_registration():
    # initiate chrome browser and navigate to URL
    driver=webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()
    time.sleep(2)

#
# cmd :  pytest
#Execute all test cases starting with 'Test'

#cmd : pytest <filename.py>
#Execute all test cases in specific file


#cmd : pytest -m <Tag name> <filename.py>
#Execute all test cases with the tag name mentioned

#run with disable warning
#pytest -v -m wikipedia --disable-warnings  test_TC002_verifyLogin.py

#Run Specific test case
#pytest -v test_TC002_verifyLogin.py::test_third_registration

#Run last failed
#pytest -v --last-failed

