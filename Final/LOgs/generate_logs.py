import logging

from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
handler_warn = logging.FileHandler('warning_log.txt')
handler_warn.setLevel(logging.WARNING)

handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warn.setFormatter(formatter)
handler_info.setFormatter(formatter)

# add the handler to the logger

logger.addHandler(handler_warn)
logger.addHandler(handler_info)

logger.info('Information')
logger.warning('warning')

path = "C:\\Users\\Hari\\Documents\\E2E_POM\\Driver\\chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome(executable_path=path)
mainWin = ""
driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings")
logger.info("This is log info")
driver.find_element(By.ID,"datepicker").click()
driver.find_element(By.XPATH,"//a[@data-handler='next']").click()
date= input("select the date:")
try:
    driver.find_element(By.XPATH,"//a[text()="+date+"]").click()
except:
    print("Invalid date entered")
