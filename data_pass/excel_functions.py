import xlrd

def excel_read(file,record):
    wb1 =xlrd.open_workbook(file)
    ws =wb1.sheet_by_index(0)
    user1=ws.cell_value(record,0)
    print(user1)
    password=ws.cell_value(record,1)
    print(password)
    return user1,password

from xlutils.copy import copy
import xlrd

def update_excel(file,record,msg):
    rb = xlrd.open_workbook(file)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(record, 2, msg)
    wb.save(file)

user,password=excel_read(file="input.xls",record=1)
print(user)
print(password)

output_message="Welcome to Proseek"
update_excel(file="input.xls",record=1,msg=output_message)

#Second user
user,password=excel_read(file="input.xls",record=2)
output_message="Welcome to Amravati"
update_excel(file="input.xls",record=2,msg=output_message)

#third user
user,password=excel_read(file="input.xls",record=3)
output_message="Welcome to Hyderabad"
update_excel(file="input.xls",record=3,msg=output_message)


#instead of that
wb1 = xlrd.open_workbook("input_datadriven.xls")
ws = wb1.sheet_by_index(0)
row_count= ws.nrows
print(row_count)
for item in range(row_count):
    user, password = excel_read(file="input_datadriven.xls", record=item)
    output_message = f"Welcome to {user}"
    update_excel(file="input_datadriven.xls", record=item, msg=output_message)