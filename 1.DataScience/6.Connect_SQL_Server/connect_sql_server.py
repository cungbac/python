import pyodbc

connect = pyodbc.connect(
    'Driver = {SQL Server Native Client RDA 11.0};'
    'Server = DESKTOP-FHB3M9B\SQLSERVER;'
    'Database = DKSH_MD;'
    'username = sa;'
    'password = 123456;'
    'Trusted_connection = yes;')