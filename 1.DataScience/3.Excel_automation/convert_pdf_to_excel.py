import tabula as tb
import pandas as pd

# read file
file = 'Dat_file.pdf'
table = tb.read_pdf(file)

# csv file
csv_table = tb.convert_into(file, 'Dat_file.csv')
