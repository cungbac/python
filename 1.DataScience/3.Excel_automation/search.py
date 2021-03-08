import pandas as pd
import numpy as np

path = '/Users/bactran/Documents/1.Learning/2.Python/1.DataScience/3.Excel_automation/'

file_names = ['SampleData.xlsx','SampleData2.xlsx']

excel_files = [path + i for i in file_names]

# -------------
for file in excel_files:
    df = pd.read_excel(file)
    rep = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    rep = rep.reset_index()
    rep = rep.drop('index',axis = 'columns')
    print(file)
    print(rep)

# ---------------
for file in excel_files:
    df = pd.read_excel(file)
    rep = df[['Rep','Item']]
    rep = rep[rep['Item'] == 'Pencil']
    rep = rep[['Rep']]
    print(file)
    print(rep)