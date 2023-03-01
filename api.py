import pyodbc
import pandas as pd

SQL_WORKLOADS_FILEPATH = "./sql/workloads.sql"
SQL_WORK_ITEMS_FILEPATH = "./sql/workitems.sql"
SQL_LOCATIONS_FILEPATH = "./sql/locations.sql"

TEST_X_FILEPATH = "./test-data/test-database.csv"
TEST_X_NEW_FILEPATH = "./test-data/test-wcat.csv"
X_NEW_FILEPATH = ""

SERVER = 'tcp:myserver.database.windows.net' 
DATBASE = 'mydb' 
USERNAME = 'myusername' 
PASSWORD = 'mypassword' 

def get_sql_workloads():
    with open(SQL_WORKLOADS_FILEPATH, "r") as query:
        return file.read().replace("\n", " ")

def get_sql_work_items():
    with open(SQL_WORK_ITEMS_FILEPATH, "r") as query:
        return file.read().replace("\n", " ")

def get_sql_locations():
    with open(SQL_LOCATIONS_FILEPATH, "r") as query:
        return file.read().replace("\n", " ")

def request_data():
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+SERVER+';DATABASE='+DATBASE+';ENCRYPT=yes;UID='+USERNAME+';PWD='+ PASSWORD)
    cursor = cnxn.cursor()
    
    workloads = cursor.execute(get_sql_workloads).fetchall() 
    work_items = cursor.execute(SQL_WORK_ITEMS_FILEPATH).fetchall() 
    locations = cursor.execute(SQL_LOCATIONS_FILEPATH).fetchall() 
    
    return 1

def request_new_data():
    return pd.read_csv(X_NEW_FILEPATH)


def test_request_data():
    return pd.read_csv(TEST_X_FILEPATH)

def test_request_test_data():
    return pd.read_csv(TEST_X_NEW_FILEPATH)
