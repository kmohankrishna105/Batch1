import xlwt
import xlrd

wbook= xlwt.Workbook()
sheet = wbook.add_sheet('Sheet 1')
sheet.write(10, 10, 'This is new statement')
wbook.save('Output1.xls')