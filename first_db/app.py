# Reference
# Connect to and query Azure SQL Database using Python and the pyodbc driver
# https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-python-quickstart?view=azuresql&tabs=windows%2Csql-inter
#
# The sample code shows raw SQL statements, which shouldn't be used in production code. Instead, use an Object Relational Mapper (ORM) 
# package like SqlAlchemy that generates a more secure object layer to access your database.
#
# Notes:
# Need to install the Microsoft ODBC 18 from the codespaces. The changes is in the devcontainer.
# Login to Azure first: az login --use-device-code
#
# Steps:
# uvicorn app:app --reload
# On the Swagger UI page for the app http://127.0.0.1:8000/docs, expand the POST method and select Try it out.
# You can also use try /redoc to see another form of generated documentation for the API. http://127.0.0.1:8000/redoc
#
# 
#
#
#
#

import os
import pyodbc, struct
from azure import identity

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: Union[str, None] = None

#connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]
connection_string = os.getenv("SQLLCC200_CONNECTION")
print(connection_string)

app = FastAPI()

@app.get("/")
def root():
    print("Root of Person API")
    try:
        conn = get_conn()
        cursor = conn.cursor()

        # Table should be created ahead of time in production app.
        cursor.execute("""
            CREATE TABLE Persons (
                ID int NOT NULL PRIMARY KEY IDENTITY,
                FirstName varchar(15),
                LastName varchar(15)
            );
        """)

        conn.commit()
    except Exception as e:
        # Table may already exist
        print(e)
    return "Person API"

@app.get("/all")
def get_persons():
    rows = []
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Persons")

        for row in cursor.fetchall():
            print(row.FirstName, row.LastName)
            rows.append(f"{row.ID}, {row.FirstName}, {row.LastName}")
    return rows

@app.get("/person/{person_id}")
def get_person(person_id: int):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Persons WHERE ID = ?", person_id)

        row = cursor.fetchone()
        return f"{row.ID}, {row.FirstName}, {row.LastName}"

@app.post("/person")
def create_person(item: Person):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Persons (FirstName, LastName) VALUES (?, ?)", item.first_name, item.last_name)
        conn.commit()

    return item

def get_conn():
    credential = identity.DefaultAzureCredential(exclude_interactive_browser_credential=False)
    token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
    token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
    SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
    conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
    return conn