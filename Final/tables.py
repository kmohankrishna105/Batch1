import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Sample1():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Documents\\E2E_POM\\Driver\\chromedriver.exe")
    # driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/webtable/")
    driver.implicitly_wait(3)
    #driver.set_page_load_timeout(50)
    assert "webtable" in driver.title
    #table = driver.find_element_by_id("table01")
    table = driver.find_element(By.ID,"table01")

    #rows = table.find_elements_by_tag_name("tr")
    rows = table.find_elements(By.TAG_NAME,"tr")

    print("rows - " + str(len(rows)))

    for i in range(len(rows)):
        columns = rows[i].find_elements_by_tag_name("td")
        for j in range(len(columns)):
            print(columns[j].text)
            if columns[j].text == "TFS":
                columns[0].click()
                # print(columns[j].text)
    time.sleep(5)

    driver.quit()