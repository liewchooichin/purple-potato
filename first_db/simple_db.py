# Reference
# https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql
# Driver = {ODBC Driver 18 for SQL Server} with the {} included.
#
# Results:
#
# python simple_db.py
# master SQL_Latin1_General_CP1_CI_AS
# sqllcc200 SQL_Latin1_General_CP1_CI_AS
#


import os
import pyodbc

server = 'sqllcc200.database.windows.net'
database = 'sqllcc200'
username = 'sqllcc200'
password = os.getenv("SQLLCC200_PASSWORD")
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()