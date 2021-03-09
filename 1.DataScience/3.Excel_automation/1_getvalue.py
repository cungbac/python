import openpyxl

path = '/Users/bactran/Documents/1.Learning/2.Python/1.DataScience/3.Excel_automation/'

file_names = ['SampleData.xlsx','SampleData2.xlsx']

excel_files = [path + i for i in file_names]

values = []

# get values in a cell
for file in excel_files: 
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['SalesOrders']
    cell_value = worksheet['G11'].value
    values.append(cell_value)

    print(cell_value)

# Create new sheets
file_data1 = openpyxl.load_workbook(excel_files[0])
file_data1.create_sheet('NewSheet1')
file_data1.save(excel_files[0])