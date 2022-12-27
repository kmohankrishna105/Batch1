#import action as action
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def read_excel(file,row):
    import xlrd
    wd=xlrd.open_workbook(file)
    sw=wd.sheet_by_index(0)
    f=sw.cell_value(row,0)
    l=sw.cell_value(row,1)
    e=sw.cell_value(row,2)
    ps=sw.cell_value(row,3)
    cp=sw.cell_value(row,3)
    return f,l,e,ps,cp

import xlrd
wb=xlrd.open_workbook("cod.xls")
ws=wb.sheet_by_index(0)
total_rows=ws.nrows

for item in range(1,total_rows):
    f,l,e,ps,cp=read_excel(file="cod.xls",row=item)
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hari\\Downloads\\geckodriver\\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/customer/account/create/")
    driver.maximize_window()
    fname=driver.find_element(By.XPATH,"//input[@id='firstname']")
    fname.send_keys(f)
    lname=driver.find_element(By.XPATH,"//input[@id='lastname']")
    lname.send_keys(l)
    email = driver.find_element(By.XPATH, "//input[@id='email_address']")
    email.send_keys(e)
    password=driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(ps)
    c_password = driver.find_element(By.XPATH, "//input[@id='confirmation']")
    c_password.send_keys(cp)
    action=ActionChains(driver)
    action.click(driver.find_element(By.XPATH, "//input[@type='checkbox']")).perform()
    action.click(driver.find_element(By.XPATH, "//button[@title='Register']")).perform()
    time.sleep(2)
    #print(welcome.text)

    def update_excel(file, row, remark,msg):
        from xlutils.copy import copy
        import xlrd
        w = xlrd.open_workbook(file)
        w1 = copy(w)
        sd = w1.get_sheet(0)
        sd.write(row,4,remark)
        sd.write(row,5,msg)
        w1.save(file)

    welcome = driver.find_element(By.XPATH, "//p[@class='welcome-msg']")
    if f in welcome.text:
        print("login successfull")
        continue
    else:
        print("Login failed")

    try:
        time.sleep(1)
        error_msg = driver.find_element(By.XPATH, "//li[@class='error-msg']//span")
        print(error_msg.text)
        update_excel(file="cod.xls", row=item, remark="Issue Found", msg=error_msg.text)

    except:
        welcome = driver.find_element(By.XPATH, "//p[@class='welcome-msg']")
        print(welcome.text)
        print(f)
        if f.upper() in welcome.text:
            print("Success")
        update_excel(file="cod.xls", row=item, remark="No_Remarks", msg=welcome.text)
