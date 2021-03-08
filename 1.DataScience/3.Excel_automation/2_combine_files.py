import pandas as pd

path = '/Users/bactran/Documents/1.Learning/2.Python/1.DataScience/3.Excel_automation/'

file_names = ['SampleData.xlsx','SampleData2.xlsx']

excel_files = [path + i for i in file_names]

merge = pd.DataFrame()

for file in excel_files:
    df = pd.read_excel(file, skiprows=1)
    merge = merge.append(df, ignore_index = True)

# print(merge.head())
# print(merge.info())
merge.to_excel('merged_file.xlsx')