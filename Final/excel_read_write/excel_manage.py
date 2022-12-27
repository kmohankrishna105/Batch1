import xlrd
wb1 =xlrd.open_workbook('../../Sample.xls')
ws =wb1.sheet_by_index(0)
user1=ws.cell_value(1,0)
print(user1)
password=ws.cell_value(1,1)
print(password)



from xlutils.copy import copy
import xlrd

rb = xlrd.open_workbook('../../Sample.xls')
wb = copy(rb)
sheet = wb.get_sheet(0)
sheet.write(1, 2, 'This is a executed Successfully and kiran is valid user')
wb.save('sample.xls')
