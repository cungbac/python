import openpyxl
import os


path = str(os.getcwd()) + '/'

file_names = ['SampleData.xlsx','SampleData2.xlsx']

excel_files = [path + i for i in file_names]

for file in excel_files:
    # open workbook
    workbook = openpyxl.load_workbook(file)

    # select worksheet
    worksheet = workbook['NewSheet']

    # add value into cells
    for i in range(1,10):
        worksheet['A'+str(i)] = i ** 2

    # set a formular in a cell
    worksheet['A10'] = '=SUM(A1:A9)'

    # save the file
    workbook.save(file)