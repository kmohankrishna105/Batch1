import xlrd
wb1 =xlrd.open_workbook('../../Output.xls')
ws =wb1.sheet_by_index(0)
user1=ws.cell_value(0,1)
print(user1)